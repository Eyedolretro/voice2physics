import re

def parse_voice_command(text: str):
    """
    Analyse le texte et extrait les paramètres physiques de base.
    Supporte : masse (kg), raideur/ressort (N/m)
    """
    params = {}
    
    # Masse
    match = re.search(r"masse\s+(\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if match:
        params["m"] = float(match.group(1))
    
    # Raideur
    match = re.search(r"raideur\s+(\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if match:
        params["k"] = float(match.group(1))
    
    return params
