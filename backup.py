import weaviate
import json
import argparse

parser = argparse.ArgumentParser(description="BEIR Dataset Name")
parser.add_argument("--name", type=str)
args = parser.parse_args()

w1 = weaviate.Client("http://localhost:8080")

# add an extra check to make sure we aren't overwriting an existing backup!!

result = w1.backup.create(
    backup_id=args.name,
    backend='filesystem',
)

print(json.dumps(result, indent=4))