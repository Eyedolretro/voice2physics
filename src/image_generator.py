from PIL import Image, ImageDraw

def generate_diagram(params):
    img = Image.new("RGB", (300, 300), color="white")
    draw = ImageDraw.Draw(img)

    if params["type"] == "cercle":
        draw.ellipse((50, 50, 250, 250), outline="black", width=3)
    elif params["type"] == "triangle":
        draw.polygon([(150, 50), (50, 250), (250, 250)], outline="black", width=3)
    elif params["type"] == "levier":
        draw.line((50, 150, 250, 150), fill="black", width=3)
        draw.line((150, 150, 150, 50), fill="black", width=3)
    else:
        draw.text((100, 150), "Système inconnu", fill="red")

    path = "temp_diagram.png"
    img.save(path)
    return path
