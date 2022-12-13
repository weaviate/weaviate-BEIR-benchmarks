import weaviate
import time
import argparse

parser = argparse.ArgumentParser(description="BEIR Dataset Name")
parser.add_argument("--name", type=str)
args = parser.parse_args()

BEIR_dataset_name = args.name

import json

f = open(f"./BEIR-Files/{BEIR_dataset_name}-Corpus.json")
import json
json_data = json.load(f)
f.close()
json_list = list(json_data)

corpus = []

for json_dict in json_list:
  new_doc_obj = {}
  for key in json_dict.keys():
    new_doc_obj[key] = json_dict[key]
  corpus.append(new_doc_obj)

f = open(f"./BEIR-Files/{BEIR_dataset_name}-Query.json")
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


client = weaviate.Client("http://localhost:8080")

from weaviate.util import generate_uuid5

# batch import, will update this very
'''
client.batch.configure(
    batch_size=16,
    dynamic=True,
    timeout_retries=3,
    callback=None,
)
'''

doc_upload_start = time.time()
for doc_idx, doc in enumerate(corpus):
    data_properties = {
        "document": doc["document"],
        "docID": doc["DocID"]
    }
    id = generate_uuid5(doc_idx)
    doc_vector = doc["vector"]
    #client.batch.add_data_object(data_properties, "Document", id, doc_vector)
    client.data_object.create(
        data_object = data_properties,
        class_name = "Document",
        vector = doc_vector,
        uuid=id
    )

print(f"Uploaded {len(corpus)} documents in {time.time() - doc_upload_start} seconds.")

# if uploading queries as well

'''
query_upload_start = time.time()  
for query_idx, query in enumerate(queries):
    data_properties = {
        "query": query["query"],
        "queryID": query["queryID"],
        "matchingDocIDs": query["matchingDocIDs"]
    }
    id = generate_uuid5(doc_idx+query_idx+1)
    client.data_object.create(
        data_object = data_properties,
        class_name = "Query",
        uuid=id
    )
print(f"Uploaded {len(queries)} queries in {time.time() - query_upload_start} seconds.")
'''
print("The objects have been uploaded to Weaviate.")