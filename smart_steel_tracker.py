# smart_steel_tracker.py
# A simple project showing data and AI-style logic
import csv
import matplotlib.pyplot as plt

def load_data(filename):
    data = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["temperature"] = float(row["temperature"])
            row["output_tons"] = float(row["output_tons"])
            row["energy_used"] = float(row["energy_used"])
            data.append(row)
    return data

def compute_efficiency(data):
    for r in data:
        r["efficiency"] = round(r["output_tons"] / r["energy_used"], 2)
    return data

def show_chart(data):
    days = [r["day"] for r in data]
    eff = [r["efficiency"] for r in data]
    plt.plot(days, eff, marker="o")
    plt.title("RSP Smart Steel Efficiency Tracker")
    plt.xlabel("Day")
    plt.ylabel("Efficiency (tons per energy unit)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    data = load_data("production_data_rsp.csv")
    data = compute_efficiency(data)
    print("Top Efficient Days:")
    sorted_data = sorted(data, key=lambda x: x["efficiency"], reverse=True)
    for d in sorted_data[:3]:
        print(d["day"], "→", d["efficiency"])
    show_chart(data)
