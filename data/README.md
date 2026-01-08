# Data Directory

This directory contains datasets used for Saviesa framework validation.

---

## 📂 Structure

```
data/
├── raw/                    # Raw data sources (original files)
└── processed/              # Processed datasets (ready for analysis)
```

---

## 📊 Datasets

### **1. COVID-19 Validation (n=65 departments)**

**File**: `processed/Article2_Dataset_COVID.csv`

**Variables**:
- `department_code`: INSEE department code (01-95)
- `department_name`: Department name
- `L`: Levier (normalized [0,1]) - Vaccination infrastructure
- `M`: Milieu (normalized [0,1]) - Socio-economic context
- `F`: Performance (normalized [0,1]) - Vaccination rate
- `facteur_limitant`: Identified limiting factor (L or M)

**Sample size**: n=65 departments with complete data

---

### **2. Education Validation (n=2,325 lycées)**

**File**: `processed/Article2_Dataset_Education.csv`

**Variables**:
- `lycee_id`: Unique lycée identifier
- `O`: Orientation (normalized [0,1]) - Lycée type (GT vs Pro)
- `L`: Levier (normalized [0,1]) - Resources and capacity
- `M`: Milieu (normalized [0,1]) - Student socio-economic background (IPS)
- `F`: Performance (normalized [0,1]) - Baccalauréat success rate

**Sample size**: n=2,325 lycées

---

## 🔗 Data Sources

### **COVID-19**
1. **Vaccination**: Data.gouv.fr - COVID-19 vaccination by department
   - URL: https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/
   - Date: December 2021

2. **Revenues**: INSEE FILOSOFI 2021
   - URL: https://www.insee.fr/fr/statistiques/fichier/6036907/FILO2021_DEC_csv.zip
   - Variables: Median income, D1, D9, poverty rate

### **Education**
1. **IPS (Social Position Index)**: Ministère Éducation Nationale
   - URL: https://data.education.gouv.fr/explore/dataset/fr-en-ips_lycees/
   - Year: 2024

2. **Baccalauréat results**: Open Data Éducation
   - URL: https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-de-resultat-des-lycees-denseignement-general-et-technologique/
   - Year: 2024

---

## 📋 Data Processing

Raw data is processed using:
- `scripts/validation/01_data_preprocessing.py`

Processing steps:
1. Load raw data sources
2. Merge datasets by geographic/institutional identifiers
3. Handle missing values (exclusion or imputation)
4. Normalize variables to [0,1] range
5. Identify limiting factors
6. Export processed datasets

---

## 📄 License

Data sources are publicly available under open licenses. Processed datasets follow the same terms.

---

## 📧 Questions?

Contact: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)
