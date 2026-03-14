import numpy as np

def gaussian_numpy(image):
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16.0
    rows, cols = image.shape
    res = np.zeros_like(image, dtype=float)
    for i in range(3):
        for j in range(3):
            res[1:-1, 1:-1] += image[i:rows-2+i, j:cols-2+j] * kernel[i, j]
    return res.astype(np.uint8)