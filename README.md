<h2> Weaviate BEIR Benchmarks </h2>

This repository contains the BEIR benchmark datasets in Weaviate!

The goal of this library is to facilitate research in text information retrieval!

Firstly download a Weaviate BEIR Backup and then organize your filesystem like this (e.g. with nfcorpus backup folder):
```md
-- backups -- nfcorpus
-- tmp     -- backups
docker-compose.yml
restore.py
ndcg-tests.py
```
<br />
Run these 3 commands to get the nDCG and hits at 1 / hits at 5 metrics for a BEIR dataset!
<br />
(Make sure to download the Backup and Query files from the links below)
```bash
docker-compose up -d
python3 restore.py --name NFCorpus
python3 ndcg-test.py --name NFCorpus --alpha 0.5
```

Weaviate Backups
<ul>
  <li> NFCorpus - https://storage.googleapis.com/weaviate-nfcorpus/nfcorpus.zip </li>
  <li> FIQA - https://storage.googleapis.com/weaviate-fiqa/fiqa.zip </li>
  <li> Arguana - https://storage.googleapis.com/weaviate-arguana/arguana.zip </li>
  <li> SCIDOCS - https://storage.googleapis.com/weaviate-scidocs/scidocs.zip </li>
  <li> SCIFACT - https://storage.googleapis.com/weaviate-scifact/scifact.zip </li>
  <li> TREC-COVID - https://storage.googleapis.com/weaviate-trec-covid/trec-covid.zip </li>
</ul>

Query Files
<ul>
  <li> NFCorpus - https://storage.googleapis.com/weaviate-nfcorpus/NFCorpus-Query.json </li>
  <li> FIQA - https://storage.googleapis.com/weaviate-fiqa/FIQA-Query.json.zip </li>
  <li> Arguana - https://storage.googleapis.com/weaviate-arguana/ARGUANA-Query.json.zip </li>
  <li> SCIDOCS - https://storage.googleapis.com/weaviate-scidocs/SCIDOCS-Query.json.zip </li>
  <li> SCIFACT - https://storage.googleapis.com/weaviate-scifact/SCIFACT-Query.json.zip </li>
  <li> TREC-COVID - https://storage.googleapis.com/weaviate-trec-covid/TREC-COVID-Query.json.zip </li>
</ul>
