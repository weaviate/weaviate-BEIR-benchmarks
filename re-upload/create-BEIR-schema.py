import weaviate
import time

client = weaviate.Client("http://localhost:8080")

schema = {
   "classes": [
       {
           "class": "Document",
           "description": "A BEIR document.",
           "moduleConfig": {
               "text2vec-transformers": {
                    "skip": False,
                    "vectorizeClassName": False,
                    "vectorizePropertyName": False
                }
           },
           "vectorIndexType": "hnsw",
           "vectorizer": "text2vec-transformers",
           "properties": [
               {
                   "name": "document",
                   "dataType": ["text"],
                   "description": "The text content in the BEIR document.",
                   "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": False,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                   }
               },
               {
                   "name": "DocID",
                   "dataType": ["int"],
                   "description": "The Document ID (these are mapped from the original BEIR doc ids to a sequential index.",
                   "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": True,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                   }
               },
           ]
       },{
            "class": "Query",
            "description": "A BEIR query.",
            "moduleConfig": {
                "text2vec-transformers": {
                    "skip": False,
                    "vectorizePropertyName": False,
                    "vectorizeClassName": False
                }
            },
            "vectorIndexType": "hnsw",
            "vectorizer": "text2vec-transformers",
            "properties": [
                {
                    "name": "query",
                    "dataType": ["text"],
                    "description": "The text content in the BEIR query.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": False,
                            "vectorizePropertyName": False,
                        }
                    }

                },
                {
                    "name": "queryID",
                    "dataType": ["text"],
                    "description": "The Query ID this is preserved as the original query id in the BEIR dataset.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": True,
                            "vectorizePropertyName": False,
                            "vectorizeClassName": False
                        }
                    }
                },
                {
                    "name": "matchingDocIDs",
                    "dataType": ["int[]"],
                    "description": "The matching document ids (these have been mapped to a sequential index).",
                    "moduleConfig": {
                    "text2vec-transformers": {
                        "skip": True,
                        "vectorizePropertyName": False,
                        "vectorizeClassName": False
                    }
                   }
                },
                {
                    "name": "matchingDoc_text",
                    "dataType": ["text[]"],
                    "description": "The matching documents labeled by humans.",
                    "moduleConfig": {
                        "text2vec-transformers": {
                            "skip": True,
                            "vectorizePropertyName": False,
                            "vectorizeClassName": False
                        }
                    }
                }
            ]
       }
   ]
}

client.schema.create(schema)