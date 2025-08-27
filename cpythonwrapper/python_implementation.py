"""
Pure Python implementation of computationally intensive functions.
This module contains functions that will be accelerated using C++.
"""

import time
import math


def sum_of_squares(n):
    """
    Calculate the sum of squares from 1 to n.
    This is a computationally intensive function perfect for demonstrating
    the performance difference between Python and C++.
    
    Args:
        n (int): Upper limit for the sum calculation
        
    Returns:
        int: Sum of squares from 1 to n
    """
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursive approach.
    This demonstrates the performance impact of recursive calls.
    
    Args:
        n (int): Position in Fibonacci sequence
        
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def prime_count(limit):
    """
    Count the number of prime numbers up to the given limit.
    Uses a simple trial division method.
    
    Args:
        limit (int): Upper limit for prime counting
        
    Returns:
        int: Number of prime numbers up to limit
    """
    if limit < 2:
        return 0
    
    count = 0
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    
    return count


def matrix_multiplication(size):
    """
    Perform matrix multiplication of two size x size matrices.
    Creates random-like matrices and multiplies them.
    
    Args:
        size (int): Size of the square matrices
        
    Returns:
        list: Result matrix as list of lists
    """
    # Create two matrices with simple values
    matrix_a = [[i + j for j in range(size)] for i in range(size)]
    matrix_b = [[i * j + 1 for j in range(size)] for i in range(size)]
    
    # Initialize result matrix
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    # Perform matrix multiplication
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result


def benchmark_function(func, *args, iterations=1):
    """
    Benchmark a function by running it multiple times and measuring execution time.
    
    Args:
        func: Function to benchmark
        *args: Arguments to pass to the function
        iterations (int): Number of times to run the function
        
    Returns:
        tuple: (result, average_time_seconds)
    """
    start_time = time.perf_counter()
    
    result = None
    for _ in range(iterations):
        result = func(*args)
    
    end_time = time.perf_counter()
    average_time = (end_time - start_time) / iterations
    
    return result, average_time


if __name__ == "__main__":
    print("Python Implementation Performance Tests")
    print("=" * 50)
    
    # Test sum_of_squares
    print("\n1. Sum of Squares (n=100000)")
    result, time_taken = benchmark_function(sum_of_squares, 100000)
    print(f"Result: {result}")
    print(f"Time: {time_taken:.6f} seconds")
    
    # Test fibonacci (smaller number due to exponential complexity)
    print("\n2. Fibonacci Recursive (n=35)")
    result, time_taken = benchmark_function(fibonacci_recursive, 35)
    print(f"Result: {result}")
    print(f"Time: {time_taken:.6f} seconds")
    
    # Test prime counting
    print("\n3. Prime Count (limit=10000)")
    result, time_taken = benchmark_function(prime_count, 10000)
    print(f"Result: {result}")
    print(f"Time: {time_taken:.6f} seconds")
    
    # Test matrix multiplication
    print("\n4. Matrix Multiplication (100x100)")
    result, time_taken = benchmark_function(matrix_multiplication, 100)
    print(f"Result: First element = {result[0][0]}")
    print(f"Time: {time_taken:.6f} seconds")