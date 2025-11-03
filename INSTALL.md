# Superhero Photo Booth - Installation Guide

## Quick Setup (Manual)

### 1. Install Backend Dependencies

**Using uv (recommended - faster and more reliable):**
```bash
cd backend
uv pip install fastapi uvicorn python-multipart Pillow --system
```

**Or using pip3:**
```bash
cd backend
pip3 install fastapi uvicorn python-multipart Pillow
```

If you get errors, try:
```bash
pip3 install --user --upgrade pip
pip3 install --user fastapi uvicorn python-multipart Pillow
```

**Note:** If you don't have `uv` installed, you can install it with:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Generate Character Images

```bash
python3 ai/simple_morph.py
```

### 3. Install Frontend Dependencies

```bash
cd ../frontend  
npm install
```

### 4. Start the Application

**Terminal 1 - Backend:**
```bash
cd backend
python3 main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### 5. Open Your Browser

Navigate to: **http://localhost:3000**

---

## Optional: Advanced Face Swapping

For better results, install OpenCV:

```bash
pip3 install opencv-python numpy
```

Then the app will automatically use advanced face detection and blending.

---

## Troubleshooting

### "Module not found" errors
- Make sure pip packages are installed in the correct Python environment
- Try `python3 -m pip install <package>` instead

### Port already in use
- Backend: Change port in `backend/main.py` (last line)
- Frontend: Next.js will auto-increment to 3001, 3002, etc.

### Webcam not working
- Use the "Upload Photo" option instead
- Check browser permissions for camera access

---

## What's Included

✅ Next.js 14 frontend with TypeScript  
✅ FastAPI backend with Python  
✅ Webcam capture + file upload  
✅ 4 superhero character options  
✅ Simple face morphing algorithm  
✅ Download transformed images  
✅ Responsive, beautiful UI  

Enjoy your superhero transformations! 🦸‍♂️🦸‍♀️
