#!/bin/bash

echo "🚀 Starting Superhero Photobooth..."
echo ""

# Check if .env file exists
if [ ! -f backend/.env ]; then
    echo "⚠️  Warning: backend/.env file not found!"
    echo "Creating template .env file..."
    echo "REPLICATE_API_TOKEN=your_token_here" > backend/.env
    echo ""
    echo "📝 Please edit backend/.env and add your Replicate API token"
    echo "Get token from: https://replicate.com/account/api-tokens"
    echo ""
fi

# Check if token is set
if grep -q "your_token_here" backend/.env; then
    echo "❌ REPLICATE_API_TOKEN not set in backend/.env"
    echo ""
    echo "To fix:"
    echo "1. Get token from: https://replicate.com/account/api-tokens"
    echo "2. Edit backend/.env"
    echo "3. Replace 'your_token_here' with your actual token"
    echo ""
    read -p "Press Enter to continue anyway (will run in test mode)..."
    echo ""
fi

# Start backend
echo "🔧 Starting backend on http://localhost:8000..."
cd backend
python main.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo "🎨 Starting frontend on http://localhost:3000..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Both servers started!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Wait for Ctrl+C
trap "echo ''; echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait
