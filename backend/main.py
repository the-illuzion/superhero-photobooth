from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import base64
from io import BytesIO
from PIL import Image
import os

app = FastAPI(title="Superhero Photo Booth API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import face morphing module
try:
    from ai.insightface_swap import swap_faces_advanced as morph_faces
    print("✓ Using InsightFace for advanced face swapping")
except ImportError as e:
    print(f"InsightFace not available ({e}), falling back to simple morph")
    try:
        from ai.face_swap import morph_faces
    except ImportError:
        from ai.simple_morph import simple_morph as morph_faces

@app.get("/")
async def root():
    return {"message": "Superhero Photo Booth API is running!"}

@app.post("/api/morph")
async def morph_image(
    user_image: UploadFile = File(...),
    character: str = Form(...)
):
    """
    Endpoint to morph user's face onto a character body.
    
    Args:
        user_image: User's uploaded photo
        character: Selected character ID (ironman, spiderman, etc.)
    
    Returns:
        JSON with base64 encoded result image
    """
    try:
        # Read user image
        user_img_bytes = await user_image.read()
        user_img = Image.open(BytesIO(user_img_bytes))
        
        # Get character image path
        character_path = f"../public/characters/{character}.jpg"
        
        if not os.path.exists(character_path):
            return JSONResponse(
                status_code=404,
                content={"error": f"Character '{character}' not found"}
            )
        
        # Perform face morphing
        result_img = morph_faces(user_img, character_path)
        
        # Convert result to base64
        buffered = BytesIO()
        result_img.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        return {
            "success": True,
            "result_image": f"data:image/jpeg;base64,{img_base64}"
        }
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
