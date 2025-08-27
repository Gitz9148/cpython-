#!/usr/bin/env python3
"""
Performance Benchmark Script
============================

This script compares the performance between pure Python implementations
and C++ accelerated versions of the same algorithms.

Usage:
    python performance_benchmark.py

Requirements:
    - Built C++ extension module (cpp_accelerated)
    - Python modules: time, sys, importlib
"""

import sys
import time
import importlib.util
from typing import Tuple, Any, Callable

# Import pure Python implementations
import python_implementation

# Try to import C++ accelerated module
try:
    import cpp_accelerated
    CPP_AVAILABLE = True
    print("✓ C++ accelerated module loaded successfully!")
except ImportError as e:
    CPP_AVAILABLE = False
    print(f"✗ C++ accelerated module not available: {e}")
    print("Please build the C++ extension first using: python setup.py build_ext --inplace")


def benchmark_function(func: Callable, *args, iterations: int = 1, name: str = "") -> Tuple[Any, float]:
    """
    Benchmark a function by running it multiple times and measuring execution time.
    
    Args:
        func: Function to benchmark
        *args: Arguments to pass to the function
        iterations: Number of times to run the function
        name: Name for display purposes
        
    Returns:
        tuple: (result, average_time_seconds)
    """
    print(f"  Running {name}..." if name else "  Running...", end=" ", flush=True)
    
    start_time = time.perf_counter()
    result = None
    
    for _ in range(iterations):
        result = func(*args)
    
    end_time = time.perf_counter()
    average_time = (end_time - start_time) / iterations
    
    print(f"Done ({average_time:.6f}s)")
    return result, average_time


def compare_implementations(test_name: str, python_func: Callable, cpp_func: Callable, 
                          args: tuple, iterations: int = 1) -> None:
    """
    Compare Python and C++ implementations of the same function.
    
    Args:
        test_name: Name of the test for display
        python_func: Python function to test
        cpp_func: C++ function to test (or None if not available)
        args: Arguments to pass to both functions
        iterations: Number of iterations for benchmarking
    """
    print(f"\n{test_name}")
    print("=" * len(test_name))
    
    # Benchmark Python implementation
    print("Python Implementation:")
    py_result, py_time = benchmark_function(python_func, *args, iterations=iterations, name="Python")
    
    if CPP_AVAILABLE and cpp_func is not None:
        # Benchmark C++ implementation
        print("C++ Implementation:")
        cpp_result, cpp_time = benchmark_function(cpp_func, *args, iterations=iterations, name="C++")
        
        # Verify results match
        if py_result == cpp_result:
            print("✓ Results match!")
        else:
            print(f"✗ Results differ! Python: {py_result}, C++: {cpp_result}")
        
        # Calculate speedup
        if py_time > 0:
            speedup = py_time / cpp_time
            print(f"\nPerformance Summary:")
            print(f"  Python time:  {py_time:.6f} seconds")
            print(f"  C++ time:     {cpp_time:.6f} seconds")
            print(f"  Speedup:      {speedup:.2f}x faster with C++")
            
            if speedup > 1:
                improvement = ((speedup - 1) * 100)
                print(f"  Improvement:  {improvement:.1f}% faster")
            else:
                slower = ((1 / speedup - 1) * 100)
                print(f"  Performance:  {slower:.1f}% slower (overhead)")
        else:
            print("Could not calculate speedup (division by zero)")
    else:
        print("C++ implementation not available for comparison")
        print(f"\nPython time: {py_time:.6f} seconds")


