from PIL import Image, ImageDraw

def generate_diagram(params: dict):
    """
    Crée un diagramme simple du système masse-ressort.
    """
    img = Image.new("RGB", (400, 200), "white")
    draw = ImageDraw.Draw(img)

    # Ligne du ressort
    draw.line((50, 100, 350, 100), fill="black", width=3)
    
    # Bloc représentant la masse
    draw.rectangle((170, 80, 230, 120), fill="gray")
    
    # Texte masse
    m_text = f"m={params.get('m','?')} kg"
    k_text = f"k={params.get('k','?')} N/m"
    draw.text((180, 130), m_text, fill="black")
    draw.text((50, 40), k_text, fill="black")
    
    return img
