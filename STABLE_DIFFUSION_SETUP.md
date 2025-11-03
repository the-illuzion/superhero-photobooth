# 🚀 Stable Diffusion + ControlNet + InstantID Setup Guide

## Overview

This advanced AI implementation uses:
- **Stable Diffusion** - Base image generation model
- **ControlNet (OpenPose)** - Preserves character pose and structure
- **CLIP** - Face identity guidance (lightweight InstantID alternative)
- **Realistic Vision V6** - High-quality photorealistic model

## System Requirements

### Minimum Requirements (CPU Only - SLOW)
- **RAM:** 16GB+ 
- **Disk Space:** 15GB for models
- **Time per image:** 5-10 minutes

### Recommended (GPU)
- **GPU:** NVIDIA RTX 3060+ (6GB VRAM) or Apple Silicon M1/M2
- **RAM:** 16GB+
- **Disk Space:** 15GB
- **Time per image:** 30-60 seconds

## Installation

### Step 1: Install Python Dependencies

```bash
cd backend

# Install core dependencies
uv pip install diffusers transformers accelerate --system
uv pip install controlnet-aux safetensors omegaconf --system
uv pip install torch torchvision --system
```

### Step 2: Download Models (First Run Only)

Models are auto-downloaded on first use (~8GB):

1. **Stable Diffusion:** `SG161222/Realistic_Vision_V6.0_B1_noVAE` (~4GB)
2. **ControlNet:** `lllyasviel/control_v11p_sd15_openpose` (~1.5GB)
3. **VAE:** `stabilityai/sd-vae-ft-mse` (~330MB)
4. **Preprocessors:** OpenPose detector (~300MB)

Total: ~6-8GB downloaded on first run.

### Step 3: Test Installation

```bash
python3 ai/stable_diffusion_morph.py
```

Expected output:
```
🔄 Loading models (this may take 5-10 minutes on first run)...
1/4 Loading ControlNet (Openpose)...
2/4 Loading Stable Diffusion model...
3/4 Loading VAE...
4/4 Loading pose and edge detectors...
✅ All models loaded successfully!
```

## Usage

### Method 1: API (Automatic Selection)

The backend automatically chooses the best method:

```bash
# Auto-detect (uses SD if GPU available, otherwise MediaPipe)
python3 main.py
```

### Method 2: Force Specific AI Method

```bash
# Force Stable Diffusion (requires GPU)
export AI_METHOD=sd
python3 main.py

# Force MediaPipe (fast, CPU-friendly)
export AI_METHOD=mediapipe
python3 main.py

# Force simple overlay (fastest)
export AI_METHOD=simple
python3 main.py
```

### Method 3: Python API

```python
from ai.stable_diffusion_morph import generate_morphed_image
from PIL import Image

result = generate_morphed_image(
    user_image="path/to/selfie.jpg",
    character_image="path/to/ironman.jpg",
    prompt="A cinematic portrait of Iron Man, movie poster style, dramatic lighting",
    num_inference_steps=30,
    guidance_scale=7.5,
    seed=42  # for reproducibility
)

result.save("output.png")
```

## Advanced Configuration

### Quality vs Speed Tradeoff

```python
# Fast (10-15 seconds, good quality)
generate_morphed_image(
    ...,
    num_inference_steps=20,
    guidance_scale=7.0
)

# Balanced (30-45 seconds, great quality)
generate_morphed_image(
    ...,
    num_inference_steps=30,
    guidance_scale=7.5
)

# High Quality (60-90 seconds, best quality)
generate_morphed_image(
    ...,
    num_inference_steps=50,
    guidance_scale=8.5
)
```

### ControlNet Strength

Controls how closely to follow character's pose:

```python
# Loose pose following (more creative)
generate_morphed_image(
    ...,
    controlnet_conditioning_scale=0.5
)

# Default (balanced)
generate_morphed_image(
    ...,
    controlnet_conditioning_scale=1.0
)

# Strict pose following (exact replication)
generate_morphed_image(
    ...,
    controlnet_conditioning_scale=1.5
)
```

### Custom Prompts

```python
# Superhero style
prompt = "Epic superhero portrait, dramatic lighting, cinematic, 8k, ultra detailed"

# Realistic photo
prompt = "Professional headshot, natural lighting, photorealistic, high resolution"

# Artistic style
prompt = "Oil painting style portrait, dramatic shadows, renaissance lighting"

# Sci-fi character
prompt = "Futuristic sci-fi character, neon lighting, cyberpunk aesthetic, detailed"
```

