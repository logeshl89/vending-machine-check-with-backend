#!/usr/bin/env python3
"""
Setup script for Raspberry Pi Status Dashboard deployment
This script helps prepare the application for deployment on Render
"""

import os
import sys

def check_files():
    """Check that all required files are present"""
    required_files = [
        'server.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'render.yaml'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("Missing required files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    print("All required files are present!")
    return True

def check_static_dir():
    """Check that static directory with index.html exists"""
    if not os.path.exists('static'):
        print("Missing static directory")
        return False
    
    if not os.path.exists('static/index.html'):
        print("Missing static/index.html")
        return False
    
    print("Static directory and index.html are present!")
    return True

def main():
    print("Raspberry Pi Status Dashboard - Deployment Setup Checker")
    print("=" * 50)
    
    # Check current directory
    print(f"Current directory: {os.getcwd()}")
    
    # Check required files
    files_ok = check_files()
    print()
    
    # Check static directory
    static_ok = check_static_dir()
    print()
    
    if files_ok and static_ok:
        print("✅ Your application is ready for deployment to Render!")
        print("\nNext steps:")
        print("1. Push this code to a GitHub repository")
        print("2. Create a new Web Service on Render")
        print("3. Connect your GitHub repository")
        print("4. Use the default build and start commands")
        print("5. Deploy!")
    else:
        print("❌ Some files are missing. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()