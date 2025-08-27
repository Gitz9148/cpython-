#!/usr/bin/env python3
"""
Advanced Usage Examples for Python + C++ Performance Wrapper

This script demonstrates advanced usage patterns and real-world scenarios
where C++ acceleration can provide significant benefits.
"""

import time
import sys
import os
from typing import List, Tuple

# Add the parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import python_implementation

try:
    import cpp_accelerated
    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
    print("Warning: C++ module not available. Some examples will be limited.")


class PerformanceProfiler:
    """A simple performance profiler for comparing implementations."""
    
    def __init__(self):
        self.results = []
    
    def profile_function(self, name: str, func, *args, iterations: int = 1):
        """Profile a function and store results."""
        times = []
        result = None
        
        for _ in range(iterations):
            start = time.perf_counter()
            result = func(*args)
            end = time.perf_counter()
            times.append(end - start)
        
        avg_time = sum(times) / len(times)
        self.results.append({
            'name': name,
            'result': result,
            'avg_time': avg_time,
            'times': times,
            'iterations': iterations
        })
        
        return result, avg_time
    
    def compare_implementations(self, task_name: str, python_func, cpp_func, *args, iterations: int = 3):
        """Compare Python and C++ implementations."""
        print(f"\n{task_name}")
        print("=" * len(task_name))
        
        # Profile Python implementation
        py_result, py_time = self.profile_function(
            f"{task_name} (Python)", python_func, *args, iterations=iterations
        )
        print(f"Python: {py_result} (avg: {py_time:.6f}s)")
        
        if CPP_AVAILABLE and cpp_func:
            # Profile C++ implementation
            cpp_result, cpp_time = self.profile_function(
                f"{task_name} (C++)", cpp_func, *args, iterations=iterations
            )
            print(f"C++:    {cpp_result} (avg: {cpp_time:.6f}s)")
            
            # Calculate and display speedup
            if py_time > 0:
                speedup = py_time / cpp_time
                improvement = ((speedup - 1) * 100)
                print(f"Speedup: {speedup:.2f}x ({improvement:.1f}% improvement)")
            
            # Verify correctness
            if py_result == cpp_result:
                print("✓ Results verified: implementations match")
            else:
                print("✗ Warning: results differ between implementations")
        else:
            print("C++ implementation not available for comparison")
    
    def generate_report(self):
        """Generate a performance report."""
        if not self.results:
            return "No profiling data available."
        
        report = "\nPerformance Report\n" + "=" * 50 + "\n"
        
        for result in self.results:
            report += f"Task: {result['name']}\n"
            report += f"  Average time: {result['avg_time']:.6f}s\n"
            report += f"  Iterations: {result['iterations']}\n"
            if len(result['times']) > 1:
                min_time = min(result['times'])
                max_time = max(result['times'])
                report += f"  Min time: {min_time:.6f}s\n"
                report += f"  Max time: {max_time:.6f}s\n"
            report += "\n"
        
        return report


def numerical_computation_examples():
    """Examples of numerical computations that benefit from C++ acceleration."""
    profiler = PerformanceProfiler()
    
    print("Numerical Computation Examples")
    print("=" * 50)
    
    # Large-scale sum of squares
    profiler.compare_implementations(
        "Large Sum of Squares (n=500,000)",
        python_implementation.sum_of_squares,
        cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None,
        500000,
        iterations=3
    )
    
    # Prime number analysis
    profiler.compare_implementations(
        "Prime Analysis (limit=50,000)",
        python_implementation.prime_count,
        cpp_accelerated.prime_count if CPP_AVAILABLE else None,
        50000,
        iterations=3
    )
    
    # Matrix operations
    profiler.compare_implementations(
        "Matrix Operations (200x200)",
        python_implementation.matrix_multiplication,
        cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None,
        200,
        iterations=2
    )
    
    return profiler


