# Getting Started with Saviesa Framework

This guide will help you set up and run your first Saviesa validation.

---

## 📋 Prerequisites

- **Python 3.11+** installed
- **Git** installed
- Basic knowledge of Python and command line

---

## 🚀 Installation

### **Step 1: Clone the repository**

```bash
git clone https://github.com/jcbogui/saviesa-framework.git
cd saviesa-framework
```

### **Step 2: Create virtual environment (recommended)**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔬 Running Your First Validation

### **COVID-19 Validation**

```bash
python scripts/validation/validation_covid.py
```

**Expected output:**
```
Dataset chargé: n=65 départements

============================================================
VALIDATION COVID-19 (n=65)
============================================================

[1/3] Modèle M0 (Additif)...
  R² = 0.9951
  RMSE = 0.0061
  MAE = 0.0048

[2/3] Modèle M1 (Interaction)...
  R² = 1.0000
  RMSE = 0.0000
  MAE = 0.0000

[3/3] Modèle M2 (Multiplicatif)...
  R² = 1.0000
  RMSE = 0.0000
  MAE = 0.0000

✅ Résultats sauvegardés: results/Validation_COVID_Results.csv
```

---

## 📊 Understanding the Results

### **Key Metrics**

- **R²**: Proportion of variance explained (higher = better)
- **RMSE**: Root Mean Squared Error (lower = better)
- **MAE**: Mean Absolute Error (lower = better)

### **Model Comparison**

| Model | Description | When to use |
|-------|-------------|-------------|
| **M0 (Additif)** | F = α₀ + α_L·L + α_M·M | Compensatory factors |
| **M1 (Interaction)** | M0 + α_I·(L×M) | Partial non-compensability |
| **M2 (Multiplicatif)** | log(F) = β₀ + β_L·log(L) + β_M·log(M) | Full non-compensability |

### **Interpretation**

**COVID-19 results** show:
- M2 (Multiplicatif) achieves R²=1.0000 (perfect fit)
- M0 (Additif) achieves R²=0.9951 (good but suboptimal)
- **Conclusion**: Non-compensatory structure confirmed

---

## 📈 Next Steps

### **1. Explore Education Validation**

```bash
python scripts/validation/validation_education.py
```

### **2. Run Diagnostic Comparison**

```bash
python scripts/validation/diagnostic_differentiel.py
```

### **3. Try LOOCV Validation**

```bash
python scripts/validation/loocv_validation.py
```

### **4. Explore Jupyter Notebooks**

```bash
jupyter notebook examples/example_covid.ipynb
```

---

## 🔧 Troubleshooting

### **Issue: Module not found**

**Solution**: Ensure you activated the virtual environment and installed dependencies:
```bash
pip install -r requirements.txt
```

### **Issue: Data file not found**

**Solution**: Ensure you're in the project root directory:
```bash
cd saviesa-framework
python scripts/validation/validation_covid.py
```

### **Issue: Python version**

**Solution**: Check Python version (must be 3.11+):
```bash
python --version
```

---

## 📚 Further Reading

- [Methodology](methodology.md): Theoretical foundations
- [API Reference](api_reference.md): Code documentation
- [Tutorials](tutorials/): Step-by-step guides

---

## 📧 Need Help?

- **Issues**: [GitHub Issues](https://github.com/jcbogui/saviesa-framework/issues)
- **Email**: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)

---

**Happy validating!** 🎉
