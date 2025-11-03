#!/bin/bash

echo "🚀 Setting up Superhero Photo Booth..."

# Check for uv, install if needed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv (modern Python package manager)..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Setup backend
echo "🐍 Installing backend dependencies with uv..."
cd backend
uv pip install fastapi uvicorn python-multipart Pillow --system

# Create character images
echo "🎨 Creating dummy character images..."
python3 ai/simple_morph.py

# Setup frontend
echo "📦 Installing frontend dependencies..."
cd ../frontend
npm install

echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "1. Terminal 1: cd backend && python3 main.py"
echo "2. Terminal 2: cd frontend && npm run dev"
echo "3. Open http://localhost:3000 in your browser"

