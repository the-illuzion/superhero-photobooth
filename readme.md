# Copilot Instructions: Build an AI-Powered Photo Booth

Goal:
Create a web application that allows a user to upload or capture their photo, select a movie character, and generate a morphed image where the user's face is blended with the chosen character's body.

Architecture Overview:
- Frontend: Next.js or React (camera capture, character selection, image preview, and download button)
- Backend: FastAPI (Python) or Node.js (Express) server to handle image uploads and call AI models
- AI Core: Python script that performs face detection and morphing using one of the following approaches:
  - SimSwap or InsightFace for realistic face swapping
  - Stable Diffusion + ControlNet + InstantID for stylized diffusion-based blending
- Storage: Use local storage for now (later can integrate AWS S3 or Firebase)
- Output: A single generated image with the user's face blended on the movie character's body.

Core Steps to Implement:
1. Create a frontend page `/booth` with:
   - Webcam capture and file upload options.
   - Dropdown to select a movie character (preloaded static images in `/public/characters`).
   - Submit button to send image + character choice to backend.

2. Backend endpoint `/api/morph`:
   - Accept multipart/form-data (user image + character name).
   - Run the face morphing model (using SimSwap or Stable Diffusion pipeline).
   - Return the generated image as a base64 or downloadable URL.

3. AI Morphing Logic (Python):
   - Detect user face and align it with target character.
   - Blend faces using chosen model.
   - Apply Poisson blending or feathered alpha mask for natural transitions.

4. Frontend should display loading animation and final output image.

5. Ensure modularity — `ai/face_swap.py`, `routes/morph.py`, `frontend/pages/booth.tsx`.

Deliverables:
- A minimal working prototype with clean, readable, and modular code.
- Include comments explaining each major function.
- Focus on local testing before deployment.

Bonus (optional):
- Add “Retake Photo” and “Try Another Character” buttons.
- Integrate live preview before morphing.
