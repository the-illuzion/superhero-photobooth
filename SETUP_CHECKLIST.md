# ✅ Replicate Setup Checklist

Use this checklist to get your superhero photobooth running!

## 📋 Pre-Setup

- [ ] Project is cloned to your computer
- [ ] Python 3.9+ is installed (`python --version`)
- [ ] Node.js 18+ is installed (`node --version`)
- [ ] You have internet connection

## 🔑 Step 1: Get Replicate Token (2 minutes)

- [ ] Go to https://replicate.com/
- [ ] Sign up with GitHub or email (free account)
- [ ] Navigate to https://replicate.com/account/api-tokens
- [ ] Click "New token"
- [ ] Copy token (starts with `r8_...`)
- [ ] Save it somewhere safe (you'll need it next)

**Your token:** `r8_________________________________`

## ⚙️ Step 2: Configure Environment (1 minute)

Choose ONE option:

### Option A: Quick Test (Session Only)
```bash
export REPLICATE_API_TOKEN="r8_your_token_here"
```
- [ ] Token set for this terminal session

### Option B: Automated Setup
```bash
cd backend
./setup_replicate.sh
```
- [ ] Setup script completed successfully
- [ ] Token saved to shell profile

### Option C: Manual .env File
```bash
cd backend
echo 'REPLICATE_API_TOKEN=r8_your_token_here' > .env
```
- [ ] .env file created in backend folder

## 📦 Step 3: Install Dependencies (2 minutes)

```bash
# Backend
cd backend
pip install replicate

# Frontend (if not done already)
cd ../frontend
npm install
```

- [ ] Replicate SDK installed
- [ ] Frontend dependencies installed

## 🧪 Step 4: Test Face Swap (Optional but Recommended)

```bash
cd backend

# Test with sample images
python ai/face_swap_replicate.py \
    path/to/your/selfie.jpg \
    public/characters/ironman.jpg
```

- [ ] Test completed successfully
- [ ] `test_output.png` looks good

**If test fails:**
- Check token is set: `echo $REPLICATE_API_TOKEN`
- Check internet connection
- See troubleshooting in `REPLICATE_SETUP.md`

## 🚀 Step 5: Start the Application

```bash
# From project root
./start.sh

# Or manually:
# Terminal 1:
cd backend && python main.py

# Terminal 2:
cd frontend && npm run dev
```

- [ ] Backend started (http://localhost:8000)
- [ ] Frontend started (http://localhost:3000)
- [ ] No errors in console

## ✅ Step 6: Verify Everything Works

1. Open http://localhost:3000
   - [ ] Page loads successfully

2. Allow camera access
   - [ ] Camera permission granted
   - [ ] Camera feed visible

3. Take a photo
   - [ ] Photo captured successfully
   - [ ] Preview shows

4. Select a superhero character
   - [ ] Character selection works

5. Click "Morph"
   - [ ] Processing starts
   - [ ] Result appears (might take 3-5 seconds)
   - [ ] Face swap looks good!

6. Download photo
   - [ ] Download works
   - [ ] Image saved successfully

## 🎉 Success!

If all boxes are checked, you're ready to use your superhero photobooth!

---

## ❌ Troubleshooting

### Issue: Backend won't start

**Check:**
- [ ] Token is set: `echo $REPLICATE_API_TOKEN`
- [ ] Port 8000 is free: `lsof -i :8000`
- [ ] Python packages installed: `pip list | grep replicate`

**Solution:**
```bash
export REPLICATE_API_TOKEN="r8_your_token"
cd backend
python main.py
```

### Issue: Frontend shows "Connection refused"

**Check:**
- [ ] Backend is running at http://localhost:8000
- [ ] Visit http://localhost:8000 in browser (should show message)

### Issue: "REPLICATE_API_TOKEN not found"

**Solution:**
```bash
# Set it now:
export REPLICATE_API_TOKEN="r8_your_token_here"

# Restart backend
cd backend
python main.py
```

### Issue: Face swap returns blank image

**Check logs:**
```bash
tail -f backend/logs/*.log
```

**Common causes:**
- Token is invalid (check on Replicate website)
- No internet connection
- Image upload failed

**Solution:**
1. Verify token at https://replicate.com/account/api-tokens
2. Check internet: `curl https://replicate.com`
3. Check logs for specific error

### Issue: Face swap is slow (>30 seconds)

**This is normal for first request!** Replicate needs to "warm up" the model.
- First swap: 10-30 seconds
- Subsequent swaps: 3-5 seconds

**If still slow after first:**
- Check internet speed
- Try different time of day
- Check Replicate status: https://status.replicate.com

### Issue: Poor quality results

**Tips:**
- Use well-lit selfies
- Face should be centered and frontal
- Use high-resolution images
- Try different character images
- Ensure similar face sizes

---

## 📞 Need More Help?

1. **Check documentation:**
   - Quick start: `REPLICATE_QUICKSTART.md`
   - Detailed guide: `backend/REPLICATE_SETUP.md`
   - Summary: `IMPLEMENTATION_SUMMARY.md`

2. **Check logs:**
   ```bash
   tail -f backend/logs/*.log
   ```

3. **Replicate support:**
   - Docs: https://replicate.com/docs
   - Status: https://status.replicate.com
   - Discord: https://discord.gg/replicate

4. **Test components individually:**
   ```bash
   # Test API token
   python -c "import os; print('Token set!' if os.getenv('REPLICATE_API_TOKEN') else 'Token missing!')"
   
   # Test import
   python -c "import replicate; print('Replicate installed!')"
   
   # Test backend
   curl http://localhost:8000
   
   # Test frontend
   curl http://localhost:3000
   ```

---

## 🎯 Quick Reference

**Start app:**
```bash
./start.sh
```

**Set token:**
```bash
export REPLICATE_API_TOKEN="r8_your_token"
```

**Test face swap:**
```bash
cd backend
python ai/face_swap_replicate.py selfie.jpg character.jpg
```

**View logs:**
```bash
tail -f backend/logs/*.log
```

**Check status:**
```bash
# Backend
curl http://localhost:8000

# Frontend
curl http://localhost:3000
```

---

## ✅ Final Checklist

Before using at an event:

- [ ] Token is set and verified
- [ ] App starts without errors
- [ ] Camera works
- [ ] Face swap works and produces good results
- [ ] Download works
- [ ] Tested with multiple people
- [ ] Know how to check logs if issues arise
- [ ] Have backup plan (use simple mode if Replicate fails)

**You're all set! Go create some superhero photos! 🦸‍♂️🦸‍♀️**
