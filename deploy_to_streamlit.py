#!/usr/bin/env python3
"""
Deployment Helper Script for Streamlit Cloud
This script checks if your project is ready for deployment.
"""

import os
import sys
import yaml
from pathlib import Path

def check_deployment_readiness():
    """Check if the project is ready for Streamlit Cloud deployment."""
    print("🔍 Checking deployment readiness...")
    print("=" * 50)
    
    issues = []
    warnings = []
    
    # Check required files
    required_files = [
        "streamlit_app.py",
        "rag_chatbot.py", 
        "requirements.txt",
        "packages.txt",
        ".streamlit/config.toml"
    ]
    
    print("📁 Checking required files:")
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - MISSING")
            issues.append(f"Missing required file: {file_path}")
    
    # Check chunked documentation
    print("\n📚 Checking documentation chunks:")
    chunks_dir = "overview_docs_chunked"
    if os.path.exists(chunks_dir):
        chunk_files = [f for f in os.listdir(chunks_dir) if f.endswith('.md')]
        print(f"  ✅ Found {len(chunk_files)} chunk files")
        if len(chunk_files) == 0:
            warnings.append("No chunk files found in overview_docs_chunked/")
    else:
        print(f"  ❌ {chunks_dir} directory not found")
        issues.append(f"Missing documentation chunks directory: {chunks_dir}")
    
    # Check requirements.txt
    print("\n📦 Checking dependencies:")
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as f:
            requirements = f.read()
            if "streamlit" in requirements:
                print("  ✅ streamlit found in requirements.txt")
            else:
                issues.append("streamlit not found in requirements.txt")
            
            if "openai" in requirements:
                print("  ✅ openai found in requirements.txt")
            else:
                issues.append("openai not found in requirements.txt")
            
            if "chromadb" in requirements:
                print("  ✅ chromadb found in requirements.txt")
            else:
                issues.append("chromadb not found in requirements.txt")
    
    # Check .gitignore
    print("\n🔒 Checking .gitignore:")
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            gitignore_content = f.read()
            # Check if the directory is actually ignored (not just mentioned in comments)
            lines = gitignore_content.split('\n')
            is_ignored = any(line.strip() == "overview_docs_chunked/" for line in lines)
            if is_ignored:
                warnings.append("overview_docs_chunked/ is in .gitignore - needed for deployment")
            else:
                print("  ✅ overview_docs_chunked/ not ignored (good for deployment)")
    else:
        warnings.append(".gitignore file not found")
    
    # Check for environment variables
    print("\n🔑 Checking environment variables:")
    print("  ℹ️  You'll need to set OPENAI_API_KEY in Streamlit Cloud secrets")
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 DEPLOYMENT SUMMARY")
    print("=" * 50)
    
    if issues:
        print("❌ CRITICAL ISSUES (must fix before deployment):")
        for issue in issues:
            print(f"  • {issue}")
        print()
    
    if warnings:
        print("⚠️  WARNINGS (should address):")
        for warning in warnings:
            print(f"  • {warning}")
        print()
    
    if not issues and not warnings:
        print("✅ All checks passed! Your project is ready for deployment.")
    elif not issues:
        print("✅ No critical issues found. You can proceed with deployment.")
    else:
        print("❌ Please fix the critical issues before deploying.")
    
    print("\n🚀 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Go to share.streamlit.io")
    print("3. Connect your repository")
    print("4. Set OPENAI_API_KEY in secrets")
    print("5. Deploy!")
    
    return len(issues) == 0

if __name__ == "__main__":
    success = check_deployment_readiness()
    sys.exit(0 if success else 1) 