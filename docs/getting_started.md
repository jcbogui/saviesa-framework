# Getting Started with Saviesa Framework

This guide will help you get started with the Saviesa Framework for institutional performance diagnosis.

---

## 📋 Prerequisites

- **Python 3.11+**
- **pip** (Python package manager)
- **Git** (for cloning the repository)

---

## 🚀 Installation

### **1. Clone the repository**

```bash
git clone https://github.com/jcbogui/saviesa-framework.git
cd saviesa-framework
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

**Required packages**:
- numpy, pandas, scipy
- scikit-learn, statsmodels
- matplotlib, seaborn, plotly
- jupyter, pytest

---

## 🎯 Running Validations

### **COVID-19 Validation**

Validate the Saviesa framework on COVID-19 vaccination data (n=65 French departments):

```bash
python scripts/validation/validation_covid.py
```

**Expected output**:
- Model comparison (Additive, Interaction, Multiplicative)
- Performance metrics (R², RMSE, MAE, AIC)
- Results saved to `results/covid_validation.csv`

---

### **Education Validation**

Validate on education performance data (n=2,325 lycées):

```bash
python scripts/validation/validation_education.py
```

**Expected output**:
- Model comparison (Additive, Multiplicative)
- Coefficient interpretation
- Results saved to `results/education_validation.csv`

---

### **Diagnostic Comparison**

Compare multiplicative vs. additive diagnostics:

```bash
python scripts/validation/diagnostic_differentiel.py
```

**Expected output**:
- Limiting factor identification for each department
- Convergence/divergence analysis
- Divergence rate: 43.1%
- Results saved to `results/diagnostic_comparison.csv`

---

## 📓 Interactive Examples

### **Jupyter Notebooks**

Launch Jupyter to explore interactive examples:

```bash
jupyter notebook
```

Then open:
- `examples/example_covid.ipynb` - COVID-19 validation walkthrough
- `examples/example_education.ipynb` - Education validation walkthrough

---

## 🧪 Running Tests

Run unit tests to verify installation:

```bash
pytest tests/
```

**Test coverage**:
- `test_models.py` - Model implementations
- `test_metrics.py` - Performance metrics

---

## 📊 Using Your Own Data

### **Data Format**

Your dataset should be a CSV file with the following columns:

```csv
id,L,M,F
1,0.75,0.82,0.65
2,0.68,0.91,0.72
...
```

Where:
- **L**: Levier (resources/capacity), normalized [0,1]
- **M**: Milieu (environment/context), normalized [0,1]
- **F**: Performance outcome, normalized [0,1]

### **Example Code**

```python
import pandas as pd
from scripts.utils.models import MultiplicativeModel

# Load your data
df = pd.read_csv('your_data.csv')
X = df[['L', 'M']].values
y = df['F'].values

# Fit multiplicative model
model = MultiplicativeModel()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Get R²
r2 = model.score(X, y)
print(f"R² = {r2:.4f}")
```

---

## 🔧 Troubleshooting

### **Import Errors**

If you encounter import errors:

```bash
# Ensure you're in the project root directory
cd saviesa-framework

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### **Data Not Found**

If validation scripts can't find data:

```bash
# Check data directory structure
ls data/processed/

# Should contain:
# - Article2_Dataset_COVID.csv
```

### **Python Version**

Check your Python version:

```bash
python --version
# Should be 3.11 or higher
```

---

## 📚 Further Reading

- **Methodology**: See [README.md](../README.md) for detailed methodology
- **API Reference**: See docstrings in `scripts/utils/` modules
- **Contributing**: See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/jcbogui/saviesa-framework/issues)
- **Email**: jean.bogui@proton.me
- **Documentation**: [docs/](.)

---

**Happy analyzing!** 🎉
