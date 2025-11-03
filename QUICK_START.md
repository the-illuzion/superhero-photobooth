# Quick Reference Card 🚀

## Installation (2 Commands)
```bash
# 1. Backend
cd backend && pip install -r requirements.txt

# 2. Frontend  
cd ../frontend && npm install

# 3. Done! ✅
```

## Running (One Command)
```bash
# From project root
./start.sh
```

Or manually (2 terminals):
```bash
# Terminal 1
cd backend && python api.py

# Terminal 2
cd frontend && npm run dev
```

## URLs
- **App:** http://localhost:3000/booth
- **API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## Key Files
```
frontend/app/booth/page.tsx  → Main UI
backend/api.py               → API endpoints
backend/facefusion/          → Face swapping engine
```

## Customization

### Add More Characters
1. Add image to `public/characters/{name}.jpg`
2. Update `CHARACTERS` array in `frontend/app/booth/page.tsx`

### Change Styling
- Edit `frontend/app/globals.css`
- Modify Tailwind classes in components

## Common Issues

**ModuleNotFoundError**
```bash
cd backend && pip install -r requirements.txt
```

**Port in use**
- Backend: Edit last line in `backend/api.py`
- Frontend: Next.js auto-increments port

**Webcam doesn't work**
- Use "Upload Photo" instead
- Check browser camera permissions

**First run is slow**
- FaceFusion downloads AI models on first use (~2GB)
- Wait 5-10 minutes for initial setup
- Subsequent runs will be fast

## Features
✅ Webcam + Upload  
✅ Multiple Characters  
✅ Download Result  
✅ Retake/Try Another  
✅ Responsive UI  
✅ 100% Local Processing (No API costs!)

**Have fun! 🦸‍♂️**
