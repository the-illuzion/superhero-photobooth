# 🦸 Superhero Photo Booth

Transform yourself into your favorite superhero using AI face swapping!

## ✨ Features

- 📸 Take photos with webcam or upload images
- 🎭 Choose from multiple superhero characters
- 🤖 AI-powered face swapping using FaceFusion (100% local, no API required!)
- ⚡ Fast processing (runs locally on your machine)
- 💾 Download your superhero transformation
- 🔒 Privacy-focused (no cloud processing)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the App

```bash
# From project root
./start.sh
```

This will start:
- Backend on http://localhost:8000
- Frontend on http://localhost:3000

### 3. Use the App

1. Open http://localhost:3000/booth
2. Take a photo or upload one
3. Choose a superhero character
4. Click "Transform Me!"
5. Download your result!

## 📁 Project Structure

```
superhero-photobooth/
├── backend/              # FastAPI backend
│   ├── api.py           # Main API server
│   ├── facefusion/      # FaceFusion library
│   ├── facefusion.py    # FaceFusion CLI
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

# Run
python api.py
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

**100% FREE!** Runs entirely on your local machine - no API costs, no cloud processing.

## 🔧 How It Works

1. **Frontend** (Next.js):
   - Captures user photo via webcam or file upload
   - User selects superhero character
   - Sends both images to backend

2. **Backend** (FastAPI):
   - Receives user photo + character image
   - Saves images to temporary files
   - Calls FaceFusion CLI for face swapping
   - Returns swapped image

3. **FaceFusion**:
   - Local AI model (no internet required)
   - Swaps user's face onto character body
   - High-quality results using state-of-the-art algorithms

## 🐛 Troubleshooting

### "Backend not responding"
- Make sure backend is running: `cd backend && python api.py`
- Check http://localhost:8000 shows "Backend is running!"

### "Face swap failed"
- First run downloads AI models (may take 5-10 minutes)
- Check backend logs for details
- Ensure enough disk space (~2GB for models)

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
- **AI**: FaceFusion (local face swap engine)
- **Camera**: react-webcam

## 📜 License

MIT License - Feel free to use this for your projects!

## 🙏 Credits

- Face swap engine: [FaceFusion](https://github.com/facefusion/facefusion)
- Built with ❤️ using FastAPI and Next.js

---

**Ready to become a superhero?** 🦸‍♂️🦸‍♀️

Run `./start.sh` and visit http://localhost:3000/booth
