#!/usr/bin/env python3
"""
Setup verification script for Storm Eowyn Forest Loss Analysis
Checks dependencies, configuration, and system requirements
"""

import sys
import os
import configparser
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    print("Checking Python version...")
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required")
        return False
    print(f"✅ Python {sys.version.split()[0]} OK")
    return True

def check_dependencies():
    """Check required Python packages"""
    print("\nChecking Python dependencies...")
    required_packages = [
        'snappy',
        'asf_search', 
        'geopandas',
        'pyarrow',
        'rasterio',
        'numpy',
        'pandas'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} OK")
        except ImportError:
            print(f"❌ {package} missing")
            missing.append(package)
    
    return len(missing) == 0

def check_snap():
    """Check SNAP installation and SNAPPY configuration"""
    print("\nChecking SNAP/SNAPPY...")
    try:
        import snappy
        print("✅ SNAPPY import OK")
        
        # Try to access SNAP operators
        from snappy import ProductIO
        print("✅ SNAP ProductIO OK")
        return True
    except Exception as e:
        print(f"❌ SNAP/SNAPPY error: {e}")
        return False

def check_config():
    """Check configuration file"""
    print("\nChecking configuration...")
    config_path = Path("config.ini")
    
    if not config_path.exists():
        print("❌ config.ini not found (copy from config.example.ini)")
        return False
    
    config = configparser.ConfigParser()
    config.read(config_path)
    
    required_sections = ['ASF', 'EARTHDATA', 'PROCESSING', 'IRELAND']
    missing_sections = []
    
    for section in required_sections:
        if section not in config:
            missing_sections.append(section)
        else:
            print(f"✅ [{section}] section OK")
    
    if missing_sections:
        print(f"❌ Missing config sections: {missing_sections}")
        return False
    
    return True

def check_directories():
    """Check required directories exist"""
    print("\nChecking directories...")
    required_dirs = [
        'data/input',
        'data/output', 
        'data/temp',
        'bin',
        'src',
        'docs',
        'tests'
    ]
    
    missing = []
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ {dir_path}/ OK")
        else:
            print(f"❌ {dir_path}/ missing")
            missing.append(dir_path)
    
    return len(missing) == 0

def main():
    """Run all setup checks"""
    print("Storm Eowyn Forest Loss Analysis - Setup Check")
    print("=" * 50)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_snap(),
        check_config(),
        check_directories()
    ]
    
    print("\n" + "=" * 50)
    if all(checks):
        print("✅ All checks passed! Setup is complete.")
        return 0
    else:
        print("❌ Some checks failed. Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
