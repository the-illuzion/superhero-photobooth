# Quick Reference Card 🚀

## Installation (3 Commands)
```bash
# 1. Backend (using uv - faster and more reliable)
cd backend && uv pip install fastapi uvicorn python-multipart Pillow --system && python3 ai/simple_morph.py

# 2. Frontend  
cd ../frontend && npm install

# 3. Done! ✅
```

## Running (2 Terminals)
```bash
# Terminal 1
cd backend && python3 main.py

# Terminal 2
cd frontend && npm run dev
```

## URLs
- **App:** http://localhost:3000
- **API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## Key Files
```
frontend/app/booth/page.tsx  → Main UI
backend/main.py              → API endpoints
backend/ai/simple_morph.py   → Face blending
```

## Customization

### Add More Characters
1. Add image to `public/characters/{name}.jpg`
2. Update `CHARACTERS` array in `frontend/app/booth/page.tsx`

### Change Styling
- Edit `frontend/app/globals.css`
- Modify Tailwind classes in components

### Improve Face Swapping
```bash
pip install opencv-python numpy
# Backend will auto-use face_swap.py
```

## Common Issues

**ModuleNotFoundError: PIL**
```bash
pip3 install --user Pillow
```

**Port in use**
- Backend: Edit last line in `backend/main.py`
- Frontend: Next.js auto-increments port

**Webcam doesn't work**
- Use "Upload Photo" instead
- Check browser camera permissions

## Features
✅ Webcam + Upload  
✅ 4 Characters  
✅ Download Result  
✅ Retake/Try Another  
✅ Responsive UI  

**Have fun! 🦸‍♂️**
