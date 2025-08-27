#ifndef CPP_FUNCTIONS_H
#define CPP_FUNCTIONS_H

#include <vector>

/**
 * Header file for C++ implementation of computationally intensive functions.
 * These functions provide high-performance alternatives to Python implementations.
 */

namespace cpp_functions {

/**
 * Calculate the sum of squares from 1 to n.
 */
long long sum_of_squares(int n);

/**
 * Calculate the nth Fibonacci number using recursive approach.
 */
long long fibonacci_recursive(int n);

/**
 * Count the number of prime numbers up to the given limit.
 */
int prime_count(int limit);

/**
 * Perform matrix multiplication of two size x size matrices.
 */
std::vector<std::vector<int>> matrix_multiplication(int size);

/**
 * Optimized sum of squares using mathematical formula.
 */
long long sum_of_squares_optimized(int n);

/**
 * Optimized prime counting using sieve of Eratosthenes.
 */
int prime_count_optimized(int limit);

/**
 * Fibonacci with memoization for better performance.
 */
long long fibonacci_memoized(int n);

} // namespace cpp_functions

#endif // CPP_FUNCTIONS_H