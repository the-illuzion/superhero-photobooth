"""
Simple face morphing script that creates placeholder character images.
Install OpenCV later for actual face swapping: pip install opencv-python
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_dummy_character_images():
    """
    Create dummy character images for testing without requiring OpenCV.
    Replace these with actual superhero images later.
    """
    characters = {
        'ironman': {'color': (220, 20, 60), 'label': 'IRON MAN'},
        'spiderman': {'color': (255, 0, 0), 'label': 'SPIDER-MAN'},
        'batman': {'color': (50, 50, 50), 'label': 'BATMAN'},
        'wonderwoman': {'color': (220, 180, 20), 'label': 'WONDER WOMAN'}
    }
    
    output_dir = '../public/characters'
    os.makedirs(output_dir, exist_ok=True)
    
    for char_id, char_info in characters.items():
        # Create image with character color
        img = Image.new('RGB', (600, 800), color=char_info['color'])
        draw = ImageDraw.Draw(img)
        
        # Draw a simple superhero silhouette
        # Head
        draw.ellipse([225, 100, 375, 250], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        # Eyes
        draw.ellipse([260, 150, 280, 170], fill=(255, 255, 255))
        draw.ellipse([320, 150, 340, 170], fill=(255, 255, 255))
        # Body
        draw.rectangle([250, 250, 350, 500], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        # Arms
        draw.rectangle([150, 280, 250, 320], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        draw.rectangle([350, 280, 450, 320], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        # Legs
        draw.rectangle([260, 500, 310, 700], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        draw.rectangle([340, 500, 390, 700], fill=(0, 0, 0), outline=(255, 255, 255), width=3)
        
        # Add character name
        try:
            # Try to use a system font
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        except:
            font = ImageFont.load_default()
        
        # Get text bbox for centering
        bbox = draw.textbbox((0, 0), char_info['label'], font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (600 - text_width) // 2
        
        draw.text((text_x, 720), char_info['label'], fill=(255, 255, 255), font=font)
        
        # Save image
        output_path = f'{output_dir}/{char_id}.jpg'
        img.save(output_path, 'JPEG', quality=95)
        print(f"✓ Created {char_id}.jpg")
    
    print(f"\n✅ All character images created in {output_dir}/")
    print("Replace these with actual superhero images for better results!")

def simple_morph(user_image, character_path):
    """
    Simple image blending without OpenCV.
    For better results, install opencv-python and use the advanced version.
    """
    from PIL import ImageFilter
    
    # Load character image
    char_img = Image.open(character_path)
    
    # Resize user image to fit in the head area
    user_resized = user_image.resize((150, 150))
    
    # Create a circular mask
    mask = Image.new('L', (150, 150), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([0, 0, 150, 150], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(10))
    
    # Paste user face onto character (in the head area)
    result = char_img.copy()
    result.paste(user_resized, (225, 100), mask)
    
    return result

if __name__ == "__main__":
    create_dummy_character_images()
