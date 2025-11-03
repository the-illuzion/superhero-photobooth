#!/usr/bin/env python3
"""
FastAPI wrapper for FaceFusion face swapping
Uses FaceFusion's CLI to perform face swaps
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import subprocess
import base64
import tempfile
import os
import shutil
from pathlib import Path

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BACKEND_DIR = Path(__file__).parent
TEMP_DIR = BACKEND_DIR / "temp"
OUTPUT_DIR = BACKEND_DIR / "output"

# Create directories
TEMP_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.get("/")
async def health_check():
    return {"status": "ok", "message": "FaceFusion API is running"}

@app.post("/morph")
async def morph_image(
    user_image: UploadFile = File(...),
    character_image: UploadFile = File(...)
):
    """
    Swap user's face onto character image using FaceFusion
    """
    source_path = None
    target_path = None
    output_path = None
    
    try:
        print("🔄 Received morph request")
        
        # Save uploaded files temporarily
        source_path = TEMP_DIR / f"source_{user_image.filename}"
        target_path = TEMP_DIR / f"target_{character_image.filename}"
        output_path = OUTPUT_DIR / f"result_{user_image.filename}"
        
        print(f"💾 Saving source to {source_path}")
        with open(source_path, "wb") as f:
            content = await user_image.read()
            f.write(content)
            print(f"📊 Source size: {len(content)} bytes")
        
        print(f"💾 Saving target to {target_path}")
        with open(target_path, "wb") as f:
            content = await character_image.read()
            f.write(content)
            print(f"📊 Target size: {len(content)} bytes")
        
        # Run FaceFusion CLI with hyperswap-1c
        print("🤖 Running FaceFusion with hyperswap-1c...")
        cmd = [
            "python", "facefusion.py",
            "headless-run",
            "--source", str(source_path),
            "--target", str(target_path),
            "--output-path", str(output_path),
            "--processors", "face_swapper",
            "--execution-providers", "cpu"
        ]
        
        print(f"🚀 Command: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            cwd=BACKEND_DIR,
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode != 0:
            print(f"❌ FaceFusion failed with code {result.returncode}")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            raise HTTPException(
                status_code=500,
                detail=f"FaceFusion failed: {result.stderr}"
            )
        
        print("✅ FaceFusion completed successfully")
        
        # Read the output image
        if not output_path.exists():
            raise HTTPException(
                status_code=500,
                detail="Output file not created"
            )
        
        with open(output_path, "rb") as f:
            result_bytes = f.read()
        
        print(f"📤 Sending result ({len(result_bytes)} bytes)")
        
        # Encode as base64
        result_b64 = base64.b64encode(result_bytes).decode('utf-8')
        
        return JSONResponse({
            "success": True,
            "image": f"data:image/png;base64,{result_b64}"
        })
        
    except subprocess.TimeoutExpired:
        print("❌ FaceFusion timeout")
        raise HTTPException(status_code=500, detail="Processing timeout")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup temp files
        for path in [source_path, target_path, output_path]:
            if path and path.exists():
                try:
                    path.unlink()
                except:
                    pass

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FaceFusion API server...")
    print(f"📁 Backend dir: {BACKEND_DIR}")
    print(f"📁 Temp dir: {TEMP_DIR}")
    print(f"📁 Output dir: {OUTPUT_DIR}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
