from PIL import Image, ImageDraw, ImageFilter
import os
os.makedirs('assets', exist_ok=True)
S = 1024
bg = Image.new('RGB', (S, S))
d = ImageDraw.Draw(bg)
for y in range(S):
    t = y / S
    d.line([(0, y), (S, y)], fill=(int(40 - 30 * t), int(26 - 18 * t), int(100 - 70 * t)))
cells = [(0,0,'#b44cff'),(1,0,'#b44cff'),(2,0,'#b44cff'),(1,1,'#b44cff'),
         (0,1,'#ffd400'),(0,2,'#ffd400'),(1,2,'#ffd400'),
         (2,1,'#00e5ff'),(2,2,'#00e5ff')]
z, g = 176, 10
o = (S - 3 * z) // 2
art = Image.new('RGBA', (S, S), (0, 0, 0, 0))
ad = ImageDraw.Draw(art)
for cx, cy, c in cells:
    x, y = o + cx * z, o + cy * z
    ad.rounded_rectangle([x + g, y + g, x + z - g, y + z - g], 30, fill=c)
    ad.rounded_rectangle([x + g + 8, y + g + 8, x + z - g - 8, y + (z // 2)], 22, fill=(255, 255, 255, 60))
glow = art.filter(ImageFilter.GaussianBlur(34))
fg = Image.alpha_composite(glow, art)
bg.save('assets/icon-background.png')
fg.save('assets/icon-foreground.png')
Image.alpha_composite(bg.convert('RGBA'), fg).save('assets/icon-only.png')
