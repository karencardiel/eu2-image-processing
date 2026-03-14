import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import os

# --- IMPORTAR FILTROS ---
from filters.gaussian_python import gaussian_pure
from filters.gaussian_numpy import gaussian_numpy
from cython_filters.filters_cython import gaussian_cython

from filters.sobel_python import sobel_pure
from filters.sobel_numpy import sobel_numpy_full
from cython_filters.filters_cython import sobel_cython_full

from filters.median_python import median_pure
from filters.median_numpy import median_numpy
from cython_filters.filters_cython import median_cython_full

# --- CARGAR IMAGEN ---
img_original = cv2.imread("mono.jpeg", cv2.IMREAD_GRAYSCALE)
img_original = cv2.resize(img_original, (256, 256))


# --- FUNCIÓN DE BENCHMARK ---
def run_benchmark(img):

    filters = {
        "Gaussian": [gaussian_pure, gaussian_numpy, gaussian_cython],
        "Sobel": [sobel_pure, sobel_numpy_full, sobel_cython_full],
        "Median": [median_pure, median_numpy, median_cython_full]
    }

    results_table = []
    final_images = {}

    print(f"{'Filter':<12} | {'Python (s)':<12} | {'NumPy (s)':<12} | {'Cython (s)':<12}")
    print("-" * 55)

    for name, funcs in filters.items():

        times = []

        for f in funcs:

            start = time.time()
            result = f(img)
            elapsed = time.time() - start

            times.append(elapsed)

            # Guardar imagen final (la de Cython)
            if f.__name__.endswith("cython_full") or f.__name__ == "gaussian_cython":
                final_images[name] = result

        results_table.append([name] + times)

        print(f"{name:<12} | {times[0]:<12.4f} | {times[1]:<12.4f} | {times[2]:<12.4f}")

    return results_table, final_images


# --- FUNCIÓN PARA GRAFICAR RESULTADOS ---
def plot_comparison(results):

    methods = [
        "Gaussian\nPure Python", "Gaussian\nNumPy", "Gaussian\nCython",
        "Sobel\nPure Python", "Sobel\nNumPy", "Sobel\nCython",
        "Median\nPure Python", "Median\nNumPy", "Median\nCython"
    ]

    times = []

    for row in results:
        times.extend(row[1:])

    plt.figure(figsize=(14, 7))

    colors = ['#B24968', '#6C5FA7', '#FA8572'] * 3
    bars = plt.bar(methods, times, color=colors)

    plt.title("Performance Comparison of Image Filters")
    plt.ylabel("Execution time (seconds)")
    plt.xlabel("Implementation method")
    plt.xticks(rotation=45)

    # escala log porque Python vs Cython suele ser MUY diferente
    plt.yscale('log')

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            yval,
            f'{yval:.4f}s',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()

    # crear carpeta si no existe
    os.makedirs("results", exist_ok=True)

    # guardar gráfica
    plt.savefig("results/performance_plot.png", dpi=300)

    plt.show()


# --- VISUALIZAR RESULTADOS DE FILTROS ---
def show_images(original, filtered):

    plt.figure(figsize=(15,5))

    plt.subplot(1,4,1)
    plt.imshow(original, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,4,2)
    plt.imshow(filtered["Gaussian"], cmap="gray")
    plt.title("Gaussian (Blur)")
    plt.axis("off")

    plt.subplot(1,4,3)
    plt.imshow(filtered["Sobel"], cmap="gray")
    plt.title("Sobel (Edges)")
    plt.axis("off")

    plt.subplot(1,4,4)
    plt.imshow(filtered["Median"], cmap="gray")
    plt.title("Median (Noise reduction)")
    plt.axis("off")

    os.makedirs("results", exist_ok=True) 
    plt.savefig("results/filters_comparison.png", dpi=300) 

    plt.show()


# --- MAIN ---
results, final_images = run_benchmark(img_original)

plot_comparison(results)

show_images(img_original, final_images)