# Examples Directory

This directory contains comprehensive examples demonstrating how to use the Python + C++ Performance Wrapper project. Each script showcases different aspects and use cases of the performance comparison framework.

## 📁 Available Examples

### 1. `basic_usage.py`
**Purpose**: Introduction to the basic functionality and simple comparisons.

**Features**:
- Simple performance comparisons with manageable data sizes
- Demonstrates C++ optimized algorithms vs standard implementations
- Shows how to create custom benchmarks
- Perfect for getting started and understanding the basics

**Usage**:
```bash
cd examples
python basic_usage.py
```

**What you'll see**:
- Sum of squares comparison (1 to 1000)
- Fibonacci number calculation (n=30)
- Prime counting up to 1000
- Small matrix multiplication (50x50)
- Algorithm optimization examples

### 2. `advanced_usage.py`
**Purpose**: Advanced usage patterns and real-world scenarios.

**Features**:
- Performance profiling class for detailed analysis
- Large-scale computational examples
- Memory efficiency demonstrations
- Real-world pipeline simulations
- Integration patterns for existing projects

**Usage**:
```bash
cd examples
python advanced_usage.py
```

**What you'll see**:
- Large-scale numerical computations
- Algorithmic optimization showcases
- Memory efficiency comparisons
- Real-world data processing pipeline simulation
- Code integration examples

### 3. `performance_analysis.py`
**Purpose**: Comprehensive performance analysis and report generation.

**Features**:
- Statistical analysis of performance data
- Detailed benchmarking across multiple scenarios
- JSON and text report generation
- System information gathering
- Performance recommendations

**Usage**:
```bash
cd examples
python performance_analysis.py
```

**Generated Files**:
- `performance_report.txt` - Human-readable analysis report
- `performance_analysis.json` - Detailed machine-readable results

**What you'll get**:
- Comprehensive performance comparison across all functions
- Statistical analysis (mean, median, standard deviation)
- System information and environment details
- Performance recommendations based on results

## 🚀 Quick Start Guide

### Option 1: Run All Examples

```bash
# From the project root directory
cd examples

# Basic examples (good starting point)
python basic_usage.py

# Advanced scenarios
python advanced_usage.py

# Comprehensive analysis
python performance_analysis.py
```

### Option 2: Using the Examples with Make

```bash
# From the project root directory
make demo  # Runs the interactive demo
make benchmark  # Runs the full benchmark suite

# Then explore examples
cd examples
python basic_usage.py
```

## 📊 Expected Performance Results

Based on typical runs, you can expect to see:

### Basic Functions
- **Sum of Squares**: 50x - 2000x speedup
- **Fibonacci**: 50x - 100x speedup (recursive), 10000x+ (memoized)
- **Prime Count**: 20x - 80x speedup
- **Matrix Multiplication**: 100x - 300x speedup

### Optimized Algorithms
- **Mathematical Formula vs Iteration**: 2x - 5x additional speedup
- **Sieve vs Trial Division**: 5x - 10x additional speedup
- **Memoization vs Recursion**: 1000x - 100000x speedup

## 🔧 Customizing Examples

### Creating Your Own Benchmark

```python
import time
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import python_implementation
import cpp_accelerated  # If available

def custom_benchmark():
    # Your custom function benchmark
    n = 50000
    
    # Python timing
    start = time.perf_counter()
    py_result = python_implementation.sum_of_squares(n)
    py_time = time.perf_counter() - start
    
    # C++ timing
    start = time.perf_counter()
    cpp_result = cpp_accelerated.sum_of_squares(n)
    cpp_time = time.perf_counter() - start
    
    speedup = py_time / cpp_time
    print(f"Custom benchmark speedup: {speedup:.2f}x")

if __name__ == "__main__":
    custom_benchmark()
```

### Adding New Test Cases

To add your own test cases to the examples:

1. **Basic Usage**: Add to the `basic_examples()` function
2. **Advanced Usage**: Add to any of the specialized functions
3. **Performance Analysis**: Add to the `scenarios` list in `run_comprehensive_analysis()`

## 🐛 Troubleshooting Examples

### Common Issues

**Issue**: `ImportError: No module named 'cpp_accelerated'`
**Solution**: Build the C++ extension first:
```bash
cd ..  # Go back to project root
python setup.py build_ext --inplace
cd examples
```

**Issue**: Examples run but show "C++ module not available"
**Solution**: Ensure the C++ extension built successfully and is in the parent directory.

**Issue**: Very slow performance on some examples
**Solution**: The advanced examples use larger datasets. Start with basic examples first.

### Platform-Specific Notes

#### macOS
- Ensure Xcode Command Line Tools are installed
- On Apple Silicon, the extension should build for arm64 automatically

#### Windows
- Visual Studio Build Tools required
- Some examples may show different performance characteristics

#### Linux
- GCC build tools required (`sudo apt install build-essential`)
- Generally shows the best C++ performance improvements

## 📈 Understanding the Results

### Performance Metrics Explained

- **Speedup**: How many times faster C++ is compared to Python
- **Improvement %**: Percentage improvement over Python baseline
- **Statistical Analysis**: Mean, median, and standard deviation of multiple runs
- **Results Match**: Verification that both implementations produce identical results

### Interpreting Speedups

- **1x - 5x**: Modest improvement, overhead may be significant
- **5x - 50x**: Good improvement, worthwhile for performance-critical code
- **50x - 500x**: Excellent improvement, highly recommended
- **500x+**: Exceptional improvement, transformative for the application

## 💡 Best Practices

1. **Start Simple**: Begin with `basic_usage.py` to understand the concepts
2. **Verify Results**: Always check that Python and C++ implementations match
3. **Multiple Runs**: Use multiple iterations for reliable timing measurements
4. **Appropriate Scale**: Use data sizes appropriate for your actual use case
5. **System Warm-up**: Run examples multiple times for consistent results

## 🔗 Related Resources

- [../README.md](../README.md) - Main project documentation
- [../performance_benchmark.py](../performance_benchmark.py) - Built-in benchmark script
- [../demo.py](../demo.py) - Interactive demonstration
- [Pybind11 Documentation](https://pybind11.readthedocs.io/) - Python-C++ binding framework

## 📞 Support

If you encounter issues with the examples:

1. Check that the C++ extension is built correctly
2. Verify your Python environment has all required packages
3. Look at the troubleshooting section above
4. Open an issue in the project repository with your system details and error messages