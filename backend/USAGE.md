# Backend Usage Guide

## Running the Backend

The backend is a FastAPI service that uses FaceFusion for face swapping.

### Start the backend:
```bash
cd backend
python3 main.py
```

The backend will start on http://localhost:8000

### API Endpoints:

1. **Health Check**
   ```bash
   GET /
   ```
   Returns: `{"status": "ok", "message": "Superhero Photobooth Backend"}`

2. **Face Swap**
   ```bash
   POST /morph
   ```
   
   **Parameters:**
   - `user_image`: The source image (user's face)
   - `character_image`: The target image (superhero/character body)
   
   **Returns:**
   ```json
   {
     "success": true,
     "image": "data:image/jpeg;base64,..."
   }
   ```

### Requirements:

The backend uses:
- **FaceFusion**: For face swapping (`face_swapper` processor)
- **FastAPI**: For the API server
- **Python 3**: System Python 3 (currently using /usr/bin/python3)

### Directories:

- `temp/`: Temporary storage for uploaded images
- `output/`: Generated face-swapped images
- `.venv/`: FaceFusion's virtual environment (if using uv)

### Timeout:

Face swapping has a 120-second timeout. If processing takes longer, the request will fail.

### Troubleshooting:

1. **Port already in use**: Kill any existing backend process:
   ```bash
   lsof -i :8000
   kill -9 <PID>
   ```

2. **FaceFusion errors**: Check that FaceFusion is properly installed in the backend directory

3. **Check logs**: The backend logs are written to `backend.log`
   ```bash
   tail -f backend.log
   ```

### Frontend Integration:

The frontend sends both user webcam image and selected character image to `/morph` endpoint and displays the result.
