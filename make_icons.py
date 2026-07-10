from PIL import Image, ImageDraw, ImageFont
import math

def make_icon(size, out_path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    radius = int(size * 0.22)
    bg_color = (255, 45, 120, 255)

    # Rounded rect background
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=bg_color)

    # Subtle inner glow ring
    glow_w = max(2, size // 48)
    draw.rounded_rectangle(
        [glow_w*2, glow_w*2, size-1-glow_w*2, size-1-glow_w*2],
        radius=radius-glow_w*2,
        outline=(255, 180, 210, 80),
        width=glow_w
    )

    # Flower emoji approximation — draw a simple stylized circle burst
    cx, cy = size // 2, size // 2
    petal_r = size * 0.18
    inner_r = size * 0.09
    num_petals = 8
    petal_color = (255, 255, 255, 230)
    center_color = (255, 220, 240, 255)

    for i in range(num_petals):
        angle = (2 * math.pi * i) / num_petals
        px = cx + math.cos(angle) * petal_r * 0.55
        py = cy + math.sin(angle) * petal_r * 0.55
        r = petal_r * 0.42
        draw.ellipse([px-r, py-r, px+r, py+r], fill=petal_color)

    # Center circle
    draw.ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=center_color
    )

    # Tiny dot detail in center
    dot_r = inner_r * 0.35
    draw.ellipse(
        [cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r],
        fill=(255, 100, 160, 255)
    )

    img.save(out_path, 'PNG')
    print(f'Saved {out_path}')

make_icon(192, 'icon-192.png')
make_icon(512, 'icon-512.png')
