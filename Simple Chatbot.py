#Simple Chatbot
def chatbot():
    print("Welcome to the Simple Chatbot!")
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm doing fine!",
        "what's your name": "I'm Chatbot!",
        "bye": "Goodbye!"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        response = responses.get(user_input, "I don't understand that.")
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
