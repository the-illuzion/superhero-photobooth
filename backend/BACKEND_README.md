# Superhero Photobooth Backend

This backend uses FaceFusion for face swapping with the `hyperswap-1c` model.

## Setup (Already Done)

The backend has been set up with `uv` for better dependency management:
- Virtual environment created at `.venv`
- All dependencies installed via `uv pip install`

## Running the Backend

### Option 1: Using the start script
```bash
./start-backend.sh
```

### Option 2: Manual start
```bash
# Activate virtual environment
source .venv/bin/activate

# Start the server
python api.py
```

### Option 3: Using uvicorn directly
```bash
source .venv/bin/activate
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

### Health Check
```bash
GET http://localhost:8000/
```

### Face Swap (Morph)
```bash
POST http://localhost:8000/morph
Content-Type: multipart/form-data

- user_image: File (the person's face to swap)
- character_image: File (the superhero/character body)
```

Returns:
```json
{
  "success": true,
  "image": "data:image/png;base64,..."
}
```

## How It Works

1. Receives two images from frontend
2. Saves them temporarily
3. Calls FaceFusion CLI with `hyperswap-1c` processor
4. Returns the face-swapped result as base64

## Dependencies

- FastAPI (web framework)
- Uvicorn (ASGI server)
- FaceFusion (face swapping engine)
- OpenCV (image processing)
- NumPy, SciPy (numerical operations)

## Troubleshooting

**Port already in use:**
```bash
# Kill existing process on port 8000
lsof -ti:8000 | xargs kill -9
```

**Dependencies issue:**
```bash
# Reinstall with uv
uv pip install -r requirements.txt
```
