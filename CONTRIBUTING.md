# Contributing to Saviesa Framework

Thank you for your interest in contributing to the Saviesa Framework! This document provides guidelines for contributing to the project.

---

## 🤝 How to Contribute

### **1. Reporting Issues**

If you find a bug or have a suggestion:

1. Check if the issue already exists in [GitHub Issues](https://github.com/jcbogui/saviesa-framework/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Python version and dependencies

### **2. Proposing Changes**

For code contributions:

1. **Fork the repository**
   ```bash
   git clone https://github.com/jcbogui/saviesa-framework.git
   cd saviesa-framework
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation

4. **Test your changes**
   ```bash
   pytest tests/
   ```

5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: clear description"
   ```

6. **Push and create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

---

## 📋 Code Standards

### **Python Style**

- Follow [PEP 8](https://pep8.org/)
- Use type hints where appropriate
- Maximum line length: 88 characters (Black formatter)
- Docstrings: Google style

### **Example**

```python
def calculate_limiting_factor(O: float, L: float, M: float) -> str:
    """
    Identify the limiting factor among O, L, M.
    
    Args:
        O: Orientation score (normalized [0,1])
        L: Levier score (normalized [0,1])
        M: Milieu score (normalized [0,1])
    
    Returns:
        Name of limiting factor ('O', 'L', or 'M')
    
    Example:
        >>> calculate_limiting_factor(0.8, 0.5, 0.9)
        'L'
    """
    factors = {'O': O, 'L': L, 'M': M}
    return min(factors, key=factors.get)
```

---

## 🧪 Testing

All new features must include tests:

```python
# tests/test_models.py
def test_limiting_factor_identification():
    """Test limiting factor correctly identified"""
    assert calculate_limiting_factor(0.8, 0.5, 0.9) == 'L'
    assert calculate_limiting_factor(0.3, 0.7, 0.6) == 'O'
```

Run tests:
```bash
pytest tests/ -v --cov=scripts
```

---

## 📚 Documentation

Update documentation for:
- New functions/classes
- Changed behavior
- New examples

Documentation files:
- `docs/methodology.md`: Theoretical explanations
- `docs/api_reference.md`: Code documentation
- `docs/tutorials/`: Step-by-step guides

---

## 🔍 Review Process

Pull requests will be reviewed for:
1. **Correctness**: Does it work as intended?
2. **Tests**: Are there adequate tests?
3. **Documentation**: Is it well-documented?
4. **Style**: Does it follow project conventions?
5. **Impact**: Does it improve the framework?

---

## 📧 Questions?

Contact: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)

---

Thank you for contributing! 🎉
