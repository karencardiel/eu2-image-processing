# Image Processing Filters Benchmark (Python vs NumPy vs Cython)

## Overview

This project compares the performance of three different implementations of common image processing filters. As a **Data Engineering** exercise, the goal is to evaluate how low-level optimizations and vectorization affect execution time when processing image data.

The filters implemented are:

* **Gaussian Filter:** Image smoothing and noise reduction.
* **Sobel Filter:** Edge detection via gradient magnitude.
* **Median Filter:** Non-linear noise reduction (Salt & Pepper).

---

## Project Structure

```text
image-processing/
├── benchmark.py            # Main execution script
├── mono.jpeg               # Sample input image
├── filters/                # Pure Python & NumPy implementations
│   ├── gaussian_python.py
│   ├── gaussian_numpy.py
│   ├── sobel_python.py
│   ├── sobel_numpy.py
│   ├── median_python.py
│   └── median_numpy.py
├── cython_filters/         # Cython optimized implementations
│   ├── filters_cython.pyx  # Cython source code
│   ├── setup.py            # Compilation script
│   └── __init__.py
├── results/                # Generated outputs
│   ├── performance_plot.png
│   └── filters_comparison.png
└── requirements.txt        # Project dependencies

```

---

## 🛠️ Setup Instructions

Follow these steps to set up the project environment on your local machine:

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd image-processing

```

### 2. Create a Virtual Environment (Recommended)

This keeps the project dependencies isolated from your global Python installation.

```bash
# Create the environment
python3 -m venv venv

# Activate it
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## ⚙️ Cython Compilation

Before running the benchmark, you must compile the Cython module into a shared object (`.so`) file. **Run this command from the project root:**

```bash
python3 cython_filters/setup.py build_ext --inplace

```

This will create the compiled extension inside the `cython_filters/` directory, allowing `benchmark.py` to import it correctly.

---

## 🚀 Running the Benchmark

Once compiled, execute the main script:

```bash
python3 benchmark.py

```

The script performs the following steps:

1. Loads `mono.jpeg` in grayscale.
2. Runs each filter (Gaussian, Sobel, Median) using all three implementations.
3. Profiles the execution time for each.
4. Generates a comparison bar chart and a visual gallery of the results.

---

## 📊 Results & Analysis

The performance data is stored in the `results/` folder:

* **`performance_plot.png`**: A bar chart comparing execution times. Since Pure Python is often $100\times$ to $1000\times$ slower than Cython, the y-axis uses a **logarithmic scale** for better visibility.
* **`filters_comparison.png`**: A side-by-side visual comparison of the original image versus the processed outputs.

### Expected Performance Trend:

1. **Pure Python:** Slowest due to nested loops and interpreted overhead.
2. **NumPy:** Significant speedup via vectorization (C-internal loops).
3. **Cython:** Fastest performance, approaching raw C speeds by using static typing and bypassing the Python GIL where possible.

---

## Conclusion

This benchmark highlights the importance of choosing the right tool for heavy data processing. While Pure Python is readable and easy to write, libraries like **NumPy** and **Cython** are essential for production-grade image processing and data engineering pipelines.

---