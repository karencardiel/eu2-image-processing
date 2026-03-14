from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import os

extensions = [
    Extension(
        "cython_filters.filters_cython", 
        ["cython_filters/filters_cython.pyx"], 
        include_dirs=[np.get_include()]
    )
]

setup(
    ext_modules=cythonize(extensions, annotate=True) 
)