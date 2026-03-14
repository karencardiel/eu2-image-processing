
import numpy as np

def sobel_numpy_full(image):
    img = image.astype(float)
    rows, cols = img.shape
    gx = np.zeros_like(img)
    gy = np.zeros_like(img)
    # Kernels aplicados con slices de NumPy
    gx[1:-1, 1:-1] = -1*img[:-2, :-2] + 1*img[:-2, 2:] - 2*img[1:-1, :-2] + 2*img[1:-1, 2:] - 1*img[2:, :-2] + 1*img[2:, 2:]
    gy[1:-1, 1:-1] = -1*img[:-2, :-2] - 2*img[:-2, 1:-1] - 1*img[:-2, 2:] + 1*img[2:, :-2] + 2*img[2:, 1:-1] + 1*img[2:, 2:]
    mag = np.sqrt(gx**2 + gy**2)
    return np.clip(mag, 0, 255).astype(np.uint8)