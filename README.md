<h2> Weaviate BEIR Benchmarks </h2>

This repository contains the BEIR benchmark datasets in Weaviate!

The goal of this library is to facilitate research in text information retrieval!


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
  <li> NFCorpus - https://storage.googleapis.com/nfcorpus/nfcorpus.zip </li>
  <li> FIQA - https://storage.googleapis.com/fiqa/fiqa.zip </li>
  <li> Arguana - https://storage.googleapis.com/arguana/arguana.zip </li>
  <li> SCIDOCS - https://storage.googleapis.com/weaviate-scidocs/scidocs.zip </li>
  <li> SCIFACT - https://storage.googleapis.com/weaviate-scifact/scifact.zip </li>
  <li> TREC-COVID - https://storage.googleapis.com/weaviate-trec-covid/trec-covid.zip </li>
</ul>

Query Files
<ul>
  <li> NFCorpus - </li>
</ul>
