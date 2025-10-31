#!/bin/bash
# =====================================================
# Voice2Physics – Setup et lancement en un clic
# =====================================================

PROJECT_DIR="$HOME/Documents/Projets/voice2physics"
cd "$PROJECT_DIR" || exit 1

echo "➡️ Supprimer l'ancien venv..."
rm -rf venv

# Vérifier pyenv
if ! command -v pyenv &> /dev/null
then
    echo "❌ pyenv non trouvé. Installe-le via Homebrew : brew install pyenv"
    exit 1
fi

# Installer Python 3.11 si nécessaire
if ! pyenv versions --bare | grep -q "^3.11.8$"; then
    echo "➡️ Installer Python 3.11.8 via pyenv..."
    pyenv install 3.11.8
fi

# Définir Python 3.11 pour le projet
pyenv local 3.11.8
PYTHON_PATH=$(pyenv which python)
echo "➡️ Créer un nouveau venv avec $PYTHON_PATH..."
$PYTHON_PATH -m venv venv

# Activer le venv
source venv/bin/activate
python --version

# Installer les dépendances
echo "➡️ Installation des packages..."
brew install portaudio >/dev/null 2>&1 || echo "PortAudio déjà installé"
pip install --upgrade pip
pip install -r requirements.txt

# Lancer Streamlit
echo "➡️ Lancer Streamlit..."
streamlit run app/streamlit_app.py