def algorithmic_optimization_showcase():
    """Showcase different algorithmic approaches."""
    if not CPP_AVAILABLE:
        print("\nAlgorithmic optimization showcase requires C++ module.")
        return
    
    print("\n" + "=" * 50)
    print("Algorithmic Optimization Showcase")
    print("=" * 50)
    
    # Sum of squares: iteration vs mathematical formula
    print("\nSum of Squares: Iteration vs Mathematical Formula")
    print("-" * 52)
    
    n = 1000000
    iterations = 10
    
    # Iterative approach
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result1 = cpp_accelerated.sum_of_squares(n)
        times.append(time.perf_counter() - start)
    avg_iterative = sum(times) / len(times)
    
    # Mathematical formula approach
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result2 = cpp_accelerated.sum_of_squares_optimized(n)
        times.append(time.perf_counter() - start)
    avg_formula = sum(times) / len(times)
    
    print(f"Iterative method:  {result1} (avg: {avg_iterative:.6f}s)")
    print(f"Formula method:    {result2} (avg: {avg_formula:.6f}s)")
    print(f"Formula speedup:   {avg_iterative/avg_formula:.2f}x")
    
    # Prime counting: trial division vs sieve
    print("\nPrime Counting: Trial Division vs Sieve of Eratosthenes")
    print("-" * 56)
    
    limit = 100000
    iterations = 5
    
    # Trial division
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result1 = cpp_accelerated.prime_count(limit)
        times.append(time.perf_counter() - start)
    avg_trial = sum(times) / len(times)
    
    # Sieve method
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        result2 = cpp_accelerated.prime_count_optimized(limit)
        times.append(time.perf_counter() - start)
    avg_sieve = sum(times) / len(times)
    
    print(f"Trial division:    {result1} primes (avg: {avg_trial:.6f}s)")
    print(f"Sieve method:      {result2} primes (avg: {avg_sieve:.6f}s)")
    print(f"Sieve speedup:     {avg_trial/avg_sieve:.2f}x")


def memory_efficiency_example():
    """Demonstrate memory efficiency differences."""
    print("\n" + "=" * 50)
    print("Memory Efficiency Example")
    print("=" * 50)
    
    print("\nNote: This is a conceptual example. In practice, C++ provides:")
    print("• Better memory layout control")
    print("• Reduced garbage collection overhead")
    print("• More efficient data structures")
    print("• Stack allocation for temporary objects")
    
    # Simulate multiple matrix operations
    sizes = [50, 100, 150, 200]
    
    print(f"\nMatrix multiplication performance scaling:")
    print(f"{'Size':<8} {'Python (s)':<12} {'C++ (s)':<10} {'Speedup':<8}")
    print("-" * 40)
    
    for size in sizes:
        # Python timing
        start = time.perf_counter()
        py_result = python_implementation.matrix_multiplication(size)
        py_time = time.perf_counter() - start
        
        if CPP_AVAILABLE:
            # C++ timing
            start = time.perf_counter()
            cpp_result = cpp_accelerated.matrix_multiplication(size)
            cpp_time = time.perf_counter() - start
            
            speedup = py_time / cpp_time
            print(f"{size}x{size:<4} {py_time:<12.6f} {cpp_time:<10.6f} {speedup:<8.2f}x")
        else:
            print(f"{size}x{size:<4} {py_time:<12.6f} {'N/A':<10} {'N/A':<8}")


