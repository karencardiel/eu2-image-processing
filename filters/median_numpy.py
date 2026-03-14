import numpy as np

def median_numpy(image):
    rows, cols = image.shape
    stacked = np.zeros((9, rows-2, cols-2), dtype=image.dtype)
    curr = 0
    for i in range(3):
        for j in range(3):
            stacked[curr] = image[i:rows-2+i, j:cols-2+j]
            curr += 1
    median = np.median(stacked, axis=0)
    result = np.zeros_like(image)
    result[1:-1, 1:-1] = median
    return result