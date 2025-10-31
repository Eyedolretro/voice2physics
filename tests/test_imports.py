import sys
import os

# Ajouter le dossier racine au path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from src.parser_voice import parse_voice_command
    from src.physics_engine import compute_physics
    from src.image_generator import generate_diagram
    print("✅ Tous les modules src/ sont accessibles !")
except ModuleNotFoundError as e:
    print("❌ Module manquant :", e)
