#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <chrono>
#include "cpp_functions.h"

/**
 * Python bindings for C++ functions using pybind11.
 * This file creates the bridge between Python and C++ implementations.
 */

namespace py = pybind11;

PYBIND11_MODULE(cpp_accelerated, m) {
    m.doc() = "C++ accelerated functions for Python - Performance comparison module";
    
    // Basic functions that mirror Python implementation
    m.def("sum_of_squares", &cpp_functions::sum_of_squares, 
          "Calculate the sum of squares from 1 to n (C++ implementation)",
          py::arg("n"));
    
    m.def("fibonacci_recursive", &cpp_functions::fibonacci_recursive,
          "Calculate the nth Fibonacci number using recursive approach (C++ implementation)", 
          py::arg("n"));
    
    m.def("prime_count", &cpp_functions::prime_count,
          "Count the number of prime numbers up to the given limit (C++ implementation)",
          py::arg("limit"));
    
    m.def("matrix_multiplication", &cpp_functions::matrix_multiplication,
          "Perform matrix multiplication of two size x size matrices (C++ implementation)",
          py::arg("size"));
    
    // Optimized versions that leverage C++ capabilities
    m.def("sum_of_squares_optimized", &cpp_functions::sum_of_squares_optimized,
          "Calculate sum of squares using mathematical formula (C++ optimized)",
          py::arg("n"));
    
    m.def("prime_count_optimized", &cpp_functions::prime_count_optimized,
          "Count primes using Sieve of Eratosthenes (C++ optimized)",
          py::arg("limit"));
    
    m.def("fibonacci_memoized", &cpp_functions::fibonacci_memoized,
          "Calculate Fibonacci with memoization (C++ optimized)",
          py::arg("n"));
    
    // Wrapper functions for easier benchmarking
    m.def("benchmark_sum_of_squares", [](int n, int iterations) {
        auto start = std::chrono::high_resolution_clock::now();
        long long result = 0;
        for (int i = 0; i < iterations; ++i) {
            result = cpp_functions::sum_of_squares(n);
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        double avg_time = duration.count() / (1e9 * iterations);
        return py::make_tuple(result, avg_time);
    }, "Benchmark sum_of_squares function", py::arg("n"), py::arg("iterations") = 1);
    
    m.def("benchmark_prime_count", [](int limit, int iterations) {
        auto start = std::chrono::high_resolution_clock::now();
        int result = 0;
        for (int i = 0; i < iterations; ++i) {
            result = cpp_functions::prime_count(limit);
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        double avg_time = duration.count() / (1e9 * iterations);
        return py::make_tuple(result, avg_time);
    }, "Benchmark prime_count function", py::arg("limit"), py::arg("iterations") = 1);
    
    m.def("benchmark_fibonacci", [](int n, int iterations) {
        auto start = std::chrono::high_resolution_clock::now();
        long long result = 0;
        for (int i = 0; i < iterations; ++i) {
            result = cpp_functions::fibonacci_recursive(n);
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        double avg_time = duration.count() / (1e9 * iterations);
        return py::make_tuple(result, avg_time);
    }, "Benchmark fibonacci_recursive function", py::arg("n"), py::arg("iterations") = 1);
    
    m.def("benchmark_matrix_mult", [](int size, int iterations) {
        auto start = std::chrono::high_resolution_clock::now();
        std::vector<std::vector<int>> result;
        for (int i = 0; i < iterations; ++i) {
            result = cpp_functions::matrix_multiplication(size);
        }
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
        double avg_time = duration.count() / (1e9 * iterations);
        return py::make_tuple(result[0][0], avg_time); // Return first element as sample
    }, "Benchmark matrix_multiplication function", py::arg("size"), py::arg("iterations") = 1);
}