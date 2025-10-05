# test_smart_steel_tracker.py
# Very simple test for students to learn about testing

from smart_steel_tracker import load_data, compute_efficiency

def test_efficiency_values():
    data = [
        {"day": "Mon", "temperature": 1200, "output_tons": 200, "energy_used": 100},
        {"day": "Tue", "temperature": 1180, "output_tons": 150, "energy_used": 100}
    ]
    result = compute_efficiency(data)
    assert result[0]["efficiency"] == 2.0
    assert result[1]["efficiency"] == 1.5
