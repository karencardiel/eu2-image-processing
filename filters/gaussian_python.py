import numpy as np

def gaussian_pure(image):
    rows, cols = image.shape
    result = np.zeros((rows, cols))

    kernel = [[1/16,2/16,1/16],
              [2/16,4/16,2/16],
              [1/16,2/16,1/16]]

    img_list = image.tolist()

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            val = 0
            for ki in range(3):
                for kj in range(3):
                    val += img_list[i+ki-1][j+kj-1] * kernel[ki][kj]

            result[i,j] = val

    return result.astype(np.uint8)