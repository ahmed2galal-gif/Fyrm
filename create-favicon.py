#!/usr/bin/env python3
"""
Create Google-suitable favicon from fyrmtech logo
Per Google Search guidelines: https://developers.google.com/search/docs/appearance/favicon-in-search
"""

from PIL import Image
import os

def create_favicon():
    logo_path = os.path.join(os.path.dirname(__file__), 'images', 'fyrmtech-logo.png')
    favicon_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
    favicon_png_path = os.path.join(os.path.dirname(__file__), 'images', 'favicon.png')
    
    if not os.path.exists(logo_path):
        print(f"Error: Logo not found at {logo_path}")
        return False
    
    try:
        # Open the original logo
        img = Image.open(logo_path)
        print(f"Original logo size: {img.size}")
        
        # Ensure the image is square by cropping or padding
        width, height = img.size
        if width != height:
            # Make it square by taking the smaller dimension
            size = min(width, height)
            left = (width - size) // 2
            top = (height - size) // 2
            right = left + size
            bottom = top + size
            img = img.crop((left, top, right, bottom))
            print(f"Cropped to square: {img.size}")
        
        # Convert to RGBA if needed (for transparency)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create favicon with multiple sizes for the ICO format
        # Google recommends at least 48x48px, we'll include multiple sizes
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        favicon_images = []
        
        for size in sizes:
            # Resize image to the specific size
            resized = img.resize(size, Image.Resampling.LANCZOS)
            favicon_images.append(resized)
            print(f"Created {size[0]}x{size[1]} version")
        
        # Save as ICO with all sizes
        favicon_images[0].save(
            favicon_path,
            format='ICO',
            sizes=sizes,
            quality=95
        )
        print(f"✓ Favicon saved to: {favicon_path}")
        
        # Also save a 256x256 PNG version for additional compatibility
        favicon_images[-1].save(favicon_png_path)
        print(f"✓ PNG favicon saved to: {favicon_png_path}")
        
        return True
        
    except Exception as e:
        print(f"Error creating favicon: {e}")
        return False

if __name__ == '__main__':
    success = create_favicon()
    if success:
        print("\n✓ Favicon creation completed successfully!")
        print("Files created:")
        print("  - favicon.ico (root directory)")
        print("  - favicon.png (images directory)")
    else:
        print("\n✗ Favicon creation failed")
        exit(1)
