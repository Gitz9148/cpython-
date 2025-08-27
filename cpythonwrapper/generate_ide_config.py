#!/usr/bin/env python3
"""
Generate compile_commands.json for better IDE integration.
This script creates a compile commands database that helps IDEs and language servers
understand how to compile the C++ files with the correct include paths.
"""

import json
import sys
import os
import subprocess
from pathlib import Path

def get_python_info():
    """Get Python and pybind11 include paths."""
    try:
        # Get Python include path
        python_include = subprocess.check_output([
            sys.executable, '-c', 
            'import sysconfig; print(sysconfig.get_path("include"))'
        ]).decode().strip()
        
        # Get pybind11 include path
        try:
            pybind11_include = subprocess.check_output([
                sys.executable, '-c',
                'import pybind11; print(pybind11.get_include())'
            ]).decode().strip()
        except:
            # Fallback for virtual environment
            import site
            site_packages = site.getsitepackages()[0] if site.getsitepackages() else ""
            if not site_packages and hasattr(site, 'USER_SITE'):
                site_packages = site.USER_SITE
            if not site_packages:
                # Try virtual environment
                venv_path = Path(sys.executable).parent.parent
                site_packages = venv_path / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
            
            pybind11_include = str(Path(site_packages) / "pybind11" / "include")
        
        return python_include, pybind11_include
    except Exception as e:
        print(f"Error getting Python info: {e}")
        return None, None

def generate_compile_commands():
    """Generate compile_commands.json file."""
    python_include, pybind11_include = get_python_info()
    
    if not python_include or not pybind11_include:
        print("Could not determine include paths. Make sure pybind11 is installed.")
        return False
    
    # Base compiler flags
    base_flags = [
        "clang++",
        "-std=c++14",
        "-fPIC",
        "-O3",
        "-Wall",
        "-DVERSION_INFO=\\\"dev\\\"",
        f"-I{pybind11_include}",
        f"-I{python_include}",
        "-c"
    ]
    
    # Files to compile
    files = [
        {
            "file": "pybind_wrapper.cpp",
            "flags": base_flags + ["pybind_wrapper.cpp"]
        },
        {
            "file": "cpp_functions.cpp", 
            "flags": base_flags + ["cpp_functions.cpp"]
        }
    ]
    
    # Generate compile commands
    compile_commands = []
    project_dir = os.getcwd()
    
    for file_info in files:
        command = {
            "directory": project_dir,
            "command": " ".join(file_info["flags"]),
            "file": file_info["file"]
        }
        compile_commands.append(command)
    
    # Write to file
    with open("compile_commands.json", "w") as f:
        json.dump(compile_commands, f, indent=2)
    
    print("✓ Generated compile_commands.json")
    print(f"  Python include: {python_include}")
    print(f"  pybind11 include: {pybind11_include}")
    return True

def generate_clangd_config():
    """Generate .clangd configuration file."""
    python_include, pybind11_include = get_python_info()
    
    if not python_include or not pybind11_include:
        return False
    
    config = f"""CompileFlags:
  Add:
    - -I{pybind11_include}
    - -I{python_include}
    - -DVERSION_INFO="dev"
    - -std=c++14
  Remove:
    - -mmacosx-version-min=*
    - -arch

Diagnostics:
  UnusedIncludes: Strict
  MissingIncludes: Strict

Index:
  Background: Build
"""
    
    with open(".clangd", "w") as f:
        f.write(config)
    
    print("✓ Generated .clangd configuration")
    return True

def main():
    """Main function."""
    print("Generating IDE configuration files...")
    
    success1 = generate_compile_commands()
    success2 = generate_clangd_config()
    
    if success1 and success2:
        print("\n✓ IDE configuration complete!")
        print("\nNext steps:")
        print("1. Restart your IDE/editor")
        print("2. Make sure clangd language server is enabled")
        print("3. The C++ errors should disappear")
        print("\nNote: If you're using VS Code, install the 'clangd' extension")
    else:
        print("\n✗ Failed to generate configuration files")

if __name__ == "__main__":
    main()