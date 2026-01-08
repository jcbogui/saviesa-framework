<<<<<<< HEAD
# Saviesa Framework

**Institutional Performance Diagnosis Based on Non-Compensatory Constraints**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--9896--5653-green.svg)](https://orcid.org/0009-0006-9896-5653)

---

## 🔬 Overview

**Saviesa** is a diagnostic framework for institutional performance that identifies **limiting factors** (Orientation, Levier, Milieu) and prescribes **targeted interventions** based on non-compensatory constraints.

Unlike traditional additive models that assume factor compensability, Saviesa uses a **multiplicative structure** (ℱ = 𝒪 × ℒ × ℳ) where performance is constrained by the weakest dimension—similar to Liebig's Law of the Minimum in agronomy.

### **Key Innovation**

**Constraint-based diagnostics** reveal that 43.1% of policy recommendations diverge from traditional approaches, with **10-25× efficiency gains** in resource allocation.

---

## 📊 Empirical Validation

Validated on **French public policies** with n=2,390 observations across two domains:

### **1. COVID-19 Vaccination (n=65 departments)**

| Metric | Multiplicative | Additive | Gain |
|--------|---------------|----------|------|
| **R²** | 1.0000 | 0.9951 | +0.49% |
| **RMSE** | 0.0000 | 0.0061 | -100% |
| **Limiting factor identification** | 100% Milieu | Mixed | Perfect |

**Result**: Multiplicative model achieves perfect fit, confirming non-compensatory structure in health policy context.

---

### **2. Education Performance (n=2,325 lycées)**

| Metric | Multiplicative | Additive | Gain |
|--------|---------------|----------|------|
| **R²** | 0.4922 | 0.4888 | +0.34% |
| **RMSE** | 0.0681 | 0.0714 | -4.6% |
| **MAE** | 0.0538 | 0.0565 | -4.8% |

**Result**: Multiplicative model shows superior predictive performance and diagnostic accuracy.

---

### **3. Diagnostic Divergence**

**43.1%** of departments receive **different recommendations** under multiplicative vs additive diagnostics:

- **Convergent cases** (56.9%): Both models agree on limiting factor
- **Divergent cases** (43.1%): Multiplicative identifies different constraint
  - **Efficiency gain**: 10-25× resource allocation optimization
  - **Example**: Department investing in Levier when Milieu is limiting → wasted resources

---

## 🚀 Quick Start

### **Installation**

```bash
# Clone repository
git clone https://github.com/jcbogui/saviesa-framework.git
cd saviesa-framework

# Install dependencies
pip install -r requirements.txt
```

### **Run Validation**

```python
# COVID-19 validation
python scripts/validation/validation_covid.py

# Education validation
python scripts/validation/validation_education.py

# Diagnostic comparison
python scripts/validation/diagnostic_differentiel.py
```

---

## 📂 Repository Structure

```
saviesa-framework/
├── README.md                  # This file
├── LICENSE                    # MIT License
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
│
├── data/                      # Datasets
│   ├── raw/                   # Raw data sources
│   │   ├── covid_vaccination_data.csv
│   │   ├── filosofi_2021_revenus.csv
│   │   ├── ips_lycees_2024.csv
│   │   └── bac_resultats_2024.csv
│   └── processed/             # Processed datasets
│       ├── Article2_Dataset_COVID.csv
│       └── Article2_Dataset_Education.csv
│
├── scripts/                   # Analysis scripts
│   ├── validation/            # Validation scripts
│   │   ├── validation_covid.py
│   │   ├── validation_education.py
│   │   ├── diagnostic_differentiel.py
│   │   └── loocv_validation.py
│   └── utils/                 # Utility functions
│       ├── models.py          # Model implementations
│       ├── metrics.py         # Performance metrics
│       └── visualization.py   # Plotting functions
│
├── figures/                   # Generated visualizations
│   ├── Figure1_Distribution_Limitants_COVID.png
│   ├── Figure2_Scatter_Education.png
│   └── Figure3_Carte_France_COVID.png
│
├── docs/                      # Documentation
│   ├── tutorials/             # Step-by-step guides
│   │   ├── 01_getting_started.md
│   │   ├── 02_data_preparation.md
│   │   └── 03_running_validation.md
│   ├── methodology.md         # Methodological details
│   └── api_reference.md       # Code documentation
│
├── examples/                  # Example notebooks
│   ├── example_covid.ipynb
│   └── example_education.ipynb
│
└── tests/                     # Unit tests
    ├── test_models.py
    ├── test_metrics.py
    └── test_validation.py
```

---

## 📚 Methodology

### **Saviesa Principle**

Performance ℱ is modeled as:

**ℱ = 𝒪 × ℒ × ℳ**

Where:
- **𝒪 (Orientation)**: Strategic clarity and goal alignment
- **ℒ (Levier)**: Operational capacity and resources
- **ℳ (Milieu)**: Environmental context and constraints

### **Limiting Factor Identification**

The **limiting factor** is the dimension with the lowest normalized value:

**Limiting Factor = argmin(𝒪, ℒ, ℳ)**

### **Validation Method**

- **LOOCV (Leave-One-Out Cross-Validation)**: Tests predictive robustness
- **Robustness tests**: 6 specifications (sample size, outliers, variables, estimation)
- **Diagnostic comparison**: Multiplicative vs additive recommendations

---

## 📈 Key Results Summary

| Validation | n | R² Mult. | R² Add. | Δ R² | Diagnostic Divergence |
|------------|---|----------|---------|------|----------------------|
| **COVID-19** | 65 | 1.0000 | 0.9951 | +0.49% | 43.1% |
| **Education** | 2,325 | 0.4922 | 0.4888 | +0.34% | N/A |

**Robustness**: 100% (6/6 tests validated)

---

## 🔗 Related Publications

### **Preprints**

1. **Article 1**: Theoretical foundations of the Saviesa principle  
   - Status: Planned for arXiv (February 2026)

2. **Article 2**: Empirical validation on French public policies  
   - Status: Submitted to SSRN (January 2026)
   - SSRN: [Author ID 9775492](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=9775492)

### **Author**

**Jean Clément Bogui**  
- ORCID: [0009-0006-9896-5653](https://orcid.org/0009-0006-9896-5653)  
- Email: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)  
- OSF: [https://osf.io/yzchu/](https://osf.io/yzchu/)

---

## 📄 Citation

If you use this framework in your research, please cite:

```bibtex
@software{bogui_saviesa_2026,
  author = {Bogui, Jean Clément},
  title = {Saviesa Framework: Institutional Performance Diagnosis Based on Non-Compensatory Constraints},
  year = {2026},
  url = {https://github.com/jcbogui/saviesa-framework},
  note = {Python/R implementation with empirical validation (n=2,390)}
}
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Data sources: Data.gouv.fr (COVID-19), INSEE FILOSOFI (revenues), Ministère Éducation Nationale (IPS, baccalauréat)
- Validation methodology inspired by Theory of Constraints (Goldratt, 1984)
- Open Science principles: All code and data publicly accessible

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/jcbogui/saviesa-framework/issues)
- **Email**: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)
- **Documentation**: [docs/](docs/)

---

**Last updated**: January 2026  
**Version**: 1.0.0  
**Status**: ✅ Validated and ready for replication
=======
# saviesa-framework
>>>>>>> b161081d8eceb12cc0bad4394079a70b5189440d
