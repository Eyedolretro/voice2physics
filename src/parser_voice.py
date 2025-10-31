def parse_voice_command(text):
    params = {}

    text_lower = text.lower()

    # Formes géométriques
    if "rond" in text_lower or "cercle" in text_lower:
        params["type"] = "cercle"
    elif "triangle" in text_lower:
        params["type"] = "triangle"
    elif "levier" in text_lower:
        params["type"] = "levier"
    else:
        # Système physique classique
        import re
        masse_match = re.search(r"masse (\d+\.?\d*) ?kg", text_lower)
        raideur_match = re.search(r"raideur (\d+\.?\d*) ?n/m", text_lower)
        if masse_match:
            params["masse (kg)"] = float(masse_match.group(1))
        if raideur_match:
            params["raideur (N/m)"] = float(raideur_match.group(1))
        params["type"] = "ressort" if params else "inconnu"

    return params
