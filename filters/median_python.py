import numpy as np
import math

def median_pure(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols))
    img_list = image.tolist()
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            window = []
            for ki in range(-1, 2):
                for kj in range(-1, 2):
                    window.append(img_list[i+ki][j+kj])
            window.sort()
            result[i, j] = window[4]
    return result.astype(np.uint8)