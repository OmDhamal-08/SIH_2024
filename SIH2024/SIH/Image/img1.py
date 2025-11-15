from PIL import Image

with Image.open("img1.png","r") as f:
    r=f.rotate(90)
r.save("img1.png")