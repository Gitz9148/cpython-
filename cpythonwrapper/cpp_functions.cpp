#include <vector>
#include <cmath>

/**
 * C++ implementation of computationally intensive functions.
 * These functions mirror the Python implementation but are optimized for speed.
 */

namespace cpp_functions {

/**
 * Calculate the sum of squares from 1 to n.
 * C++ version with optimized integer operations.
 */
long long sum_of_squares(int n) {
    long long total = 0;
    for (int i = 1; i <= n; ++i) {
        total += static_cast<long long>(i) * i;
    }
    return total;
}

/**
 * Calculate the nth Fibonacci number using recursive approach.
 * C++ version with optimized function calls.
 */
long long fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

/**
 * Count the number of prime numbers up to the given limit.
 * C++ version with optimized trial division.
 */
int prime_count(int limit) {
    if (limit < 2) {
        return 0;
    }
    
    int count = 0;
    for (int num = 2; num <= limit; ++num) {
        bool is_prime = true;
        int sqrt_num = static_cast<int>(std::sqrt(num));
        
        for (int i = 2; i <= sqrt_num; ++i) {
            if (num % i == 0) {
                is_prime = false;
                break;
            }
        }
        
        if (is_prime) {
            ++count;
        }
    }
    
    return count;
}

/**
 * Perform matrix multiplication of two size x size matrices.
 * C++ version with optimized memory access patterns.
 */
std::vector<std::vector<int>> matrix_multiplication(int size) {
    // Create two matrices with simple values
    std::vector<std::vector<int>> matrix_a(size, std::vector<int>(size));
    std::vector<std::vector<int>> matrix_b(size, std::vector<int>(size));
    
    // Initialize matrices
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            matrix_a[i][j] = i + j;
            matrix_b[i][j] = i * j + 1;
        }
    }
    
    // Initialize result matrix
    std::vector<std::vector<int>> result(size, std::vector<int>(size, 0));
    
    // Perform matrix multiplication with cache-friendly access pattern
    for (int i = 0; i < size; ++i) {
        for (int k = 0; k < size; ++k) {
            for (int j = 0; j < size; ++j) {
                result[i][j] += matrix_a[i][k] * matrix_b[k][j];
            }
        }
    }
    
    return result;
}

/**
 * Alternative optimized sum of squares using mathematical formula.
 * This demonstrates how C++ can leverage mathematical optimizations.
 */
long long sum_of_squares_optimized(int n) {
    // Using the mathematical formula: sum of squares = n(n+1)(2n+1)/6
    long long ln = static_cast<long long>(n);
    return (ln * (ln + 1) * (2 * ln + 1)) / 6;
}

/**
 * Optimized prime counting using sieve of Eratosthenes.
 * This demonstrates algorithmic optimization possible in C++.
 */
int prime_count_optimized(int limit) {
    if (limit < 2) {
        return 0;
    }
    
    std::vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;
    
    for (int i = 2; i * i <= limit; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }
    
    int count = 0;
    for (int i = 2; i <= limit; ++i) {
        if (is_prime[i]) {
            ++count;
        }
    }
    
    return count;
}

/**
 * Fibonacci with memoization for better performance.
 * Demonstrates how C++ can implement efficient caching.
 */
long long fibonacci_memoized(int n) {
    static std::vector<long long> memo;
    
    if (memo.size() <= static_cast<size_t>(n)) {
        memo.resize(n + 1, -1);
    }
    
    if (n <= 1) {
        return n;
    }
    
    if (memo[n] != -1) {
        return memo[n];
    }
    
    memo[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2);
    return memo[n];
}

} // namespace cpp_functions