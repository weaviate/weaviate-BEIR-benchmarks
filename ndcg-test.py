import weaviate
import math
import time
import re
import argparse

parser = argparse.ArgumentParser(description="BEIR Dataset Name")
parser.add_argument("--name", type=str)
parser.add_argument("--alpha", type=float)
args = parser.parse_args()

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

print("Loaded queries into local memory.")

nDCG = 0
hits_at_1 = 0
hits_at_5 = 0

start = time.time()
for idx, query_obj in enumerate(queries):
    # may want to move this intermediate monitoring into a CLI argument
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
                    hybridSearch: {
                        query: "%s"
                        alpha: %s
                    }
                ){
                docID
                }
            }
        }
    """ % (query, args.alpha)
    results = client.query.raw(weaviate_query_str)["data"]["Get"]["Document"]

    DCG = 0
    for rank, doc_obj in enumerate(results):
        if doc_obj["docID"] in matchingDocIDs:
            if rank == 0:
                hits_at_1 += 1
            if rank < 5:
                hits_at_5 += 1
            DCG +=  1 / math.log(rank+2)

    nDCG += (DCG / IDCG)

nDCG /= len(queries)
print(f"Calculated nDCG, hits_at_k metrics in {time.time() - start} seconds.")
print(f"nDCG = {nDCG}, hits_at_1 = {hits_at_1}, hits_at_5 = {hits_at_5}.")    



