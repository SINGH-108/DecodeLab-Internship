import json
import os
MEMORY_FILE = "C:/Users/shristi singh/Downloads/chatbot_memory.json"
def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as file:
                return json.load(file)
        except Exception:
            return {"user_name": "Guest"}
    return {"user_name": "Guest"}
def save_memory(name):
    data = {"user_name": name}
    try:
        with open(MEMORY_FILE, "w") as file:
            json.dump(data, file)
        print(f"-- System: Memory synchronized to {MEMORY_FILE} --")
    except Exception as e:
        print(f"-- Error: Could not save memory. {e} --")
def main():
    global MEMORY_FILE
    print("--- DecodeLabs Chatbot: PROFESSIONAL EDITION ---")
    if not os.path.exists(os.path.dirname(MEMORY_FILE)):
        MEMORY_FILE = "chatbot_memory.json"
    memory = load_memory()
    user_name = memory["user_name"]
    print(f"Chatbot: Welcome back, {user_name}!")
    intents = {
        "status": "I am running smoothly on a rule-based engine.",
        "purpose": "I demonstrate deterministic AI logic and file I/O.",
        "help": "Tell me your name or ask who you are!"
    }
    while True:
        user_input = input(f"({user_name}) You: ").lower().strip()
        for char in "!.,?;":
            user_input = user_input.replace(char, "")
        user_input = user_input.strip()
        if user_input in ["exit", "bye"]:
            print(f"Chatbot: Goodbye, {user_name}!")
            break
        if not user_input:
            continue
        if "my name is" in user_input and len(user_input) > 10:
            name_parts = user_input.split("my name is")
            potential_name = name_parts[1].strip()
            if potential_name:
                user_name = potential_name.capitalize()
                save_memory(user_name)
                print(f"Chatbot: I'll remember you as {user_name}.\n")
            continue
        if any(x in user_input for x in ["who am i", "who i am", "what is my name"]):
            print(f"Chatbot: You are {user_name}.\n")
            continue
        response = intents.get(user_input, f"I don't have a rule for that yet, {user_name}.")
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    main()