def run_all_benchmarks():
    """Run all performance benchmarks comparing Python and C++ implementations."""
    
    print("Python vs C++ Performance Comparison")
    print("=" * 50)
    print("Running comprehensive performance benchmarks...")
    
    if not CPP_AVAILABLE:
        print("\nWARNING: C++ module not available. Only Python benchmarks will run.")
        print("To build C++ extension: python setup.py build_ext --inplace\n")
    
    # Test 1: Sum of Squares
    compare_implementations(
        "1. Sum of Squares (n=100,000)",
        python_implementation.sum_of_squares,
        cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None,
        (100000,),
        iterations=5
    )
    
    # Test 2: Fibonacci (smaller number due to exponential complexity)
    compare_implementations(
        "2. Fibonacci Recursive (n=35)",
        python_implementation.fibonacci_recursive,
        cpp_accelerated.fibonacci_recursive if CPP_AVAILABLE else None,
        (35,),
        iterations=1
    )
    
    # Test 3: Prime Counting
    compare_implementations(
        "3. Prime Count (limit=10,000)",
        python_implementation.prime_count,
        cpp_accelerated.prime_count if CPP_AVAILABLE else None,
        (10000,),
        iterations=3
    )
    
    # Test 4: Matrix Multiplication
    compare_implementations(
        "4. Matrix Multiplication (100x100)",
        python_implementation.matrix_multiplication,
        cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None,
        (100,),
        iterations=3
    )
    
    # Additional tests with optimized C++ versions if available
    if CPP_AVAILABLE:
        print("\n" + "=" * 50)
        print("BONUS: Optimized C++ Algorithm Comparisons")
        print("=" * 50)
        
        # Optimized Sum of Squares comparison
        print("\n5. Optimized Sum of Squares (n=1,000,000)")
        print("=" * 40)
        
        print("Standard C++ Implementation:")
        std_result, std_time = benchmark_function(
            cpp_accelerated.sum_of_squares, 1000000, iterations=10, name="Standard C++"
        )
        
        print("Mathematical Formula C++ Implementation:")
        opt_result, opt_time = benchmark_function(
            cpp_accelerated.sum_of_squares_optimized, 1000000, iterations=10, name="Optimized C++"
        )
        
        if std_result == opt_result:
            print("✓ Results match!")
            if std_time > 0:
                speedup = std_time / opt_time
                print(f"\nOptimization Impact:")
                print(f"  Standard time:   {std_time:.6f} seconds")
                print(f"  Optimized time:  {opt_time:.6f} seconds")
                print(f"  Speedup:         {speedup:.2f}x faster with optimization")
        
        # Optimized Prime Counting comparison  
        print("\n6. Optimized Prime Count (limit=100,000)")
        print("=" * 42)
        
        print("Trial Division C++ Implementation:")
        trial_result, trial_time = benchmark_function(
            cpp_accelerated.prime_count, 100000, iterations=3, name="Trial Division"
        )
        
        print("Sieve of Eratosthenes C++ Implementation:")
        sieve_result, sieve_time = benchmark_function(
            cpp_accelerated.prime_count_optimized, 100000, iterations=3, name="Sieve Algorithm"
        )
        
        if trial_result == sieve_result:
            print("✓ Results match!")
            if trial_time > 0:
                speedup = trial_time / sieve_time
                print(f"\nAlgorithmic Improvement:")
                print(f"  Trial division:  {trial_time:.6f} seconds")
                print(f"  Sieve method:    {sieve_time:.6f} seconds")
                print(f"  Speedup:         {speedup:.2f}x faster with better algorithm")
        
        # Fibonacci memoization comparison
        print("\n7. Fibonacci Memoization (n=40)")
        print("=" * 32)
        
        print("Recursive C++ Implementation:")
        rec_result, rec_time = benchmark_function(
            cpp_accelerated.fibonacci_recursive, 40, iterations=1, name="Recursive"
        )
        
        print("Memoized C++ Implementation:")
        memo_result, memo_time = benchmark_function(
            cpp_accelerated.fibonacci_memoized, 40, iterations=1, name="Memoized"
        )
        
        if rec_result == memo_result:
            print("✓ Results match!")
            if rec_time > 0:
                speedup = rec_time / memo_time
                print(f"\nMemoization Impact:")
                print(f"  Recursive time:  {rec_time:.6f} seconds")
                print(f"  Memoized time:   {memo_time:.6f} seconds")
                print(f"  Speedup:         {speedup:.2f}x faster with memoization")
    
    print("\n" + "=" * 50)
    print("Benchmark Complete!")
    print("=" * 50)
    
    if CPP_AVAILABLE:
        print("\nKey Takeaways:")
        print("• C++ provides significant speedups for compute-intensive tasks")
        print("• Algorithm choice matters more than language for some problems")
        print("• Memory optimization (memoization) can provide dramatic improvements")
        print("• Mathematical formulas can replace iterative calculations")
    else:
        print("\nTo see C++ performance comparison:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Build extension: python setup.py build_ext --inplace")
        print("3. Re-run this script: python performance_benchmark.py")


def run_quick_test():
    """Run a quick test to verify everything is working."""
    print("Quick Functionality Test")
    print("=" * 25)
    
    # Test Python implementation
    print("Testing Python implementation...")
    result = python_implementation.sum_of_squares(1000)
    print(f"  Sum of squares (1-1000): {result}")
    
    if CPP_AVAILABLE:
        print("Testing C++ implementation...")
        cpp_result = cpp_accelerated.sum_of_squares(1000)
        print(f"  Sum of squares (1-1000): {cpp_result}")
        
        if result == cpp_result:
            print("✓ Both implementations produce the same result!")
        else:
            print("✗ Results differ between implementations!")
    else:
        print("C++ implementation not available.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        run_quick_test()
    else:
        run_all_benchmarks()