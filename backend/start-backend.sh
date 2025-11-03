#!/bin/bash

cd "$(dirname "$0")"

echo "🚀 Starting Superhero Photobooth Backend..."

# Activate virtual environment
source .venv/bin/activate

# Start the API server
python api.py
