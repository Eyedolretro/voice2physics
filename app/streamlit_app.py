# ======================================================
# Streamlit App – Voice2Physics
# Prototype fonctionnel : vocal/texte → schéma → calculs
# ======================================================

import sys
import os

# 🔹 Ajouter le dossier racine au path pour trouver src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

# 🔹 Import des modules src
from src.parser_voice import parse_voice_command
from src.physics_engine import compute_physics
from src.image_generator import generate_diagram

# ======================================================
# Interface utilisateur
# ======================================================
st.title("🎛 Voice2Physics")
st.write("Décrivez un système physique à la voix (ou texte), et obtenez son schéma et ses calculs.")

# Saisie texte (ou utiliser la reconnaissance vocale)
user_input = st.text_input("Décrivez votre expérience :", "")

if user_input:
    # 🔹 Extraire les paramètres (masse, raideur, etc.)
    params = parse_voice_command(user_input)
    st.write("🔍 Paramètres détectés :", params)

    # 🔹 Calculs physiques
    results = compute_physics(params)
    st.write("📊 Résultats des calculs :", results)

    # 🔹 Génération diagramme
    diagram_path = generate_diagram(params)
    st.image(diagram_path, caption="Diagramme généré", use_column_width=True)

# ======================================================
# Footer
# ======================================================
st.write("---")
st.write("Prototype Voice2Physics – 🔬 Calculs et diagrammes automatiques")
