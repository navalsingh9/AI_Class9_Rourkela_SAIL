# iron_to_steel_simulator.py
# Basic math and variables example

print("⚙️ Iron to Steel Converter Simulation")
iron_ore = float(input("Enter iron ore quantity (in tons): "))
carbon = float(input("Enter carbon added (in %) : "))

# simple made-up formula
steel_output = iron_ore * (1 - (carbon / 100)) * 0.9

print("Approx. steel produced:", round(steel_output, 2), "tons")
print("This shows how purity and carbon content affect steel strength 💪")
