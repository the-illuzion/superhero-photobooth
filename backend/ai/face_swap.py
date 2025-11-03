"""
Face swapping/morphing module using OpenCV and basic image processing.
For production, consider using InsightFace or SimSwap for better results.
"""

import cv2
import numpy as np
from PIL import Image
import os

def detect_face(image):
    """
    Detect face in image using Haar Cascade classifier.
    
    Args:
        image: PIL Image or numpy array
    
    Returns:
        Tuple of (x, y, w, h) for face bounding box, or None if no face found
    """
    # Convert PIL to OpenCV format if needed
    if isinstance(image, Image.Image):
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        return faces[0]  # Return first face found
    return None

def morph_faces(user_image, character_path):
    """
    Morph user's face onto character image.
    This is a simplified version using face detection and blending.
    
    Args:
        user_image: PIL Image of user's photo
        character_path: Path to character image file
    
    Returns:
        PIL Image of morphed result
    """
    # Convert user image to OpenCV format
    user_cv = cv2.cvtColor(np.array(user_image), cv2.COLOR_RGB2BGR)
    
    # Load character image
    character_cv = cv2.imread(character_path)
    if character_cv is None:
        raise ValueError(f"Could not load character image: {character_path}")
    
    # Detect faces in both images
    user_face = detect_face(user_cv)
    char_face = detect_face(character_cv)
    
    if user_face is None:
        raise ValueError("No face detected in user image")
    
    if char_face is None:
        # If no face in character, just overlay user face in center
        char_face = (
            character_cv.shape[1] // 4,
            character_cv.shape[0] // 4,
            character_cv.shape[1] // 2,
            character_cv.shape[0] // 2
        )
    
    # Extract face regions
    ux, uy, uw, uh = user_face
    cx, cy, cw, ch = char_face
    
    user_face_region = user_cv[uy:uy+uh, ux:ux+uw]
    
    # Resize user face to match character face region
    user_face_resized = cv2.resize(user_face_region, (cw, ch))
    
    # Create result image (copy of character)
    result = character_cv.copy()
    
    # Blend user face onto character
    # Create a mask for smooth blending
    mask = np.zeros((ch, cw), dtype=np.uint8)
    center = (cw // 2, ch // 2)
    radius = min(cw, ch) // 2
    cv2.circle(mask, center, radius, 255, -1)
    
    # Apply Gaussian blur to mask for smooth edges
    mask = cv2.GaussianBlur(mask, (21, 21), 11)
    
    # Normalize mask
    mask_normalized = mask.astype(float) / 255.0
    mask_3channel = np.stack([mask_normalized] * 3, axis=2)
    
    # Blend faces
    face_region = result[cy:cy+ch, cx:cx+cw]
    blended = (user_face_resized * mask_3channel + 
               face_region * (1 - mask_3channel)).astype(np.uint8)
    
    # Place blended face back onto result
    result[cy:cy+ch, cx:cx+cw] = blended
    
    # Convert back to PIL Image
    result_pil = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    
    return result_pil

def create_dummy_character_images():
    """
    Create dummy character images for testing.
    This should be replaced with actual superhero images.
    """
    characters = ['ironman', 'spiderman', 'batman', 'wonderwoman']
    output_dir = '../public/characters'
    
    os.makedirs(output_dir, exist_ok=True)
    
    colors = {
        'ironman': (200, 50, 50),      # Red
        'spiderman': (255, 0, 0),       # Bright Red
        'batman': (50, 50, 50),         # Dark Gray
        'wonderwoman': (220, 180, 20)   # Gold
    }
    
    for char in characters:
        # Create colored dummy image
        img = np.zeros((600, 400, 3), dtype=np.uint8)
        img[:] = colors[char]
        
        # Add text
        cv2.putText(img, char.upper(), (50, 300), 
                   cv2.FONT_HERSHEY_BOLD, 1.5, (255, 255, 255), 3)
        
        # Draw a simple face outline
        cv2.circle(img, (200, 200), 80, (255, 255, 255), 2)
        cv2.circle(img, (170, 180), 10, (255, 255, 255), -1)  # Left eye
        cv2.circle(img, (230, 180), 10, (255, 255, 255), -1)  # Right eye
        cv2.ellipse(img, (200, 220), (30, 20), 0, 0, 180, (255, 255, 255), 2)  # Smile
        
        cv2.imwrite(f'{output_dir}/{char}.jpg', img)
        print(f"Created {char}.jpg")

if __name__ == "__main__":
    # Create dummy character images for testing
    create_dummy_character_images()
    print("Dummy character images created!")
