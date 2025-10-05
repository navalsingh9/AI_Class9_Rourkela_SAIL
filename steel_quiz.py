# steel_quiz.py
# Simple 3-question quiz using if-else

print("🧠 Steel Quiz Time!")
score = 0

ans = input("1️⃣ What is RSP short for? ").strip().lower()
if "rourkela" in ans and "steel" in ans:
    score += 1

ans = input("2️⃣ Steel is made mainly from which metal? (a) Copper (b) Iron (c) Aluminium: ").lower()
if ans == "b" or "iron" in ans:
    score += 1

ans = input("3️⃣ Name one thing around you made of steel: ")
if ans:
    score += 1

print(f"✅ You scored {score} out of 3!")
if score == 3:
    print("Excellent! You’re a Steel City Champion 🏆")
else:
    print("Good try — keep learning about RSP and AI!")
