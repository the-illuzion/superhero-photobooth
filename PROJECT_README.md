# Superhero Photo Booth

An AI-powered photo booth application that transforms users into their favorite superhero characters using face swapping technology.

## Features

- 📷 Webcam capture or photo upload
- 🦸 Multiple superhero character options
- ✨ AI-powered face morphing
- 💾 Download transformed images
- 🎨 Beautiful, responsive UI

## Tech Stack

**Frontend:**
- Next.js 14 with TypeScript
- Tailwind CSS for styling
- React Webcam for camera capture

**Backend:**
- FastAPI (Python)
- OpenCV for face detection
- PIL for image processing

## Project Structure

```
superhero-photobooth/
├── frontend/              # Next.js frontend application
│   ├── app/
│   │   ├── page.tsx      # Home page
│   │   ├── booth/        # Photo booth page
│   │   ├── layout.tsx    # Root layout
│   │   └── globals.css   # Global styles
│   └── package.json
├── backend/               # FastAPI backend
│   ├── main.py           # API endpoints
│   ├── ai/
│   │   └── face_swap.py  # Face morphing logic
│   └── requirements.txt
└── public/
    └── characters/        # Character images
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
```bash
cd superhero-photobooth
```

2. **Setup Frontend**
```bash
cd frontend
npm install
```

3. **Setup Backend**
```bash
cd ../backend
pip install -r requirements.txt
```

4. **Create Character Images**
```bash
# Generate dummy character images for testing
python ai/face_swap.py
```

### Running the Application

1. **Start the Backend Server**
```bash
cd backend
python main.py
```
The API will run on http://localhost:8000

2. **Start the Frontend** (in a new terminal)
```bash
cd frontend
npm run dev
```
The app will run on http://localhost:3000

3. **Open your browser** and navigate to http://localhost:3000

## Usage

1. Click "Start Photo Booth" on the home page
2. Choose to capture a photo with your webcam or upload an existing photo
3. Select your favorite superhero character
4. Click "Transform Me!" and watch the magic happen
5. Download your transformed image or try another character

## How It Works

1. **Frontend**: Captures/uploads user photo and sends it to the backend API
2. **Backend**: 
   - Detects faces in both user and character images using Haar Cascade
   - Extracts and resizes user's face region
   - Blends user's face onto character's body using alpha masking
   - Returns the morphed image as base64
3. **Frontend**: Displays the result with download option

## Future Enhancements

- [ ] Integrate InsightFace or SimSwap for more realistic face swapping
- [ ] Add Stable Diffusion + ControlNet for stylized transformations
- [ ] Implement face landmark detection for better alignment
- [ ] Add more superhero characters
- [ ] Social sharing features
- [ ] Cloud storage integration (AWS S3 / Firebase)
- [ ] Real-time preview before morphing

## Development Notes

- The current implementation uses basic OpenCV face detection and blending
- For production-quality face swaps, consider:
  - **InsightFace**: Best for realistic face swapping
  - **SimSwap**: High-quality face swap models
  - **Stable Diffusion + InstantID**: For stylized, diffusion-based results

## License

MIT

## Author

Built with ❤️ for fun and learning
