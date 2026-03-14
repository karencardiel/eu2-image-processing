# <img src="https://slackmojis.com/emojis/78198-monkeyplsq/download" width="45"> Image Processing (Python, NumPy and Cython)

This activity compares the performance of three different implementations of common image processing filters. The goal is to evaluate how low-level optimizations and vectorization affect execution time when processing image data.

The filters implemented are:

* **Gaussian Filter:** Image smoothing and noise reduction.
* **Sobel Filter:** Edge detection via gradient magnitude.
* **Median Filter:** Non-linear noise reduction (Salt and Pepper).


## 🍌 Project Structure

```text
image-processing/
├── benchmark.py            # Main execution script
├── mono.jpeg               # Sample input image
├── filters/                # Pure Python and NumPy implementations
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
└── requirements.txt        # Project dependencies
```

## 🍌 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/karencardiel/eu2-image-processing.git
cd image-processing
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🍌 Cython Compilation

Before running the benchmark, compile the Cython module into a shared object (`.so`) file. **Run from the project root:**

```bash
python3 cython_filters/setup.py build_ext --inplace
```


## 🍌 Running the Benchmark

```bash
python3 benchmark.py
```

The script performs the following steps:

1. Loads `mono.jpeg` in grayscale.
2. Runs each filter (Gaussian, Sobel, Median) using all three implementations.
3. Profiles the execution time for each.
4. Generates a comparison bar chart and a visual gallery of the results.
