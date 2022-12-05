import weaviate
import json
import argparse

parser = argparse.ArgumentParser(description="BEIR Dataset Name")
parser.add_argument("--name", type=str)
args = parser.parse_args()

client = weaviate.Client("http://localhost:8080")

result = client.backup.restore(
    backup_id=args.name,
    backend='filesystem',
    wait_for_completion=True
)

print(json.dumps(result, indent=4))