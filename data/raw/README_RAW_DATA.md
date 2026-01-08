# Raw Data Sources

This directory should contain the raw data files used to construct the processed datasets.

## Required Files

### 1. COVID-19 Vaccination Data
**Filename**: `covid_vaccination_data.csv`  
**Source**: Santé Publique France - VACSI  
**URL**: https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/  
**Variables**: Department code, vaccination coverage by age group, dates  
**Sample size**: 101 French departments  
**Date**: 2021-2022

### 2. Socioeconomic Data (FILOSOFI)
**Filename**: `filosofi_2021_revenus.csv`  
**Source**: INSEE - FILOSOFI 2021  
**URL**: https://www.insee.fr/fr/statistiques/7233950  
**Variables**: Median income, poverty rate, Gini coefficient by department  
**Sample size**: 101 French departments  
**Date**: 2021

### 3. Education - IPS Lycées
**Filename**: `ips_lycees_2024.csv`  
**Source**: Ministère de l'Éducation Nationale - Open Data  
**URL**: https://data.education.gouv.fr/explore/dataset/fr-en-ips_lycees/  
**Variables**: IPS (Social Position Index), lycée characteristics  
**Sample size**: ~4,000 lycées  
**Date**: 2024

### 4. Education - Baccalauréat Results
**Filename**: `bac_resultats_2024.csv`  
**Source**: Ministère de l'Éducation Nationale - Open Data  
**URL**: https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-de-resultat-des-lycees-denseignement-general-et-technologique/  
**Variables**: Success rates, value-added indicators  
**Sample size**: ~4,000 lycées  
**Date**: 2024

---

## Data Processing

The raw data files are processed using the scripts in `scripts/validation/` to create:
- `data/processed/Article2_Dataset_COVID.csv` (n=65 departments)
- `data/processed/Article2_Dataset_Education.csv` (n=2,325 lycées)

See `data/README.md` for detailed processing steps.

---

## Note

Raw data files are **not included** in this repository due to:
1. **Size**: Large CSV files (several MB each)
2. **Licensing**: Public data but with redistribution restrictions
3. **Reproducibility**: Processed datasets are sufficient for replication

To reconstruct the full pipeline:
1. Download raw data from official sources (links above)
2. Place files in this directory
3. Run processing scripts in `scripts/validation/`

---

**Last updated**: January 2026
