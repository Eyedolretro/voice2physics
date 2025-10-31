def compute_physics(params):
    """
    Effectue les calculs physiques selon le type de système.
    Types supportés : ressort, triangle, levier, pendule
    """
    m = params.get("m", 1.0)
    k = params.get("k", 1.0)
    system_type = params.get("type", "ressort")

    results = {"masse (kg)": m, "type": system_type}
    formulas = {}

    if system_type == "ressort":
        # Exemple : F = 100 N appliquée
        F = 100
        x = F / k
        results.update({
            "raideur (N/m)": k,
            "force appliquée (N)": F,
            "déplacement (m)": round(x,3)
        })
        formulas["Loi de Hooke"] = "F = k * x"

    elif system_type == "triangle":
        # Exemple : triangle sur plan horizontal avec poids m*g
        g = 9.81
        W = m * g
        results["poids (N)"] = round(W,3)
        formulas["Poids"] = "W = m * g"

    elif system_type == "levier":
        # Exemple simple levier : F1*L1 = F2*L2
        L1 = 1.0
        L2 = 0.5
        F2 = m * 9.81
        F1 = F2 * L2 / L1
        results.update({"F1 (N)": round(F1,3), "F2 (N)": round(F2,3), "L1 (m)": L1, "L2 (m)": L2})
        formulas["Loi du levier"] = "F1*L1 = F2*L2"

    elif system_type == "pendule":
        # Petit pendule simple
        g = 9.81
        L = 1.0
        T = 2 * 3.1416 * (L/g)**0.5
        results.update({"longueur (m)": L, "période (s)": round(T,3)})
        formulas["Période pendule"] = "T = 2π√(L/g)"

    else:
        results["info"] = "Système non reconnu, calculs par défaut"
    
    return results, formulas

def export_for_matlab(results, filename="export_matlab.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    return filename
