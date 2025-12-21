from PIL import Image
import os

# Load the original logo with transparent background
logo_path = "images/fyrmtech-logo.png"
output_path = "images/fyrmtech-logo-bg.png"

# Open the logo
logo = Image.open(logo_path)

# Create a new image with black background (1200x630 for Google Search)
width, height = 1200, 630
background = Image.new('RGB', (width, height), color='#000000')

# Calculate position to center the logo
logo.thumbnail((width - 100, height - 100), Image.Resampling.LANCZOS)
logo_width, logo_height = logo.size
x = (width - logo_width) // 2
y = (height - logo_height) // 2

# Paste logo onto black background
if logo.mode == 'RGBA':
    # If logo has transparency, use it
    background.paste(logo, (x, y), logo)
else:
    background.paste(logo, (x, y))

# Save the new image
background.save(output_path, 'PNG', quality=95)
print(f"✓ Logo with black background created: {output_path}")
print(f"  Size: {width}x{height}px")
print(f"  Format: PNG")
