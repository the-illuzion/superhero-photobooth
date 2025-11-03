from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import base64
import os
import subprocess
import shutil
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = Path("temp")
OUTPUT_DIR = Path("output")
FACEFUSION_DIR = Path(".")

TEMP_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Superhero Photobooth Backend"}

@app.post("/morph")
async def morph_image(
    user_image: UploadFile = File(...),
    character_image: UploadFile = File(...)
):
    """Face swap using FaceFusion"""
    try:
        logger.info("🔄 Received morph request")
        
        # Save uploaded files
        user_path = TEMP_DIR / "source_user.jpg"
        character_path = TEMP_DIR / "target_character.jpg"
        output_path = OUTPUT_DIR / "result_user.jpg"
        
        logger.info("💾 Saving uploaded files...")
        with open(user_path, "wb") as f:
            content = await user_image.read()
            f.write(content)
            logger.info(f"📊 User image size: {len(content)} bytes")
        
        with open(character_path, "wb") as f:
            content = await character_image.read()
            f.write(content)
            logger.info(f"📊 Character image size: {len(content)} bytes")
        
        # Remove old output if exists
        if output_path.exists():
            output_path.unlink()
        
        # Build FaceFusion command - use face_swapper processor
        cmd = [
            ".venv/bin/python",
            "facefusion.py",
            "headless-run",
            "--source", str(user_path.absolute()),
            "--target", str(character_path.absolute()),
            "--output-path", str(output_path.absolute()),
            "--processors", "face_swapper",
            "--execution-providers", "cpu"
        ]
        
        logger.info(f"🚀 Command: {' '.join(cmd)}")
        
        # Run FaceFusion from its directory
        result = subprocess.run(
            cmd,
            cwd=FACEFUSION_DIR,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            logger.error(f"❌ FaceFusion error:\n{result.stderr}")
            logger.error(f"📋 Stdout:\n{result.stdout}")
            raise HTTPException(status_code=500, detail=f"FaceFusion failed: {result.stderr}")
        
        logger.info(f"✅ FaceFusion completed:\n{result.stdout}")
        
        # Check if output was created
        if not output_path.exists():
            logger.error("❌ Output file not created")
            raise HTTPException(status_code=500, detail="Output file not created")
        
        # Read and encode result
        with open(output_path, "rb") as f:
            result_bytes = f.read()
            result_b64 = base64.b64encode(result_bytes).decode('utf-8')
        
        logger.info(f"✅ Result size: {len(result_bytes)} bytes")
        
        return JSONResponse({
            "success": True,
            "image": f"data:image/jpeg;base64,{result_b64}"
        })
        
    except subprocess.TimeoutExpired:
        logger.error("❌ FaceFusion timeout")
        raise HTTPException(status_code=500, detail="Face swap processing timeout")
    except Exception as e:
        logger.error(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup temp files
        for p in [user_path, character_path]:
            if p.exists():
                p.unlink()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
