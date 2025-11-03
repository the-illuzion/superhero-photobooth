# Adding Superhero Images

## How to Add Your Superhero Character Images

### Step 1: Prepare Your Images

1. **Find or create superhero images** with clear, visible faces
2. **Recommended specifications:**
   - Format: JPG or PNG
   - Resolution: At least 600x800 pixels
   - Face should be clearly visible and front-facing
   - Good lighting on the face

### Step 2: Place Images in the Correct Folder

Put your superhero images in:
```
public/characters/
```

**Naming Convention:**
- Use lowercase, no spaces
- Examples: `ironman.jpg`, `spiderman.jpg`, `batman.jpg`, `wonderwoman.jpg`

### Step 3: Update the Frontend

Edit `frontend/app/booth/page.tsx` and update the `CHARACTERS` array:

```typescript
const CHARACTERS = [
  { id: 'ironman', name: 'Iron Man', image: '/characters/ironman.jpg' },
  { id: 'spiderman', name: 'Spider-Man', image: '/characters/spiderman.jpg' },
  { id: 'batman', name: 'Batman', image: '/characters/batman.jpg' },
  { id: 'wonderwoman', name: 'Wonder Woman', image: '/characters/wonderwoman.jpg' },
  // Add more characters here:
  { id: 'superman', name: 'Superman', image: '/characters/superman.jpg' },
  { id: 'hulk', name: 'Hulk', image: '/characters/hulk.jpg' },
]
```

### Step 4: Restart the Frontend

```bash
# The frontend will hot-reload automatically
# Or restart manually:
cd frontend
npm run dev
```

## Face Swap Technology

The app now uses **MediaPipe Face Mesh** for high-quality face swapping:

### How It Works:

1. **Face Detection**: MediaPipe detects 468 facial landmarks on both your face and the character's face
2. **Delaunay Triangulation**: Creates a mesh of triangles connecting the landmarks
3. **Face Warping**: Warps your facial features to match the character's face structure
4. **Seamless Blending**: Uses OpenCV's seamless cloning to blend the result naturally

### Features:

✅ **Accurate landmark detection** (468 points on face)  
✅ **Natural warping** using Delaunay triangulation  
✅ **Seamless blending** with the character's body  
✅ **Works with any face angle** (best with front-facing)  
✅ **Preserves facial expressions**  

## Tips for Best Results

### For Character Images:
- ✅ Use high-quality images
- ✅ Character's face should be clearly visible
- ✅ Front-facing or slight angle works best
- ✅ Good lighting on the face
- ❌ Avoid heavily shadowed faces
- ❌ Avoid profile views (side angles)

### For User Photos:
- ✅ Look directly at the camera
- ✅ Good lighting on your face
- ✅ Neutral or slight smile expression
- ✅ Remove glasses if possible (for best results)
- ❌ Avoid heavy shadows
- ❌ Avoid extreme angles

## Examples

### Directory Structure:
```
public/characters/
├── ironman.jpg          # Tony Stark in Iron Man suit
├── spiderman.jpg        # Spider-Man with mask
├── batman.jpg           # Batman in cowl
├── wonderwoman.jpg      # Wonder Woman
├── superman.jpg         # Superman
├── thor.jpg             # Thor
├── blackwidow.jpg       # Black Widow
└── captainamerica.jpg   # Captain America
```

### Image Sources:

**Legal Options:**
- Stock photo websites (with proper licenses)
- Fan art (with artist permission)
- Your own photos in costumes
- AI-generated superhero images
- Public domain images

**Note:** Ensure you have the right to use any images you add.

## Troubleshooting

### "No face detected in character image"
- Character image needs a clear, visible face
- Try a different image with better face visibility
- Ensure the face is not too small in the image

### "Face swap doesn't look good"
- Use higher quality character images
- Ensure good lighting in both user and character images
- Try character images with front-facing poses

### "Swap is slow"
- First swap initializes the models (takes ~2-3 seconds)
- Subsequent swaps are faster
- MediaPipe runs on CPU - consider upgrading hardware for faster processing

## Advanced: Using Your Own Face Swap Model

If you want to use a different face swap technology:

1. Create a new file in `backend/ai/your_swap.py`
2. Implement a function with this signature:
   ```python
   def your_swap_function(user_image: PIL.Image, character_path: str) -> PIL.Image:
       # Your implementation
       pass
   ```
3. Update `backend/main.py` to import your function
4. Restart the backend

## Current Technology Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS v4
- **Backend**: FastAPI (Python)
- **Face Detection**: MediaPipe Face Mesh (468 landmarks)
- **Face Warping**: Delaunay Triangulation + Affine Transform
- **Blending**: OpenCV Seamless Cloning
- **Fallback**: Simple overlay method (if MediaPipe fails)

---

**Have fun creating superhero transformations!** 🦸‍♂️🦸‍♀️
