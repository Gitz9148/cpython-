"""
Setup script for building the C++ accelerated Python extension.
This script uses pybind11 to create a Python module from C++ code.
"""

from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "cpp_accelerated",  # Module name
        sources=[
            "pybind_wrapper.cpp",
            "cpp_functions.cpp",
        ],
        include_dirs=[
            # Path to pybind11 headers
            pybind11.get_include(),
        ],
        language='c++',
        cxx_std=14,  # C++14 standard
        # Force correct architecture
        define_macros=[('VERSION_INFO', '"dev"')],
        extra_compile_args=["-arch", "arm64"],
        extra_link_args=["-arch", "arm64"],
    ),
]

setup(
    name="cpp_accelerated",
    version="1.0.0",
    author="Python C++ Performance Comparison",
    author_email="",
    description="C++ accelerated functions for Python performance comparison",
    long_description="""
    This package provides C++ implementations of computationally intensive functions
    that can be called from Python for significant performance improvements.
    
    Features:
    - Sum of squares calculation
    - Fibonacci sequence generation
    - Prime number counting
    - Matrix multiplication
    - Optimized versions using advanced algorithms
    
    The package demonstrates the performance difference between pure Python
    implementations and C++ accelerated versions of the same algorithms.
    """,
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "pybind11>=2.6.0",
        "numpy>=1.18.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: C++",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Hardware",
    ],
)