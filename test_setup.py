#!/usr/bin/env python3
"""
Test script to verify Pinterest SaaS environment setup
"""

import sys
import os
from dotenv import load_dotenv

def test_environment():
    """Test the Python environment and dependencies"""
    print("🧪 Testing Pinterest SaaS Environment...")
    print(f"📍 Python version: {sys.version}")
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Test core imports
    try:
        import requests
        import openai
        import pandas as pd
        import PIL
        from bs4 import BeautifulSoup
        import selenium
        print("✅ All core dependencies imported successfully!")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Test environment variables
    load_dotenv()
    openai_key = os.getenv('OPENAI_API_KEY')
    amazon_tag = os.getenv('AMAZON_ASSOCIATE_TAG')
    
    print(f"🔑 OpenAI API Key: {'✅ Set' if openai_key and openai_key != 'your_openai_key_here' else '❌ Not configured'}")
    print(f"🛒 Amazon Associate Tag: {'✅ Set' if amazon_tag and amazon_tag != 'yourtag-20' else '❌ Not configured'}")
    
    # Test data directory
    data_dir = 'data'
    if os.path.exists(data_dir):
        print(f"📂 Data directory: ✅ Exists")
        csv_file = os.path.join(data_dir, 'products.csv')
        if os.path.exists(csv_file):
            print(f"📄 Products CSV: ✅ Exists")
        else:
            print(f"📄 Products CSV: ❌ Not found")
    else:
        print(f"📂 Data directory: ❌ Not found")
    
    print("\n🎉 Environment test completed!")
    return True

if __name__ == "__main__":
    test_environment()
