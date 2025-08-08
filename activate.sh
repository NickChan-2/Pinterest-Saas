#!/bin/bash

# Activation script for Pinterest SaaS project
echo "🚀 Activating Pinterest SaaS virtual environment..."

# Activate the virtual environment
source .venv/bin/activate

echo "✅ Virtual environment activated!"
echo "📦 Python version: $(python --version)"
echo "📍 Python path: $(which python)"
echo ""
echo "💡 To deactivate, run: deactivate"
echo "📚 To run scripts, use: python scripts/script_name.py"
echo ""
echo "📋 Available scripts:"
echo "  - scripts/product_scraper.py"
echo "  - scripts/gpt_generator.py"
echo "  - scripts/image_creator.py"
echo "  - scripts/affiliate_linker.py"
echo ""
echo "🔧 Don't forget to update your .env file with your API keys!"
