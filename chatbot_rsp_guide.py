# chatbot_rsp_guide.py
# A simple rule-based chatbot about Rourkela Steel Plant

print("🤖 Hi! I'm RSP Bot — your tour guide for Rourkela Steel Plant!")
while True:
    q = input("Ask me something (type 'bye' to exit): ").lower()
    if "bye" in q:
        print("Goodbye! Visit RSP again soon 👋")
        break
    elif "where" in q and "located" in q:
        print("📍 RSP is in Rourkela, Odisha — near the Koel and Sankha rivers.")
    elif "year" in q:
        print("🏗️ Rourkela Steel Plant began production in 1959.")
    elif "owner" in q or "sail" in q:
        print("💼 RSP is owned by Steel Authority of India Limited (SAIL).")
    elif "product" in q:
        print("🔩 RSP makes steel for construction, railways, and industries.")
    else:
        print("🤔 I’m not sure, but I’ll learn more as I grow!")
