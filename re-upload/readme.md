<h1> Re-Upload </h1>

In addition to the collection of Backups, this folder contains the necessary scripts for uploading the BEIR data to Weaviate.
<br />
<br />
Please begin by grabbing query and corpus files from the main landing page of Weaviate-BEIR-Benchmarks/readme.md
<br />
```bash
python3 create-BEIR-schema.py
python3 upload.py --name NFCorpus
```
