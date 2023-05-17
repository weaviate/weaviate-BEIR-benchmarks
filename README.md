<h2> Weaviate BEIR Benchmarks </h2>

This repository contains the <a href = "https://arxiv.org/abs/2104.08663">BEIR benchmark datasets</a> in Weaviate!

To run the tests, first grab the backup and query files from the google drive links below:

Your file system should look like this:
```md
-- backups / {BEIR-dataset-name}
-- BEIR-Files / {BEIR-dataset-name}-Query.json
docker-compose.yml
restore.py
get-metrics.py
```
<br />
Run with these 3 commands:

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
  <li> SCIDOCS - https://drive.google.com/file/d/1cX4y_4NuZ5jyI6ujbbIbw5JG_nkwDbix/view?usp=sharing </li>
  <li> SCIFACT -  https://drive.google.com/file/d/1VyOHExz1tXzfIYYENoBB4Y4kTIwvm2QL/view?usp=sharing </li>
  <li> TREC-COVID - https://drive.google.com/file/d/1A5tfafCtIpsSonvO6bbOJ5-iRORdFDjS/view?usp=sharing</li>
  <li> TOUCHE2020 - https://drive.google.com/file/d/1gJk30-OU32zXfJUYdrmn4pO-LzV4tdYw/view?usp=sharing </li>
  <li> QUORA - https://drive.google.com/file/d/1ZLUCJxsOhr_AbUL06DLG3qh6QU5MEB1Z/view?usp=sharing </li>
  <li> Natural Questions - https://drive.google.com/file/d/1WevhlcWnoSIHpskvs0DGsbXrsa2V7pmv/view?usp=sharing </li>
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

More particularly, these 4 datasets need the multi-relevance labels,
- TREC-COVID
- NFCorpus
- Touche-2020
- DBPedia
