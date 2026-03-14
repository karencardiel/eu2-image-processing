import numpy as np
cimport numpy as cnp
cimport cython
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
def gaussian_cython(unsigned char[:, :] image):

    cdef int rows = image.shape[0]
    cdef int cols = image.shape[1]

    cdef cnp.ndarray[cnp.float64_t, ndim=2] result = np.zeros((rows, cols), dtype=np.float64)

    cdef double[:, :] kernel = np.array([
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ], dtype=np.float64)

    cdef int i, j, ki, kj
    cdef double val

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            val = 0

            for ki in range(3):
                for kj in range(3):

                    val += image[i + ki - 1, j + kj - 1] * kernel[ki, kj]

            result[i, j] = val

    return result.astype(np.uint8)


@cython.boundscheck(False)
@cython.wraparound(False)
def sobel_cython_full(unsigned char[:, :] image):

    cdef int rows = image.shape[0]
    cdef int cols = image.shape[1]

    cdef cnp.ndarray[cnp.uint8_t, ndim=2] result = np.zeros((rows, cols), dtype=np.uint8)

    cdef double gx, gy, mag
    cdef int i, j

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            gx = (-1*image[i-1,j-1]) + (1*image[i-1,j+1]) \
               + (-2*image[i,j-1]) + (2*image[i,j+1]) \
               + (-1*image[i+1,j-1]) + (1*image[i+1,j+1])

            gy = (-1*image[i-1,j-1]) + (-2*image[i-1,j]) + (-1*image[i-1,j+1]) \
               + (1*image[i+1,j-1]) + (2*image[i+1,j]) + (1*image[i+1,j+1])

            mag = sqrt(gx*gx + gy*gy)

            result[i, j] = <unsigned char>(mag if mag < 255 else 255)

    return result


@cython.boundscheck(False)
@cython.wraparound(False)
def median_cython_full(unsigned char[:, :] image):

    cdef int rows = image.shape[0]
    cdef int cols = image.shape[1]

    cdef cnp.ndarray[cnp.uint8_t, ndim=2] result = np.zeros((rows, cols), dtype=np.uint8)

    cdef int i, j, ki, kj, index
    cdef int[9] window

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            index = 0

            for ki in range(3):
                for kj in range(3):

                    window[index] = image[i + ki - 1, j + kj - 1]
                    index += 1

            for ki in range(9):
                for kj in range(ki + 1, 9):

                    if window[ki] > window[kj]:
                        window[ki], window[kj] = window[kj], window[ki]

            result[i, j] = window[4]

    return result