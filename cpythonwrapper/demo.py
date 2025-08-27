#!/usr/bin/env python3
"""
Simple demonstration script showing how to use both Python and C++ implementations.
This script provides an easy way to test individual functions and see the performance difference.
"""

import time
import sys

# Import implementations
import python_implementation

try:
    import cpp_accelerated
    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
    print("Warning: C++ module not available. Only Python functions will work.")
    print("To build: python setup.py build_ext --inplace")


def demo_sum_of_squares():
    """Demonstrate sum of squares calculation."""
    print("\n" + "="*50)
    print("SUM OF SQUARES DEMO")
    print("="*50)
    
    n = 100000
    print(f"Calculating sum of squares from 1 to {n:,}")
    
    # Python version
    start = time.perf_counter()
    py_result = python_implementation.sum_of_squares(n)
    py_time = time.perf_counter() - start
    print(f"Python result: {py_result:,} (took {py_time:.6f}s)")
    
    if CPP_AVAILABLE:
        # C++ version
        start = time.perf_counter()
        cpp_result = cpp_accelerated.sum_of_squares(n)
        cpp_time = time.perf_counter() - start
        print(f"C++ result:    {cpp_result:,} (took {cpp_time:.6f}s)")
        
        # Optimized C++ version
        start = time.perf_counter()
        opt_result = cpp_accelerated.sum_of_squares_optimized(n)
        opt_time = time.perf_counter() - start
        print(f"C++ optimized: {opt_result:,} (took {opt_time:.6f}s)")
        
        if py_time > 0:
            speedup = py_time / cpp_time
            print(f"\nSpeedup: {speedup:.1f}x faster with C++")


def demo_fibonacci():
    """Demonstrate Fibonacci calculation."""
    print("\n" + "="*50)
    print("FIBONACCI DEMO")
    print("="*50)
    
    n = 35
    print(f"Calculating Fibonacci number #{n}")
    
    # Python version
    start = time.perf_counter()
    py_result = python_implementation.fibonacci_recursive(n)
    py_time = time.perf_counter() - start
    print(f"Python result: {py_result:,} (took {py_time:.6f}s)")
    
    if CPP_AVAILABLE:
        # C++ recursive version
        start = time.perf_counter()
        cpp_result = cpp_accelerated.fibonacci_recursive(n)
        cpp_time = time.perf_counter() - start
        print(f"C++ recursive: {cpp_result:,} (took {cpp_time:.6f}s)")
        
        # C++ memoized version
        start = time.perf_counter()
        memo_result = cpp_accelerated.fibonacci_memoized(n)
        memo_time = time.perf_counter() - start
        print(f"C++ memoized:  {memo_result:,} (took {memo_time:.6f}s)")
        
        if py_time > 0:
            speedup1 = py_time / cpp_time
            speedup2 = py_time / memo_time
            print(f"\nSpeedup: {speedup1:.1f}x faster with C++ recursive")
            print(f"Speedup: {speedup2:.1f}x faster with C++ memoized")


def demo_prime_count():
    """Demonstrate prime counting."""
    print("\n" + "="*50)
    print("PRIME COUNT DEMO")
    print("="*50)
    
    limit = 10000
    print(f"Counting prime numbers up to {limit:,}")
    
    # Python version
    start = time.perf_counter()
    py_result = python_implementation.prime_count(limit)
    py_time = time.perf_counter() - start
    print(f"Python result: {py_result:,} primes (took {py_time:.6f}s)")
    
    if CPP_AVAILABLE:
        # C++ trial division version
        start = time.perf_counter()
        cpp_result = cpp_accelerated.prime_count(limit)
        cpp_time = time.perf_counter() - start
        print(f"C++ trial div: {cpp_result:,} primes (took {cpp_time:.6f}s)")
        
        # C++ sieve version
        start = time.perf_counter()
        sieve_result = cpp_accelerated.prime_count_optimized(limit)
        sieve_time = time.perf_counter() - start
        print(f"C++ sieve:     {sieve_result:,} primes (took {sieve_time:.6f}s)")
        
        if py_time > 0:
            speedup1 = py_time / cpp_time
            speedup2 = py_time / sieve_time
            print(f"\nSpeedup: {speedup1:.1f}x faster with C++ trial division")
            print(f"Speedup: {speedup2:.1f}x faster with C++ sieve")


def demo_matrix_mult():
    """Demonstrate matrix multiplication."""
    print("\n" + "="*50)
    print("MATRIX MULTIPLICATION DEMO")
    print("="*50)
    
    size = 100
    print(f"Multiplying two {size}x{size} matrices")
    
    # Python version
    start = time.perf_counter()
    py_result = python_implementation.matrix_multiplication(size)
    py_time = time.perf_counter() - start
    print(f"Python result: First element = {py_result[0][0]} (took {py_time:.6f}s)")
    
    if CPP_AVAILABLE:
        # C++ version
        start = time.perf_counter()
        cpp_result = cpp_accelerated.matrix_multiplication(size)
        cpp_time = time.perf_counter() - start
        print(f"C++ result:    First element = {cpp_result[0][0]} (took {cpp_time:.6f}s)")
        
        if py_time > 0:
            speedup = py_time / cpp_time
            print(f"\nSpeedup: {speedup:.1f}x faster with C++")


def interactive_demo():
    """Interactive demo allowing user to choose which functions to test."""
    print("Python + C++ Performance Comparison Demo")
    print("="*50)
    
    if not CPP_AVAILABLE:
        print("\nWARNING: C++ module not available.")
        print("To build: python setup.py build_ext --inplace\n")
    
    while True:
        print("\nAvailable demos:")
        print("1. Sum of Squares")
        print("2. Fibonacci")
        print("3. Prime Count")
        print("4. Matrix Multiplication")
        print("5. Run All Demos")
        print("0. Exit")
        
        try:
            choice = input("\nSelect demo (0-5): ").strip()
            
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                demo_sum_of_squares()
            elif choice == "2":
                demo_fibonacci()
            elif choice == "3":
                demo_prime_count()
            elif choice == "4":
                demo_matrix_mult()
            elif choice == "5":
                demo_sum_of_squares()
                demo_fibonacci()
                demo_prime_count()
                demo_matrix_mult()
            else:
                print("Invalid choice. Please select 0-5.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        demo_name = sys.argv[1].lower()
        if demo_name in ["sum", "squares"]:
            demo_sum_of_squares()
        elif demo_name in ["fib", "fibonacci"]:
            demo_fibonacci()
        elif demo_name in ["prime", "primes"]:
            demo_prime_count()
        elif demo_name in ["matrix", "mult"]:
            demo_matrix_mult()
        elif demo_name in ["all", "demo"]:
            demo_sum_of_squares()
            demo_fibonacci()
            demo_prime_count()
            demo_matrix_mult()
        else:
            print(f"Unknown demo: {demo_name}")
            print("Available: sum, fibonacci, prime, matrix, all")
    else:
        interactive_demo()