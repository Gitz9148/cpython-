#!/usr/bin/env python3
"""
Basic Usage Examples for Python + C++ Performance Wrapper

This script demonstrates the basic usage of both Python and C++ implementations
with simple, easy-to-understand examples.
"""

import time
import sys
import os

# Add the parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import python_implementation

try:
    import cpp_accelerated
    CPP_AVAILABLE = True
    print("✓ C++ accelerated module loaded successfully!")
except ImportError:
    CPP_AVAILABLE = False
    print("✗ C++ module not available. Please build it first:")
    print("  python setup.py build_ext --inplace")


def compare_performance(name, python_func, cpp_func, *args):
    """Compare performance between Python and C++ implementations."""
    print(f"\n{name}")
    print("-" * len(name))
    
    # Python version
    start = time.perf_counter()
    py_result = python_func(*args)
    py_time = time.perf_counter() - start
    print(f"Python: {py_result} (took {py_time:.6f}s)")
    
    if CPP_AVAILABLE and cpp_func:
        # C++ version
        start = time.perf_counter()
        cpp_result = cpp_func(*args)
        cpp_time = time.perf_counter() - start
        print(f"C++:    {cpp_result} (took {cpp_time:.6f}s)")
        
        # Calculate speedup
        if py_time > 0:
            speedup = py_time / cpp_time
            print(f"Speedup: {speedup:.1f}x faster with C++")
        
        # Verify results match
        if py_result == cpp_result:
            print("✓ Results match!")
        else:
            print("✗ Results differ!")
    else:
        print("C++ comparison not available")


def basic_examples():
    """Run basic examples with small, manageable numbers."""
    print("Basic Usage Examples")
    print("=" * 50)
    
    # Example 1: Small sum of squares
    compare_performance(
        "Sum of squares (1 to 1000)",
        python_implementation.sum_of_squares,
        cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None,
        1000
    )
    
    # Example 2: Small Fibonacci
    compare_performance(
        "Fibonacci number #30",
        python_implementation.fibonacci_recursive,
        cpp_accelerated.fibonacci_recursive if CPP_AVAILABLE else None,
        30
    )
    
    # Example 3: Prime counting
    compare_performance(
        "Prime count up to 1000",
        python_implementation.prime_count,
        cpp_accelerated.prime_count if CPP_AVAILABLE else None,
        1000
    )
    
    # Example 4: Small matrix multiplication
    compare_performance(
        "Matrix multiplication (50x50)",
        python_implementation.matrix_multiplication,
        cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None,
        50
    )


def optimized_examples():
    """Demonstrate C++ optimized algorithms."""
    if not CPP_AVAILABLE:
        print("\nOptimized examples require C++ module to be built.")
        return
    
    print("\n" + "=" * 50)
    print("Optimized Algorithm Examples")
    print("=" * 50)
    
    # Optimized sum of squares
    print("\nSum of Squares Optimization")
    print("-" * 30)
    
    n = 100000
    
    # Standard implementation
    start = time.perf_counter()
    std_result = cpp_accelerated.sum_of_squares(n)
    std_time = time.perf_counter() - start
    print(f"Standard C++: {std_result} (took {std_time:.6f}s)")
    
    # Mathematical formula optimization
    start = time.perf_counter()
    opt_result = cpp_accelerated.sum_of_squares_optimized(n)
    opt_time = time.perf_counter() - start
    print(f"Optimized:    {opt_result} (took {opt_time:.6f}s)")
    
    if std_time > 0:
        speedup = std_time / opt_time
        print(f"Optimization speedup: {speedup:.1f}x")
    
    # Prime counting optimization
    print("\nPrime Counting Optimization")
    print("-" * 31)
    
    limit = 50000
    
    # Trial division
    start = time.perf_counter()
    trial_result = cpp_accelerated.prime_count(limit)
    trial_time = time.perf_counter() - start
    print(f"Trial division: {trial_result} primes (took {trial_time:.6f}s)")
    
    # Sieve of Eratosthenes
    start = time.perf_counter()
    sieve_result = cpp_accelerated.prime_count_optimized(limit)
    sieve_time = time.perf_counter() - start
    print(f"Sieve method:   {sieve_result} primes (took {sieve_time:.6f}s)")
    
    if trial_time > 0:
        speedup = trial_time / sieve_time
        print(f"Algorithm speedup: {speedup:.1f}x")
    
    # Fibonacci memoization
    print("\nFibonacci Memoization")
    print("-" * 21)
    
    n = 40
    
    # Recursive
    start = time.perf_counter()
    rec_result = cpp_accelerated.fibonacci_recursive(n)
    rec_time = time.perf_counter() - start
    print(f"Recursive: {rec_result} (took {rec_time:.6f}s)")
    
    # Memoized
    start = time.perf_counter()
    memo_result = cpp_accelerated.fibonacci_memoized(n)
    memo_time = time.perf_counter() - start
    print(f"Memoized:  {memo_result} (took {memo_time:.6f}s)")
    
    if rec_time > 0:
        speedup = rec_time / memo_time
        print(f"Memoization speedup: {speedup:.1f}x")


def custom_benchmark_example():
    """Show how to create custom benchmarks."""
    print("\n" + "=" * 50)
    print("Custom Benchmark Example")
    print("=" * 50)
    
    def custom_benchmark(func, *args, iterations=5):
        """Custom benchmark function."""
        times = []
        result = None
        
        for i in range(iterations):
            start = time.perf_counter()
            result = func(*args)
            end = time.perf_counter()
            times.append(end - start)
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        return result, avg_time, min_time, max_time
    
    print("\nCustom benchmark: Sum of squares (n=50000, 5 iterations)")
    
    # Python benchmark
    py_result, py_avg, py_min, py_max = custom_benchmark(
        python_implementation.sum_of_squares, 50000
    )
    print(f"Python: avg={py_avg:.6f}s, min={py_min:.6f}s, max={py_max:.6f}s")
    
    if CPP_AVAILABLE:
        # C++ benchmark
        cpp_result, cpp_avg, cpp_min, cpp_max = custom_benchmark(
            cpp_accelerated.sum_of_squares, 50000
        )
        print(f"C++:    avg={cpp_avg:.6f}s, min={cpp_min:.6f}s, max={cpp_max:.6f}s")
        
        speedup = py_avg / cpp_avg
        print(f"Average speedup: {speedup:.1f}x")


if __name__ == "__main__":
    print("Python + C++ Performance Wrapper - Usage Examples")
    print("=" * 60)
    
    # Run all examples
    basic_examples()
    optimized_examples()
    custom_benchmark_example()
    
    print("\n" + "=" * 60)
    print("Examples complete!")
    
    if not CPP_AVAILABLE:
        print("\nTo see C++ performance improvements:")
        print("1. Build the extension: python setup.py build_ext --inplace")
        print("2. Re-run this script: python examples/basic_usage.py")