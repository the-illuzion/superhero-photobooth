# 🚀 START HERE - Superhero Photobooth with Replicate

**Welcome!** This guide will get you up and running in **5 minutes**.

---

## 📋 What You Need

1. ✅ This project (already cloned!)
2. ✅ Python 3.9+ installed
3. ✅ Node.js 18+ installed
4. ✅ Internet connection
5. ⭐ **FREE Replicate account** (we'll get this now!)

---

## 🎯 3-Step Quick Start

### 1️⃣ Get Your Free API Token (2 minutes)

👉 **https://replicate.com/account/api-tokens**

1. Sign up with GitHub (30 seconds)
2. Click "New token"
3. Copy your token (starts with `r8_...`)

**You get $5 FREE credit = ~1000 face swaps!** 🎉

---

### 2️⃣ Set Your Token (30 seconds)

**Option A: Using .env file (Recommended)**

```bash
cd backend
nano .env  # or use any text editor
# Change "your_token_here" to your actual token
# Save and exit (Ctrl+X, then Y, then Enter in nano)
```

**Option B: Environment variable (Session only)**

```bash
export REPLICATE_API_TOKEN="r8_paste_your_token_here"
```

That's it! ✅

---

### 3️⃣ Start the App (1 minute)

```bash
./start.sh
```

Then open: **http://localhost:3000** 🎉

---

## 🎨 How It Works

1. **Take a selfie** with your webcam
2. **Choose a superhero** (Iron Man, Wonder Woman, etc.)
3. **Click "Morph"** - AI swaps your face onto the superhero! (3-5 sec)
4. **Download** your superhero photo! 📸

---

## 📚 Documentation

- **This file** - Quick start (you are here!)
- `SETUP_CHECKLIST.md` - Step-by-step checklist
- `REPLICATE_QUICKSTART.md` - 5-minute guide
- `backend/REPLICATE_SETUP.md` - Detailed setup
- `IMPLEMENTATION_SUMMARY.md` - Technical details

---

## 🧪 Test Face Swap First (Optional)

Want to test before running the full app?

```bash
cd backend
python ai/face_swap_replicate.py your_photo.jpg public/characters/ironman.jpg
# Check result: test_output.png
```

---

## ❓ Troubleshooting

### "REPLICATE_API_TOKEN not found"

```bash
export REPLICATE_API_TOKEN="r8_your_token_here"
```

### "Module 'replicate' not found"

```bash
cd backend
pip install replicate
```

### Backend/Frontend won't start

```bash
# Start manually
# Terminal 1:
cd backend && python main.py

# Terminal 2:
cd frontend && npm run dev
```

### More help needed?

See `SETUP_CHECKLIST.md` for detailed troubleshooting!

---

## 💰 Pricing

**Free tier:** $5 credit included  
**After that:** $0.005 per image (half a cent!)

**Examples:**
- 100 photos at a party = $0.50
- 1000 photos at a festival = $5.00

---

## ✨ What Makes This Special?

✅ **Professional AI face swapping** (not just overlay!)  
✅ **Fast** - 3-5 seconds per photo  
✅ **Super cheap** - $0.005 per image  
✅ **Easy setup** - 5 minutes total  
✅ **No GPU needed** - works on any computer  
✅ **High quality** - ⭐⭐⭐⭐⭐

---

## 🎯 Ready? Let's Go!

```bash
# 1. Get token from https://replicate.com/account/api-tokens

# 2. Set it
export REPLICATE_API_TOKEN="r8_your_token_here"

# 3. Start!
./start.sh

# 4. Open browser
# http://localhost:3000
```

---

## 🦸‍♂️ Have Fun!

Take amazing superhero photos and share them with friends!

**Questions?** Check the other docs or see the logs in `backend/logs/`

---

**🎉 Now go become a superhero! 🦸‍♀️**
