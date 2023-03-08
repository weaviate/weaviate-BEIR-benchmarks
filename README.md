<h2> Weaviate BEIR Benchmarks </h2>

This repository contains the BEIR benchmark datasets in Weaviate!

To run the tests, first grab the backup and query files from the google drive links below:

YOur file system should look like this:
```md
-- backups / {BEIR-dataset-name}
-- BEIR-Files / {BEIR-dataset-name}-Query.json
docker-compose.yml
restore.py
get-metrics.py
```
<br />
Run these 3 commands to get the nDCG and hits at 1 / hits at 5 metrics for a BEIR dataset!
<br />
(Make sure to download the Backup and Query files from the links below)

```bash
docker-compose up -d
python3 restore.py --name NFCorpus
python3 get-metrics.py --name NFCorpus --alpha 0.5
```

Weaviate Backups
<ul>
  <li> NFCorpus - https://drive.google.com/file/d/17Y4gh5AJUqSceXESissWck6YT62biEjK/view?usp=sharing </li>
  <li> FIQA - https://drive.google.com/file/d/12T_rPc_RaaSt6H_we6cOjozCddlHsE2v/view?usp=sharing </li>
  <li> ARGUANA - https://drive.google.com/file/d/1eUFASQZ0UG_mW2aluRj-FkpXGowDlVIL/view?usp=sharing </li>
  <li> SCIDOCS - https://storage.googleapis.com/weaviate-scidocs/scidocs.zip </li>
  <li> SCIFACT - https://storage.googleapis.com/weaviate-scifact/scifact.zip </li>
  <li> TREC-COVID - https://storage.googleapis.com/weaviate-trec-covid/trec-covid.zip </li>
  <li> QUORA - </li>
  <li> Natural Questions - </li>
</ul>

Query Files (These need to be extended with multi-relevance labels)
<ul>
  <li> NFCorpus - https://drive.google.com/file/d/1FCmjtBF4VQwsoeUIUt6oP_rmDSgkPpFE/view?usp=sharing </li>
  <li> FIQA - https://drive.google.com/file/d/1fKZouQq_s-Lg7-GhJ4Dp83Q-rH7dkimI/view?usp=sharing </li>
  <li> ARGUANA - https://drive.google.com/file/d/1sbRy8zJhD9_ZwcgXISfqu2b9_AlOhcwD/view?usp=sharing </li>
  <li> SCIDOCS - https://drive.google.com/file/d/1himnjWVMLR2VDlYoFBWGayScrG32ipAu/view?usp=sharing </li>
  <li> SCIFACT - https://drive.google.com/file/d/1Ah95b_tIPd6PLmYUDqQ-iVN58aTQxS_Q/view?usp=sharing </li>
  <li> TREC-COVID - https://drive.google.com/file/d/141MhWA2OeYUI42AgibNA7VEZU4J4sVua/view?usp=sharing </li>
  <li> TOUCHE2020 - https://drive.google.com/file/d/1--a6mu0pBYLXpOzeXgK3iXGcwzrFS9IA/view?usp=sharing </li>
  <li> QUORA - https://drive.google.com/file/d/1-7uB1Od7T0i1H9DH-SoI6fX8fRNn6JD2/view?usp=sharing </li>
  <li> NQ - https://drive.google.com/file/d/1yH-jmuBahv1SCaj8lfz012j-foiVzMcB/view?usp=sharing </li>
</ul>

Corpus Files (coming soon)
