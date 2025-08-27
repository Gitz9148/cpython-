# Makefile for Python + C++ Performance Wrapper Project

# Variables
PYTHON = python3
VENV_DIR = venv
PIP = $(VENV_DIR)/bin/pip
PYTHON_VENV = $(VENV_DIR)/bin/python

# Default target
.PHONY: all
all: setup build test

# Create virtual environment
.PHONY: venv
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)/"

# Install dependencies
.PHONY: install
install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Dependencies installed successfully!"

# Setup: create venv and install dependencies
.PHONY: setup
setup: install

# Build the C++ extension
.PHONY: build
build:
	@echo "Building C++ extension..."
	$(PYTHON_VENV) setup.py build_ext --inplace
	@echo "C++ extension built successfully!"

# Clean build artifacts
.PHONY: clean
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf __pycache__/
	rm -f cpp_accelerated.*.so
	@echo "Clean complete!"

# Full clean including virtual environment
.PHONY: clean-all
clean-all: clean
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)/
	@echo "Full clean complete!"

# Rebuild: clean and build
.PHONY: rebuild
rebuild: clean build

# Test the installation
.PHONY: test
test:
	@echo "Running quick test..."
	$(PYTHON_VENV) performance_benchmark.py --quick

# Run performance benchmark
.PHONY: benchmark
benchmark:
	@echo "Running full performance benchmark..."
	$(PYTHON_VENV) performance_benchmark.py

# Run interactive demo
.PHONY: demo
demo:
	@echo "Starting interactive demo..."
	$(PYTHON_VENV) demo.py

# Run Python-only tests
.PHONY: test-python
test-python:
	@echo "Running Python implementation tests..."
	$(PYTHON_VENV) python_implementation.py

# Check if C++ extension is working
.PHONY: check
check:
	@echo "Checking C++ extension..."
	@$(PYTHON_VENV) -c "import cpp_accelerated; print('✓ C++ extension is working!')" || echo "✗ C++ extension not available"

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  setup       - Create venv and install dependencies"
	@echo "  build       - Build the C++ extension"
	@echo "  test        - Run quick functionality test"
	@echo "  benchmark   - Run full performance comparison"
	@echo "  demo        - Run interactive demo"
	@echo "  check       - Check if C++ extension is working"
	@echo "  clean       - Clean build artifacts"
	@echo "  clean-all   - Clean everything including venv"
	@echo "  rebuild     - Clean and rebuild"
	@echo "  help        - Show this help message"
	@echo ""
	@echo "Quick start:"
	@echo "  make setup"
	@echo "  make build"
	@echo "  make test"