from sympy import symbols, Eq, solve

def compute_physics(params: dict):
    """
    Calcule les valeurs physiques de base pour un système masse-ressort.
    Retourne un dictionnaire avec formule et résultat.
    """
    m_val = params.get("m", 1.0)   # kg
    k_val = params.get("k", 10.0)  # N/m

    m, k, x = symbols("m k x")
    f = k * x
    eq = Eq(f, m * 9.81)  # P = m*g
    sol = solve(eq.subs({m: m_val, k: k_val}), x)
    
    return {
        "formule": "F = k*x",
        "masse (kg)": m_val,
        "raideur (N/m)": k_val,
        "déplacement (m)": float(sol[0])
    }
