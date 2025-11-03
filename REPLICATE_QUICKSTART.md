# 🎭 Replicate Face Swap - QUICK START

## ⚡ 5-Minute Setup

### 1️⃣ Get Your Free API Token

👉 **Go to: https://replicate.com/account/api-tokens**

- Sign up with GitHub (takes 30 seconds)
- Click "New token"
- Copy your token (starts with `r8_...`)

**Free tier includes $5 credit = ~1000 face swaps!** 🎉

---

### 2️⃣ Set the Token

**Quick way (this session only):**

```bash
export REPLICATE_API_TOKEN="r8_paste_your_token_here"
```

**Or run the setup script:**

```bash
cd backend
./setup_replicate.sh
```

---

### 3️⃣ Start the App

```bash
# From project root
./start.sh
```

That's it! Open http://localhost:3000 🚀

---

## 🧪 Test It First

Want to test before starting the full app?

```bash
cd backend

# Test with your own images
python ai/face_swap_replicate.py my_selfie.jpg public/characters/ironman.jpg

# Check the output: test_output.png
```

---

## ❓ Troubleshooting

### "REPLICATE_API_TOKEN not found"

```bash
# Set it in your terminal:
export REPLICATE_API_TOKEN="r8_your_token_here"

# Or add to .env file:
echo 'REPLICATE_API_TOKEN=r8_your_token_here' > backend/.env
```

### "Module 'replicate' not found"

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org replicate
```

### "SSL Certificate Error"

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade replicate
```

---

## 💰 Pricing

- **Free tier:** $5 credit (~1000 images)
- **After free credit:** $0.005 per image
- **Example:** 200-photo event = $1.00

**No subscription needed!** Pay only for what you use.

---

## 🎯 How It Works

1. **You:** Take a selfie in the app
2. **Replicate:** Swaps your face onto Iron Man's body (3-5 seconds)
3. **You:** Download your superhero photo!

**Quality:** ⭐⭐⭐⭐⭐ (Best available for face swapping)

---

## 📚 Full Documentation

- **Detailed setup:** `REPLICATE_SETUP.md`
- **API docs:** https://replicate.com/docs
- **Model we use:** https://replicate.com/yan-ops/faceswap

---

## ✅ Checklist

- [ ] Created Replicate account
- [ ] Got API token from https://replicate.com/account/api-tokens
- [ ] Set `REPLICATE_API_TOKEN` environment variable
- [ ] Installed replicate: `pip install replicate`
- [ ] Tested with `python ai/face_swap_replicate.py ...`
- [ ] Started the app with `./start.sh`
- [ ] Took a superhero photo! 📸

---

## 🚀 Ready to Go!

```bash
export REPLICATE_API_TOKEN="r8_your_token_here"
./start.sh
```

**Open http://localhost:3000 and become a superhero!** 🦸‍♂️🦸‍♀️

---

**Questions?** Check the logs in `backend/logs/` or see `REPLICATE_SETUP.md` for detailed help.