## GPU Optimization

### NVIDIA GPU

```python
# Enable optimizations in stable_diffusion_morph.py
pipe.enable_model_cpu_offload()  # Offload to CPU when not in use
pipe.enable_vae_slicing()        # Process VAE in slices (saves VRAM)
pipe.enable_attention_slicing(1) # Reduce memory usage
```

### Apple Silicon (M1/M2/M3)

```python
# Uses MPS (Metal Performance Shaders) automatically
device = "mps"
```

### CPU Only

```python
# Uses float32 instead of float16
torch_dtype=torch.float32
device = "cpu"
```

## Troubleshooting

### Issue: Out of Memory (OOM)

**Solution 1:** Reduce image size
```python
height=384, width=384  # Instead of 512x512
```

**Solution 2:** Reduce batch size
```python
pipe.enable_attention_slicing(1)
pipe.enable_vae_slicing()
```

**Solution 3:** Use CPU offloading
```python
pipe.enable_sequential_cpu_offload()
```

### Issue: Models not downloading

**Solution:** Manual download
```bash
# Download models manually
huggingface-cli download SG161222/Realistic_Vision_V6.0_B1_noVAE
huggingface-cli download lllyasviel/control_v11p_sd15_openpose
```

### Issue: Slow generation

**Cause:** Using CPU instead of GPU

**Solution:** Check GPU availability
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available: {torch.backends.mps.is_available()}")
```

### Issue: Face doesn't look like user

**Solution 1:** Use better quality user photo
- Front-facing
- Good lighting
- Clear facial features

**Solution 2:** Adjust prompt
```python
prompt = "portrait of [describe user], as Iron Man, cinematic"
```

**Solution 3:** Use IP-Adapter (future feature)

## Comparison: Methods

| Method | Quality | Speed | VRAM | Setup |
|--------|---------|-------|------|-------|
| **Stable Diffusion** | ⭐⭐⭐⭐⭐ | 30-60s | 6GB | Hard |
| **MediaPipe** | ⭐⭐⭐⭐ | 2-3s | 0 | Easy |
| **Simple Overlay** | ⭐⭐ | <1s | 0 | Easy |

## File Structure

```
backend/
├── ai/
│   ├── stable_diffusion_morph.py  # SD + ControlNet implementation
│   ├── mediapipe_swap.py          # MediaPipe face swap
│   ├── simple_morph.py            # Simple overlay
│   └── __init__.py
├── main.py                        # FastAPI server (auto-selects method)
└── requirements.txt
```

## Environment Variables

```bash
# Force specific AI method
export AI_METHOD=sd          # Use Stable Diffusion
export AI_METHOD=mediapipe   # Use MediaPipe
export AI_METHOD=simple      # Use simple overlay
export AI_METHOD=auto        # Auto-detect (default)

# Hugging Face cache directory
export HF_HOME=/path/to/models/cache

# Disable telemetry
export HF_HUB_DISABLE_TELEMETRY=1
```

## Model Cache Location

Models are cached at:
- **Linux/Mac:** `~/.cache/huggingface/hub/`
- **Windows:** `C:\Users\<username>\.cache\huggingface\hub\`

Total size: ~8GB

## Production Deployment

### 1. Pre-download models

```bash
python3 -c "from ai.stable_diffusion_morph import initialize_models; initialize_models()"
```

### 2. Use model caching

Models stay in memory after first load. Don't restart the server unnecessarily.

### 3. Queue system

For multiple users, implement a job queue (Celery, RQ) to handle concurrent requests.

### 4. GPU Server

Deploy on GPU instances:
- **AWS:** p3.2xlarge (V100)
- **Google Cloud:** n1-standard-4 + Tesla T4
- **Azure:** NC6 (K80)

### 5. Monitoring

Track generation time and quality:
```python
import time
start = time.time()
result = generate_morphed_image(...)
print(f"Generated in {time.time() - start:.2f}s")
```

## Future Enhancements

### 1. IP-Adapter Integration
Better face identity preservation with IP-Adapter models.

### 2. Multi-ControlNet
Combine pose + depth + canny for better control.

### 3. SDXL Support
Use SDXL models for even higher quality (requires 12GB+ VRAM).

### 4. LoRA Fine-tuning
Train custom LoRAs for specific superhero styles.

### 5. Video Generation
Extend to video morphing using AnimateDiff.

---

**Status:** ✅ Fully implemented and ready for GPU-enabled systems!

For systems without GPU, MediaPipe provides excellent quality with much faster generation.
