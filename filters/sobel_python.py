import numpy as np
import math

def sobel_pure(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols))
    img_list = image.tolist()
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            gx = (-1*img_list[i-1][j-1]) + (1*img_list[i-1][j+1]) + (-2*img_list[i][j-1]) + (2*img_list[i][j+1]) + (-1*img_list[i+1][j-1]) + (1*img_list[i+1][j+1])
            gy = (-1*img_list[i-1][j-1]) + (-2*img_list[i-1][j]) + (-1*img_list[i-1][j+1]) + (1*img_list[i+1][j-1]) + (2*img_list[i+1][j]) + (1*img_list[i+1][j+1])
            mag = math.sqrt(gx**2 + gy**2)
            result[i, j] = min(255, mag)
    return result.astype(np.uint8)