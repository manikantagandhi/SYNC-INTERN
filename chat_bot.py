import random

personality = {
    "greetings": ["Hello!", "Hi there!", "Hey!", "How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye now!"],
    "responses": {
        "how are you": ["I'm just a chatbot, but thanks for asking!", "I'm here to assist you."],
        "help": ["I can provide information or answer questions. Just ask!", "What do you need help with?"],
        "default": ["I'm not sure I understand. Can you please rephrase your question?", "I didn't catch that. Could you try again?"],
    }
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return random.choice(personality["greetings"])
    elif user_input in ["goodbye", "bye"]:
        return random.choice(personality["goodbye"])

    else:
        response_list = personality["responses"].get(user_input, random.choice(personality["responses"]["default"]))
        return random.choice(response_list)  # Randomly select a response from the list

# Step 7: Test the chatbot
print("Chatbot: " + chatbot_response("hello"))

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: " + chatbot_response("goodbye"))
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot: " + response)
