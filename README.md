<div align="center">

# 🧠 AI/ML Bootcamp Journey

### *A structured path through the fundamentals of Artificial Intelligence and Machine Learning*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![ML](https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

</div>

---

## 📖 About This Repository

This repository chronicles my systematic journey through AI/ML fundamentals, starting from the foundational libraries and progressing through core concepts. Each day builds upon the previous, creating a comprehensive learning path from basics to advanced topics.

> **Note**: This is an active learning repository, continuously updated as I progress through the bootcamp.

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────┐
│  Foundation → Core Libraries → Algorithms → Deep Learning │
└─────────────────────────────────────────────────────────┘
```

### Current Progress

```
Day 01 ██████████████████████  NumPy & Pandas Basics [In Progress]
Day 02 ░░░░░░░░░░░░░░░░░░░░  Coming Soon
Day 03 ░░░░░░░░░░░░░░░░░░░░  Coming Soon
```

---

## 📚 Course Content

### **Day 01** — NumPy Deep Dive

> *Understanding the backbone of numerical computing in Python*

The first day focuses on mastering NumPy, the fundamental package for scientific computing. Divided into progressive phases:

<table>
<tr>
<td width="50%">

**Phase 01** [`numpy-phase01.ipynb`](Day01/numpy-phase01.ipynb)
- Array creation and initialization
- Lists vs Arrays performance comparison
- Basic array operations
- Vector, Matrix, and Tensor concepts
- Array properties and reshaping

</td>
<td width="50%">

**Phase 02** [`numpy-phase02.ipynb`](Day01/numpy-phase02.ipynb)
- Advanced array manipulations
- Broadcasting mechanics
- Array slicing and indexing
- Stacking and splitting arrays

</td>
</tr>
<tr>
<td width="50%">

**Phase 03** [`numpy-phase03.ipynb`](Day01/numpy-phase03.ipynb)
- Mathematical operations
- Statistical functions
- Linear algebra operations
- Random number generation

</td>
<td width="50%">

**Phase 04** [`numpy-phase04.ipynb`](Day01/numpy-phase04.ipynb)
- Advanced NumPy techniques
- Performance optimization
- Real-world applications
- Best practices

</td>
</tr>
</table>

#### 🎯 Key Takeaways from Day 01 - NumPy

- **Speed Matters**: NumPy arrays are ~23x faster than Python lists for numerical operations
- **Memory Efficiency**: Fixed-type arrays use significantly less memory than dynamic Python lists
- **Broadcasting**: Powerful mechanism for performing operations on arrays of different shapes
- **Vectorization**: Write cleaner, more efficient code without explicit loops

### **Day 01** — Pandas Introduction

> *Getting started with data manipulation and analysis*

Building on NumPy fundamentals, this notebook introduces Pandas for working with structured data:

**Pandas Basics** [`pandas.ipynb`](Day01/pandas.ipynb)
- Reading CSV files with `pd.read_csv()`
- Data exploration methods (head, tail, info, describe)
- Column and row selection
- Index-based access (loc, iloc)
- Filtering data with boolean conditions
- Working with multiple conditions using logical operators

#### 🎯 Key Concepts Covered

- **DataFrames**: Two-dimensional labeled data structures
- **Data Selection**: Multiple methods for accessing specific data
- **Filtering**: Using boolean indexing for data subsetting
- **Conditional Logic**: Combining multiple conditions with `&` and `|` operators

---

## 🛠️ Technical Stack

| Category | Tools & Libraries |
|----------|-------------------|
| **Language** | Python 3.x |
| **Core Libraries** | NumPy, Pandas, Matplotlib, Seaborn |
| **ML Frameworks** | Scikit-learn, TensorFlow, PyTorch *(upcoming)* |
| **Environment** | Jupyter Notebook, Google Colab |
| **Version Control** | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

```bash
python >= 3.8
jupyter notebook
```

### Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/yourusername/aimlBootCamp.git
cd aimlBootCamp

# Install required packages
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

### Running the Notebooks

```bash
# Launch Jupyter Notebook
jupyter notebook

# Navigate to the desired day and phase
# Example: Day01/numpy-phase01.ipynb
```

---

## 📊 Project Structure

```
aimlBootCamp/
│
├── Day01/                          # NumPy & Pandas Fundamentals
│   ├── numpy-phase01.ipynb        # Introduction & Basics
│   ├── numpy-phase02.ipynb        # Intermediate Operations
│   ├── numpy-phase03.ipynb        # Advanced Techniques
│   ├── numpy-phase04.ipynb        # Optimization & Best Practices
│   ├── pandas.ipynb               # Pandas Introduction & Basics
│   └── numpy-logo.npy             # NumPy logo data
│
├── Day02/                          # Coming Soon
├── Day03/                          # Coming Soon
└── README.md                       # You are here
```

---

## 💡 Learning Resources

Key resources that complement this bootcamp:

- [NumPy Official Documentation](https://numpy.org/doc/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Machine Learning Coursera](https://www.coursera.org/learn/machine-learning)
- [Deep Learning Specialization](https://www.deeplearning.ai/)

---

## 📝 Notes & Best Practices

### Code Quality Standards

- ✅ Clear variable naming following Python conventions
- ✅ Comprehensive comments explaining complex operations
- ✅ Performance comparisons where applicable
- ✅ Practical examples demonstrating real-world usage
- ✅ Progressive difficulty throughout each phase

### Notebook Organization

Each notebook follows a consistent structure:
1. **Introduction** — Concept overview
2. **Theory** — Mathematical/conceptual foundation
3. **Implementation** — Hands-on code examples
4. **Practice** — Exercises and challenges
5. **Summary** — Key takeaways and next steps

---

## 🎯 Upcoming Topics

<details>
<summary><b>Expand to see the roadmap</b></summary>

- [ ] **Day 02**: Pandas for Data Manipulation
- [ ] **Day 03**: Data Visualization with Matplotlib & Seaborn
- [ ] **Day 04**: Statistical Analysis Fundamentals
- [ ] **Day 05**: Introduction to Machine Learning
- [ ] **Day 06**: Linear Regression & Gradient Descent
- [ ] **Day 07**: Classification Algorithms
- [ ] **Day 08**: Decision Trees & Random Forests
- [ ] **Day 09**: Support Vector Machines
- [ ] **Day 10**: Neural Networks Basics
- [ ] **Day 11**: Deep Learning with TensorFlow/PyTorch
- [ ] **Day 12**: Convolutional Neural Networks (CNNs)
- [ ] **Day 13**: Recurrent Neural Networks (RNNs)
- [ ] **Day 14**: Natural Language Processing
- [ ] **Day 15**: Final Project & Deployment

</details>

---

## 🤝 Contributing

While this is primarily a personal learning repository, suggestions and corrections are welcome! Feel free to:

- Open an issue for errors or improvements
- Suggest additional resources
- Share alternative approaches to problems

---

## 📄 License

This project is open source and available for educational purposes. Feel free to fork and adapt for your own learning journey.

---

<div align="center">

### ⭐ If you find this helpful, consider starring the repo!

**Happy Learning!** 🚀

*Last Updated: November 2025*

---

**[⬆ Back to Top](#-aiml-bootcamp-journey)**

</div>
