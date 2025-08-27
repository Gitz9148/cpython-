#!/usr/bin/env python3
"""
Performance Analysis and Report Generator

This script generates detailed performance analysis reports comparing
Python and C++ implementations across various scenarios and datasets.
"""

import time
import sys
import os
import statistics
from typing import Dict, List, Tuple, Any
import json

# Add the parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import python_implementation

try:
    import cpp_accelerated
    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
    print("Warning: C++ module not available. Analysis will be limited to Python only.")


class PerformanceAnalyzer:
    """Comprehensive performance analysis tool."""
    
    def __init__(self):
        self.results = []
        self.system_info = self._get_system_info()
    
    def _get_system_info(self) -> Dict[str, str]:
        """Gather system information for the report."""
        import platform
        return {
            'platform': platform.platform(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'architecture': platform.architecture()[0],
            'system': platform.system(),
            'cpp_available': CPP_AVAILABLE
        }
    
    def benchmark_function(self, name: str, func, args: Tuple, iterations: int = 5) -> Dict[str, Any]:
        """Benchmark a single function with statistical analysis."""
        times = []
        result = None
        
        # Warm-up run
        result = func(*args)
        
        # Actual benchmarking
        for _ in range(iterations):
            start = time.perf_counter()
            result = func(*args)
            end = time.perf_counter()
            times.append(end - start)
        
        # Statistical analysis
        return {
            'name': name,
            'result': result,
            'times': times,
            'mean': statistics.mean(times),
            'median': statistics.median(times),
            'stdev': statistics.stdev(times) if len(times) > 1 else 0,
            'min': min(times),
            'max': max(times),
            'iterations': iterations
        }
    
    def compare_implementations(self, task_name: str, python_func, cpp_func, args: Tuple, iterations: int = 5) -> Dict[str, Any]:
        """Compare Python and C++ implementations with detailed analysis."""
        print(f"Analyzing: {task_name}...")
        
        # Benchmark Python implementation
        py_results = self.benchmark_function(f"{task_name} (Python)", python_func, args, iterations)
        
        comparison = {
            'task': task_name,
            'args': args,
            'python': py_results,
            'cpp': None,
            'speedup': None,
            'improvement_percent': None
        }
        
        if CPP_AVAILABLE and cpp_func:
            # Benchmark C++ implementation
            cpp_results = self.benchmark_function(f"{task_name} (C++)", cpp_func, args, iterations)
            comparison['cpp'] = cpp_results
            
            # Calculate speedup metrics
            if cpp_results['mean'] > 0:
                speedup = py_results['mean'] / cpp_results['mean']
                improvement = ((speedup - 1) * 100)
                comparison['speedup'] = speedup
                comparison['improvement_percent'] = improvement
            
            # Verify correctness
            comparison['results_match'] = (py_results['result'] == cpp_results['result'])
        
        self.results.append(comparison)
        return comparison
    
    def run_comprehensive_analysis(self):
        """Run a comprehensive performance analysis across various scenarios."""
        print("Running Comprehensive Performance Analysis")
        print("=" * 60)
        
        # Test scenarios with different complexity levels
        scenarios = [
            # Sum of squares with increasing complexity
            ("Sum of Squares (n=1K)", python_implementation.sum_of_squares, 
             cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None, (1000,)),
            ("Sum of Squares (n=10K)", python_implementation.sum_of_squares, 
             cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None, (10000,)),
            ("Sum of Squares (n=100K)", python_implementation.sum_of_squares, 
             cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None, (100000,)),
            ("Sum of Squares (n=1M)", python_implementation.sum_of_squares, 
             cpp_accelerated.sum_of_squares if CPP_AVAILABLE else None, (1000000,)),
            
            # Fibonacci with increasing complexity
            ("Fibonacci (n=25)", python_implementation.fibonacci_recursive, 
             cpp_accelerated.fibonacci_recursive if CPP_AVAILABLE else None, (25,)),
            ("Fibonacci (n=30)", python_implementation.fibonacci_recursive, 
             cpp_accelerated.fibonacci_recursive if CPP_AVAILABLE else None, (30,)),
            ("Fibonacci (n=35)", python_implementation.fibonacci_recursive, 
             cpp_accelerated.fibonacci_recursive if CPP_AVAILABLE else None, (35,)),
            
            # Prime counting with different ranges
            ("Prime Count (n=1K)", python_implementation.prime_count, 
             cpp_accelerated.prime_count if CPP_AVAILABLE else None, (1000,)),
            ("Prime Count (n=10K)", python_implementation.prime_count, 
             cpp_accelerated.prime_count if CPP_AVAILABLE else None, (10000,)),
            ("Prime Count (n=50K)", python_implementation.prime_count, 
             cpp_accelerated.prime_count if CPP_AVAILABLE else None, (50000,)),
            
            # Matrix multiplication with different sizes
            ("Matrix Mult (50x50)", python_implementation.matrix_multiplication, 
             cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None, (50,)),
            ("Matrix Mult (100x100)", python_implementation.matrix_multiplication, 
             cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None, (100,)),
            ("Matrix Mult (200x200)", python_implementation.matrix_multiplication, 
             cpp_accelerated.matrix_multiplication if CPP_AVAILABLE else None, (200,)),
        ]
        
        # Run all scenarios
        for scenario in scenarios:
            task_name, py_func, cpp_func, args = scenario
            self.compare_implementations(task_name, py_func, cpp_func, args)
        
        # Run optimized algorithm comparisons if C++ is available
        if CPP_AVAILABLE:
            self._analyze_optimized_algorithms()
    
    def _analyze_optimized_algorithms(self):
        """Analyze optimized C++ algorithms against standard implementations."""
        print("\nAnalyzing Optimized Algorithms...")
        
        # Sum of squares: standard vs optimized
        n = 1000000
        std_results = self.benchmark_function("Sum Squares Standard", cpp_accelerated.sum_of_squares, (n,))
        opt_results = self.benchmark_function("Sum Squares Optimized", cpp_accelerated.sum_of_squares_optimized, (n,))
        
        optimization_comparison = {
            'task': 'Sum of Squares Optimization',
            'standard': std_results,
            'optimized': opt_results,
            'speedup': std_results['mean'] / opt_results['mean'] if opt_results['mean'] > 0 else None
        }
        
        # Prime counting: trial division vs sieve
        limit = 100000
        trial_results = self.benchmark_function("Prime Count Trial", cpp_accelerated.prime_count, (limit,))
        sieve_results = self.benchmark_function("Prime Count Sieve", cpp_accelerated.prime_count_optimized, (limit,))
        
        algorithm_comparison = {
            'task': 'Prime Count Algorithm Comparison',
            'trial_division': trial_results,
            'sieve': sieve_results,
            'speedup': trial_results['mean'] / sieve_results['mean'] if sieve_results['mean'] > 0 else None
        }
        
        # Fibonacci: recursive vs memoized
        n = 40
        rec_results = self.benchmark_function("Fibonacci Recursive", cpp_accelerated.fibonacci_recursive, (n,), iterations=1)
        memo_results = self.benchmark_function("Fibonacci Memoized", cpp_accelerated.fibonacci_memoized, (n,))
        
        memoization_comparison = {
            'task': 'Fibonacci Memoization',
            'recursive': rec_results,
            'memoized': memo_results,
            'speedup': rec_results['mean'] / memo_results['mean'] if memo_results['mean'] > 0 else None
        }
        
        # Store optimization results
        self.optimization_results = [optimization_comparison, algorithm_comparison, memoization_comparison]
    
    def generate_text_report(self) -> str:
        """Generate a comprehensive text report."""
        report = []
        report.append("PYTHON + C++ PERFORMANCE ANALYSIS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # System information
        report.append("System Information:")
        report.append(f"  Platform: {self.system_info['platform']}")
        report.append(f"  Processor: {self.system_info['processor']}")
        report.append(f"  Python Version: {self.system_info['python_version']}")
        report.append(f"  Architecture: {self.system_info['architecture']}")
        report.append(f"  C++ Module Available: {self.system_info['cpp_available']}")
        report.append("")
        
        # Performance comparison results
        report.append("Performance Comparison Results:")
        report.append("-" * 40)
        report.append("")
        
        if CPP_AVAILABLE:
            report.append(f"{'Task':<25} {'Python (ms)':<12} {'C++ (ms)':<10} {'Speedup':<8} {'Match':<6}")
            report.append("-" * 65)
            
            for result in self.results:
                if result['cpp']:
                    py_time = result['python']['mean'] * 1000  # Convert to ms
                    cpp_time = result['cpp']['mean'] * 1000
                    speedup = result['speedup'] or 0
                    match = "✓" if result['results_match'] else "✗"
                    
                    report.append(f"{result['task']:<25} {py_time:<12.3f} {cpp_time:<10.3f} {speedup:<8.2f} {match:<6}")
        else:
            report.append(f"{'Task':<30} {'Python (ms)':<12}")
            report.append("-" * 45)
            
            for result in self.results:
                py_time = result['python']['mean'] * 1000
                report.append(f"{result['task']:<30} {py_time:<12.3f}")
        
        report.append("")
        
        # Statistical summary
        if CPP_AVAILABLE and any(r['speedup'] for r in self.results if r['speedup']):
            speedups = [r['speedup'] for r in self.results if r['speedup']]
            report.append("Statistical Summary:")
            report.append(f"  Average Speedup: {statistics.mean(speedups):.2f}x")
            report.append(f"  Median Speedup: {statistics.median(speedups):.2f}x")
            report.append(f"  Max Speedup: {max(speedups):.2f}x")
            report.append(f"  Min Speedup: {min(speedups):.2f}x")
            if len(speedups) > 1:
                report.append(f"  Speedup Std Dev: {statistics.stdev(speedups):.2f}")
            report.append("")
        
        # Optimization results
        if hasattr(self, 'optimization_results'):
            report.append("Algorithm Optimization Results:")
            report.append("-" * 35)
            
            for opt_result in self.optimization_results:
                task = opt_result['task']
                speedup = opt_result.get('speedup', 0)
                report.append(f"  {task}: {speedup:.2f}x improvement")
            report.append("")
        
        # Recommendations
        report.append("Recommendations:")
        report.append("-" * 15)
        
        if CPP_AVAILABLE:
            avg_speedup = statistics.mean([r['speedup'] for r in self.results if r['speedup']])
            if avg_speedup > 10:
                report.append("  • Excellent performance gains with C++ acceleration")
                report.append("  • Recommended for production use in compute-intensive applications")
            elif avg_speedup > 3:
                report.append("  • Good performance improvements with C++ acceleration")
                report.append("  • Consider C++ for performance-critical sections")
            else:
                report.append("  • Modest performance gains with C++ acceleration")
                report.append("  • Evaluate trade-offs between complexity and performance")
        else:
            report.append("  • Build C++ extension to unlock performance improvements")
            report.append("  • Expected speedups: 10x-1000x for computational tasks")
        
        report.append("")
        report.append("Analysis complete.")
        
        return "\n".join(report)
    
    def save_json_results(self, filename: str = "performance_analysis.json"):
        """Save detailed results to JSON file."""
        data = {
            'system_info': self.system_info,
            'results': self.results,
            'optimization_results': getattr(self, 'optimization_results', []),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"Detailed results saved to {filename}")


def main():
    """Main analysis function."""
    analyzer = PerformanceAnalyzer()
    
    # Run comprehensive analysis
    analyzer.run_comprehensive_analysis()
    
    # Generate and display report
    print("\n" + "=" * 60)
    report = analyzer.generate_text_report()
    print(report)
    
    # Save results
    analyzer.save_json_results()
    
    # Save text report
    with open("performance_report.txt", 'w') as f:
        f.write(report)
    
    print("Text report saved to performance_report.txt")


if __name__ == "__main__":
    main()