#!/bin/bash

# Chemin projet
PROJECT_DIR="$HOME/Documents/Projets/voice2physics"

echo "➡️ Aller dans le projet..."
cd "$PROJECT_DIR" || exit 1

echo "➡️ Supprimer ancien venv..."
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

echo "➡️ Définir Python 3.11 pour le projet..."
pyenv local 3.11.8

PYTHON_PATH=$(pyenv which python)
echo "➡️ Créer le venv avec $PYTHON_PATH..."
$PYTHON_PATH -m venv venv

echo "➡️ Activer le venv..."
source venv/bin/activate

echo "➡️ Mettre pip à jour..."
pip install --upgrade pip

echo "➡️ Installer les dépendances..."
pip install -r requirements.txt

echo "➡️ Lancer Streamlit..."
streamlit run app/streamlit_app.py
