from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
images_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
os.makedirs(images_dir, exist_ok=True)

# Image dimensions
width, height = 800, 600

# Service configurations
services = [
    {
        'filename': 'service-network-infrastructure.jpg',
        'gradient': [(15, 23, 42), (30, 58, 138)],  # slate-900 to blue-900
        'title': 'Network Infrastructure',
        'icon_color': (59, 130, 246)  # blue-500
    },
    {
        'filename': 'service-security-access.jpg',
        'gradient': [(15, 23, 42), (127, 29, 29)],  # slate-900 to red-900
        'title': 'Security & Access Control',
        'icon_color': (239, 68, 68)  # red-500
    },
    {
        'filename': 'service-office-equipment.jpg',
        'gradient': [(15, 23, 42), (21, 94, 117)],  # slate-900 to cyan-900
        'title': 'Office & Data Equipment',
        'icon_color': (6, 182, 212)  # cyan-500
    },
    {
        'filename': 'service-computing.jpg',
        'gradient': [(15, 23, 42), (88, 28, 135)],  # slate-900 to purple-900
        'title': 'Computing & Accessories',
        'icon_color': (168, 85, 247)  # purple-500
    },
    {
        'filename': 'service-product-supply.jpg',
        'gradient': [(15, 23, 42), (4, 120, 87)],  # slate-900 to emerald-900
        'title': 'Product Supply & Logistics',
        'icon_color': (16, 185, 129)  # emerald-500
    }
]

def create_gradient(draw, width, height, color1, color2):
    """Create a diagonal gradient"""
    for y in range(height):
        for x in range(width):
            # Calculate gradient factor (diagonal)
            factor = (x + y) / (width + height)
            
            r = int(color1[0] + (color2[0] - color1[0]) * factor)
            g = int(color1[1] + (color2[1] - color1[1]) * factor)
            b = int(color1[2] + (color2[2] - color1[2]) * factor)
            
            draw.point((x, y), fill=(r, g, b))

def add_tech_pattern(draw, width, height, color):
    """Add geometric tech pattern overlay"""
    # Draw circuit-like lines
    for i in range(0, width, 100):
        draw.line([(i, 0), (i + 50, height)], fill=color, width=2)
    
    for i in range(0, height, 100):
        draw.line([(0, i), (width, i + 50)], fill=color, width=2)
    
    # Draw nodes/circles at intersections
    for x in range(100, width, 100):
        for y in range(100, height, 100):
            draw.ellipse([x-10, y-10, x+10, y+10], fill=color, outline=color)

# Generate images
for service in services:
    print(f"Generating {service['filename']}...")
    
    # Create base image
    img = Image.new('RGB', (width, height), color=service['gradient'][0])
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Create gradient background
    create_gradient(draw, width, height, service['gradient'][0], service['gradient'][1])
    
    # Add semi-transparent tech pattern
    pattern_color = (*service['icon_color'], 30)  # Add alpha for transparency
    add_tech_pattern(draw, width, height, pattern_color)
    
    # Add vignette effect (darken edges)
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    for i in range(150):
        alpha = int((i / 150) * 100)
        overlay_draw.rectangle(
            [i, i, width-i, height-i],
            outline=(*service['gradient'][0], alpha)
        )
    
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Draw large icon-like shape in center
    draw = ImageDraw.Draw(img, 'RGBA')
    center_x, center_y = width // 2, height // 2
    
    # Draw a stylized tech icon (abstract geometric shape)
    icon_color = (*service['icon_color'], 180)
    
    if 'Network' in service['title']:
        # Network nodes
        for offset in [(-100, -50), (100, -50), (-100, 50), (100, 50), (0, 0)]:
            x, y = center_x + offset[0], center_y + offset[1]
            draw.ellipse([x-30, y-30, x+30, y+30], fill=icon_color)
        # Connection lines
        draw.line([(center_x, center_y), (center_x-100, center_y-50)], fill=icon_color, width=8)
        draw.line([(center_x, center_y), (center_x+100, center_y-50)], fill=icon_color, width=8)
        draw.line([(center_x, center_y), (center_x-100, center_y+50)], fill=icon_color, width=8)
        draw.line([(center_x, center_y), (center_x+100, center_y+50)], fill=icon_color, width=8)
    
    elif 'Security' in service['title']:
        # Shield shape
        points = [
            (center_x, center_y - 120),
            (center_x + 80, center_y - 80),
            (center_x + 80, center_y + 40),
            (center_x, center_y + 120),
            (center_x - 80, center_y + 40),
            (center_x - 80, center_y - 80)
        ]
        draw.polygon(points, fill=icon_color)
        # Lock symbol
        draw.rectangle([center_x-30, center_y, center_x+30, center_y+60], fill=(255, 255, 255, 200))
        draw.ellipse([center_x-25, center_y-40, center_x+25, center_y+10], outline=(255, 255, 255, 200), width=8)
    
    elif 'Office' in service['title']:
        # Printer/document shape
        draw.rectangle([center_x-100, center_y-80, center_x+100, center_y+80], fill=icon_color)
        draw.rectangle([center_x-80, center_y-60, center_x+80, center_y-30], fill=(255, 255, 255, 200))
        draw.rectangle([center_x-80, center_y-20, center_x+80, center_y+10], fill=(255, 255, 255, 200))
        draw.rectangle([center_x-80, center_y+20, center_x+80, center_y+50], fill=(255, 255, 255, 200))
    
    elif 'Computing' in service['title']:
        # Laptop shape
        draw.rectangle([center_x-120, center_y-60, center_x+120, center_y+40], fill=icon_color)
        draw.rectangle([center_x-100, center_y-50, center_x+100, center_y+10], fill=(255, 255, 255, 200))
        draw.polygon([
            (center_x-140, center_y+40),
            (center_x+140, center_y+40),
            (center_x+120, center_y+60),
            (center_x-120, center_y+60)
        ], fill=icon_color)
    
    else:  # Product Supply
        # Boxes/packages
        draw.rectangle([center_x-80, center_y-80, center_x+20, center_y+20], fill=icon_color)
        draw.rectangle([center_x+30, center_y-50, center_x+110, center_y+50], fill=icon_color)
        draw.rectangle([center_x-50, center_y+30, center_x+30, center_y+100], fill=icon_color)
        # Draw lines to indicate boxes
        draw.line([(center_x-30, center_y-80), (center_x-30, center_y+20)], fill=(255, 255, 255, 150), width=4)
        draw.line([(center_x+70, center_y-50), (center_x+70, center_y+50)], fill=(255, 255, 255, 150), width=4)
    
    # Save image
    output_path = os.path.join(images_dir, service['filename'])
    img.save(output_path, 'JPEG', quality=95)
    print(f"Saved {output_path}")

print("\nAll service images generated successfully!")
