# Saviesa Framework

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.2139%2Fssrn.4977549-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4977549)

**A multiplicative framework for institutional performance diagnosis based on non-compensatory constraints.**

---

## Overview

The **Saviesa Framework** provides a rigorous methodology for diagnosing institutional performance by identifying **limiting factors** that constrain outcomes. Unlike traditional additive models, it uses a **multiplicative structure** where performance is determined by the weakest dimension.

### Core Model

**ℱ = 𝒪 × ℒ × ℳ**

Where:
- **ℱ (Performance)**: Observed institutional outcome
- **𝒪 (Orientation)**: Strategic clarity and institutional positioning
- **ℒ (Levier)**: Action, intervention, or resource deployment
- **ℳ (Milieu)**: Context, environment, or structural conditions

### Key Principle

**Non-compensability**: High values in one dimension cannot fully compensate for low values in another. Performance is constrained by the **minimum factor**.

---

## Key Features

- **Multiplicative model**: F = O × L × M (non-compensatory)
- **Limiting factor identification**: Diagnose which dimension constrains performance
- **Empirical validation**: Tested on French public policies (COVID-19, Education)
- **Open science**: Full reproducibility with code, data, and documentation

---

## Empirical Validation

### 1. COVID-19 Vaccination (n=65 departments)

| Model | R² | Improvement |
|-------|-----|-------------|
| **Multiplicative** | **1.0000** | - |
| Additive | 0.9951 | +0.49% |

**Key finding**: In 100% of departments, socioeconomic context (M) is the limiting factor, not vaccination coverage (L).

### 2. Education Performance (n=2,325 lycées)

| Model | R² | Improvement |
|-------|-----|-------------|
| **Multiplicative** | **0.4922** | - |
| Additive | 0.4888 | +0.34% |

**Key finding**: Social position index (IPS) explains 35.1% variance, 7× more than performance variance (5.0%).

---

## Quick Start

### Installation

```bash
git clone https://github.com/jcbogui/saviesa-framework.git
cd saviesa-framework
pip install -r requirements.txt
```

### Run COVID-19 Validation

```bash
python scripts/validation/validation_covid.py
```

**Expected output**:
```
COVID-19 Validation Results
Sample size: n=65 departments
R² (multiplicative): 1.0000
R² (additive): 0.9951
β_L: 1.000, β_M: 1.000
```

### Run Education Validation

```bash
python scripts/validation/validation_education.py
```

---

## Repository Structure

```
saviesa-framework/
├── data/
│   ├── raw/                    # Raw data sources (COVID, INSEE, DEPP)
│   └── processed/              # Processed datasets (COVID, Education)
├── scripts/
│   ├── validation/             # Validation scripts
│   └── utils/                  # Utility modules (models, metrics, viz)
├── docs/
│   ├── tutorials/              # Step-by-step guides
│   ├── methodology.md          # Theoretical framework
│   └── api_reference.md        # API documentation
├── tests/                      # Unit tests
├── examples/                   # Jupyter notebooks
└── figures/                    # Visualizations
```

---

## Documentation

- **[Getting Started](docs/getting_started.md)**: Installation and first steps
- **[Methodology](docs/methodology.md)**: Theoretical framework and mathematical model
- **[API Reference](docs/api_reference.md)**: Complete function documentation
- **[Tutorials](docs/tutorials/)**: Step-by-step guides
  - [01. Getting Started](docs/tutorials/01_getting_started.md)
  - [02. Data Preparation](docs/tutorials/02_data_preparation.md)
  - [03. Running Validation](docs/tutorials/03_running_validation.md)

---

## Citation

If you use this framework in your research, please cite:

```bibtex
@misc{bogui2024saviesa,
  title={Saviesa Framework: A Multiplicative Model for Institutional Performance Diagnosis},
  author={Bogui, Jean Clément},
  year={2024},
  publisher={GitHub},
  howpublished={\\url{https://github.com/jcbogui/saviesa-framework}},
  note={Validated on French public policies (COVID-19, Education)}
}
```

**SSRN Paper**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4977549  
**ORCID**: [0009-0006-9896-5653](https://orcid.org/0009-0006-9896-5653)

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Areas for contribution**:
- Additional empirical validations (new domains, countries)
- Extensions to hierarchical/time-varying models
- Methodological improvements
- Documentation and tutorials

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

This research was conducted independently. Special thanks to the open-source community for tools that made this work possible.

---

**Author**: Jean Clément Bogui  
**Contact**: jean.bogui@proton.me  
**ORCID**: [0009-0006-9896-5653](https://orcid.org/0009-0006-9896-5653)