def real_world_scenario():
    """Simulate a real-world computational scenario."""
    print("\n" + "=" * 50)
    print("Real-World Scenario: Computational Analysis Pipeline")
    print("=" * 50)
    
    print("\nScenario: Processing mathematical sequences for data analysis")
    print("Tasks: Multiple sum calculations, prime analysis, and data transformation")
    
    # Simulate a data processing pipeline
    datasets = [10000, 25000, 50000, 75000, 100000]
    
    total_py_time = 0
    total_cpp_time = 0
    
    print(f"\n{'Dataset Size':<12} {'Python Time':<12} {'C++ Time':<10} {'Speedup':<8}")
    print("-" * 45)
    
    for size in datasets:
        # Python pipeline
        start = time.perf_counter()
        py_sum = python_implementation.sum_of_squares(size)
        py_primes = python_implementation.prime_count(min(size, 10000))  # Limit to avoid long execution
        py_time = time.perf_counter() - start
        total_py_time += py_time
        
        if CPP_AVAILABLE:
            # C++ pipeline
            start = time.perf_counter()
            cpp_sum = cpp_accelerated.sum_of_squares(size)
            cpp_primes = cpp_accelerated.prime_count(min(size, 10000))
            cpp_time = time.perf_counter() - start
            total_cpp_time += cpp_time
            
            speedup = py_time / cpp_time if cpp_time > 0 else float('inf')
            print(f"{size:<12} {py_time:<12.6f} {cpp_time:<10.6f} {speedup:<8.2f}x")
        else:
            print(f"{size:<12} {py_time:<12.6f} {'N/A':<10} {'N/A':<8}")
    
    print("-" * 45)
    
    if CPP_AVAILABLE and total_cpp_time > 0:
        overall_speedup = total_py_time / total_cpp_time
        print(f"{'Total':<12} {total_py_time:<12.6f} {total_cpp_time:<10.6f} {overall_speedup:<8.2f}x")
        print(f"\nOverall pipeline speedup: {overall_speedup:.2f}x")
        print(f"Time saved: {total_py_time - total_cpp_time:.6f}s ({((total_py_time - total_cpp_time)/total_py_time)*100:.1f}%)")
    else:
        print(f"{'Total':<12} {total_py_time:<12.6f} {'N/A':<10} {'N/A':<8}")


def integration_examples():
    """Show how to integrate C++ acceleration into existing Python projects."""
    print("\n" + "=" * 50)
    print("Integration Examples")
    print("=" * 50)
    
    print("\nExample 1: Drop-in replacement pattern")
    print("-" * 40)
    
    code_example = '''
# Before: Pure Python
def calculate_metrics(data_size):
    sum_sq = python_implementation.sum_of_squares(data_size)
    primes = python_implementation.prime_count(data_size // 10)
    return sum_sq, primes

# After: C++ accelerated (with fallback)
def calculate_metrics_fast(data_size):
    try:
        import cpp_accelerated
        sum_sq = cpp_accelerated.sum_of_squares(data_size)
        primes = cpp_accelerated.prime_count(data_size // 10)
    except ImportError:
        # Fallback to Python implementation
        sum_sq = python_implementation.sum_of_squares(data_size)
        primes = python_implementation.prime_count(data_size // 10)
    return sum_sq, primes
    '''
    
    print(code_example)
    
    print("\nExample 2: Configuration-based acceleration")
    print("-" * 45)
    
    config_example = '''
class ComputationEngine:
    def __init__(self, use_cpp_acceleration=True):
        self.use_cpp = use_cpp_acceleration and CPP_AVAILABLE
        
    def sum_of_squares(self, n):
        if self.use_cpp:
            return cpp_accelerated.sum_of_squares(n)
        return python_implementation.sum_of_squares(n)
    '''
    
    print(config_example)


if __name__ == "__main__":
    print("Advanced Usage Examples for Python + C++ Performance Wrapper")
    print("=" * 70)
    
    # Run all advanced examples
    profiler = numerical_computation_examples()
    algorithmic_optimization_showcase()
    memory_efficiency_example()
    real_world_scenario()
    integration_examples()
    
    # Generate final report
    print(profiler.generate_report())
    
    print("=" * 70)
    print("Advanced examples complete!")
    
    if not CPP_AVAILABLE:
        print("\nTo unlock the full potential of these examples:")
        print("1. Build the C++ extension: python setup.py build_ext --inplace")
        print("2. Re-run this script: python examples/advanced_usage.py")