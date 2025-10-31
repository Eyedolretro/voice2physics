from src.parser_voice import parse_voice_command
from src.physics_engine import compute_physics

def test_compute_physics():
    text = "masse 2 kg, raideur 50 N/m"
    params = parse_voice_command(text)
    results = compute_physics(params)
    
    assert "déplacement (m)" in results
    assert results["masse (kg)"] == 2
    assert results["raideur (N/m)"] == 50

    print("Test passé ✅")
    
if __name__ == "__main__":
    test_compute_physics()
