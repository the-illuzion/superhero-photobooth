# 🦸 Superhero Photo Booth

Transform yourself into your favorite superhero using AI face swapping!

## ✨ Features

- 📸 Take photos with webcam or upload images
- 🎭 Choose from multiple superhero characters
- 🤖 AI-powered face swapping using Replicate API
- ⚡ Fast processing (~3-5 seconds)
- 💾 Download your superhero transformation

## 🚀 Quick Start

### 1. Get Replicate API Token (FREE)

1. Go to https://replicate.com/account/api-tokens
2. Sign up (free $5 credit = ~1000 face swaps)
3. Copy your API token (starts with `r8_`)

### 2. Setup

```bash
# Edit backend/.env
nano backend/.env

# Replace 'your_token_here' with your actual token:
REPLICATE_API_TOKEN=r8_your_actual_token_here
```

### 3. Start the App

```bash
./start.sh
```

This will start:
- Backend on http://localhost:8000
- Frontend on http://localhost:3000

### 4. Use the App

1. Open http://localhost:3000/booth
2. Take a photo or upload one
3. Choose a superhero character
4. Click "Transform Me!"
5. Download your result!

## 📁 Project Structure

```
superhero-photobooth/
├── backend/              # FastAPI backend
│   ├── main.py          # Main API server
│   ├── .env             # Your API token (edit this!)
│   └── requirements.txt # Python dependencies
├── frontend/            # Next.js frontend
│   ├── app/
│   │   └── booth/page.tsx  # Main photo booth UI
│   └── public/
│       └── characters/     # Superhero images
└── start.sh            # One-command startup script
```

## 🛠️ Manual Setup

### Backend

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set your token in .env
echo "REPLICATE_API_TOKEN=r8_your_token" > .env

# Run
python main.py
```

### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run
npm run dev
```

## 🎨 Adding More Characters

1. Add superhero image to `public/characters/yourcharacter.jpg`
2. Edit `frontend/app/booth/page.tsx`:

```typescript
const CHARACTERS = [
  { id: 'ironman', name: 'Iron Man', image: '/characters/ironman.jpg' },
  { id: 'yourcharacter', name: 'Your Character', image: '/characters/yourcharacter.jpg' },
  // ... more characters
]
```

## 💰 Pricing

- **FREE**: $5 credit (~1000 images)
- **After**: $0.005 per image (half a cent!)

## 🔧 How It Works

1. **Frontend** (Next.js):
   - Captures user photo via webcam or file upload
   - User selects superhero character
   - Sends both images to backend

2. **Backend** (FastAPI):
   - Receives user photo + character image
   - Converts to base64 data URIs
   - Calls Replicate face swap API
   - Returns swapped image

3. **Replicate API**:
   - Uses `yan-ops/face_swap` model
   - Swaps user's face onto character body
   - Returns high-quality result

## 🐛 Troubleshooting

### "Backend not responding"
- Make sure backend is running: `cd backend && python main.py`
- Check http://localhost:8000 shows "Backend is running!"

### "Token error"
- Edit `backend/.env`
- Make sure token starts with `r8_`
- Get new token from https://replicate.com/account/api-tokens

### "Module not found"
```bash
cd backend
pip install -r requirements.txt
```

### "Frontend won't start"
```bash
cd frontend
npm install
npm run dev
```

## 📝 API Documentation

### POST /morph

Swap face from user image onto character image.

**Request:**
```
POST http://localhost:8000/morph
Content-Type: multipart/form-data

user_image: <image file>
character_image: <image file>
```

**Response:**
```json
{
  "success": true,
  "image": "data:image/png;base64,..."
}
```

### GET /

Health check endpoint.

**Response:**
```json
{
  "status": "Backend is running!"
}
```

## 🎯 Tech Stack

- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **Backend**: FastAPI (Python)
- **AI**: Replicate API (face swap model)
- **Camera**: react-webcam

## 📜 License

MIT License - Feel free to use this for your projects!

## 🙏 Credits

- Face swap model: [yan-ops/face_swap on Replicate](https://replicate.com/yan-ops/face_swap)
- Built with ❤️ using FastAPI and Next.js

---

**Ready to become a superhero?** 🦸‍♂️🦸‍♀️

Run `./start.sh` and visit http://localhost:3000/booth
