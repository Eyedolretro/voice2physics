import sys
import os
import streamlit as st
import speech_recognition as sr

# -----------------------
# Fix pour src
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from src.parser_voice import parse_voice_command
from src.physics_engine import compute_physics
from src.image_generator import generate_diagram
import json

# -----------------------
st.set_page_config(page_title="Voice2Physics", layout="wide")
st.title("Voice2Physics – Reconnaissance vocale et calculs physiques")

# -----------------------
# Chargement des exemples
with open("examples.json") as f:
    examples = json.load(f)
example_names = [ex["name"] for ex in examples]

st.sidebar.header("Exemples rapides (optionnels)")
example_choice = st.sidebar.selectbox("Choisir un exemple", example_names)
if st.sidebar.button("Charger l'exemple"):
    user_input = examples[example_names.index(example_choice)]["text"]
else:
    user_input = ""

# -----------------------
# Reconnaissance vocale prioritaire
st.subheader("🎤 Parlez maintenant…")
if st.button("Démarrer la reconnaissance vocale"):
    r = sr.Recognizer()
    r.energy_threshold = 300
    try:
        with sr.Microphone() as source:
            st.info("🎤 Écoute en cours… Parlez clairement")
            audio = r.listen(source, timeout=5)
        try:
            user_input = r.recognize_google(audio, language="fr-FR")
            st.success(f"Texte reconnu : {user_input}")
        except sr.UnknownValueError:
            st.error("⚠️ Impossible de comprendre l'audio")
            user_input = ""
        except sr.RequestError as e:
            st.error(f"Erreur service Google : {e}")
            user_input = ""
    except Exception as e:
        st.error(f"Erreur micro : {e}")
        user_input = ""

# -----------------------
# Zone texte optionnelle
user_input = st.text_input("Ou tapez votre description (option texte, facultatif) :", value=user_input)

# -----------------------
# Traitement
if user_input:
    params = parse_voice_command(user_input)
    st.write("Paramètres détectés :", params)

    if params:
        results, formulas = compute_physics(params)
        st.subheader("Résultats physiques")
        st.json(results)

        st.subheader("Formules utilisées")
        st.json(formulas)

        diagram_path = generate_diagram(params)
        st.image(diagram_path, caption="Diagramme généré", use_container_width=True)
    else:
        st.warning("⚠️ Aucun paramètre détecté. Veuillez décrire correctement votre système.")
