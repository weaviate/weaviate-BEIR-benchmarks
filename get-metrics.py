import weaviate
import math
import time
import re
import argparse

parser = argparse.ArgumentParser(description="BEIR Dataset Name")
parser.add_argument("--name", type=str)
parser.add_argument("--alpha", type=float)
args = parser.parse_args()

# ToDo, ^ add check for this

client = weaviate.Client("http://localhost:8080")

# Could also get the queries from the Weaviate backup

f = open(f"./BEIR-Files/{args.name}-Query.json")
import json
json_data = json.load(f)
f.close()
json_list = list(json_data)

queries = []

for json_dict in json_list:
  new_query_obj = {}
  for key in json_dict.keys():
    new_query_obj[key] = json_dict[key]
  queries.append(new_query_obj)

print(f"Loaded {len(queries)} queries into local memory.")

nDCG = 0
hits_at_1 = 0
hits_at_5 = 0
hits_at_100 = 0
total_recall = 0
#total_precision = 0

start = time.time()
for idx, query_obj in enumerate(queries):
    # may want to move this intermediate monitoring into an optional CLI argument
    if idx % 100 == 99:
        print(f"{idx} queries tested in {time.time() - start} seconds.")
        print(f"Current nDCG = {nDCG/(idx+1)}, hits_at_1 = {hits_at_1}, hits_at_5 = {hits_at_5}.")
    query = query_obj["query"]
    matchingDocIDs = query_obj["matchingDocIDs"]

    IDCG = 0
    # need to update for non-binary relevance
    for pos_doc_counter in range(len(matchingDocIDs)):
        IDCG += 1 / math.log(pos_doc_counter + 2)
    
    query = re.sub('"', '', query)
    weaviate_query_str = """
    {
            Get {
                Document (
                    hybrid: {
                        query: "%s"
                        alpha: %s
                    },
                    limit: 100
                ){
                docID
                }
            }
    }
    """ % (query, args.alpha)
    # note add limit: 10 above to configure i.e. NDCG@10 or whatever k
    try: # there is a latex expression in the Quora dataset that it doesn't like
        results = client.query.raw(weaviate_query_str)["data"]["Get"]["Document"]

        DCG = 0
        local_hits_at_100 = 0
        for rank, doc_obj in enumerate(results):
            if doc_obj["docID"] in matchingDocIDs:
                if rank == 0:
                    hits_at_1 += 1
                if rank < 5:
                    hits_at_5 += 1
                local_hits_at_100 += 1
                DCG +=  1 / math.log(rank+2)

        hits_at_100 += local_hits_at_100
        total_recall += local_hits_at_100 / len(matchingDocIDs)
        #total_precision += hits_at_1 / len(results) # more important to with AutoCut
        nDCG += (DCG / IDCG)
    except:
        print(f"This query caused a failure {query}")

nDCG /= len(queries)
average_recall = total_recall / len(queries)
print(f"Calculated nDCG, hits_at_k metrics in {time.time() - start} seconds.")
print(f"nDCG = {nDCG}, hits_at_1 = {hits_at_1}, hits_at_5 = {hits_at_5}, hits_at_100 = {hits_at_100}, average_recall = {average_recall}")    



