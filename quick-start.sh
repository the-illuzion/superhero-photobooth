#!/bin/bash

echo "🚀 Quick Start - Superhero Photo Booth"
echo "======================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check Node
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    exit 1
fi

echo "✓ Python and Node.js found"
echo ""

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
pip3 install -q fastapi uvicorn python-multipart Pillow 2>/dev/null || {
    echo "Installing with user flag..."
    pip3 install --user fastapi uvicorn python-multipart Pillow
}
cd ..

# Generate character images
echo "🎨 Creating character images..."
python3 backend/ai/simple_morph.py

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend
npm install --silent 2>/dev/null

echo ""
echo "✅ Setup complete!"
echo ""
echo "📖 To start the application:"
echo "   1. Terminal 1: cd backend && python3 main.py"
echo "   2. Terminal 2: cd frontend && npm run dev"
echo "   3. Open http://localhost:3000"
echo ""
