import random
import requests

# Example API Key for demonstration (replace with a real API key for functionality)
WEATHER_API_KEY = "your_weather_api_key_here"

def get_weather(city):
    """Fetch weather information from an API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            return f"The current temperature in {city} is {temp}°C with {weather}."
        else:
            return "Sorry, I couldn't fetch the weather information."
    except Exception as e:
        return f"An error occurred: {e}"

def chatbot():
    print("Welcome to the Advanced Chatbot!")
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing fine! How about you?",
        "what's your name": "I'm Chatbot! What's your name?",
        "bye": "Goodbye! Have a great day!",
    }
    user_info = {}
    conversation_history = []

    while True:
        user_input = input("You: ").strip().lower()
        conversation_history.append(f"You: {user_input}")

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            conversation_history.append("Chatbot: Goodbye! Have a great day!")
            break
        
        if user_input.startswith("weather in"):
            city = user_input.split("weather in", 1)[1].strip()
            weather_response = get_weather(city)
            print(f"Chatbot: {weather_response}")
            conversation_history.append(f"Chatbot: {weather_response}")
            continue

        if user_input.startswith("my name is"):
            name = user_input.split("my name is", 1)[1].strip()
            user_info['name'] = name
            response = f"Nice to meet you, {name}!"
            print(f"Chatbot: {response}")
            conversation_history.append(f"Chatbot: {response}")
            continue

        if "name" in user_info:
            name = user_info['name']
            response = responses.get(user_input, f"I don't understand '{user_input}'.")
            response = response.replace("I'm Chatbot!", f"I'm Chatbot, nice to talk to you again, {name}!")
        else:
            response = responses.get(user_input, f"I don't understand '{user_input}'.")

        print(f"Chatbot: {response}")
        conversation_history.append(f"Chatbot: {response}")

    # Optionally, you can save the conversation history to a file
    with open("conversation_history.txt", "w") as f:
        for line in conversation_history:
            f.write(line + "\n")

if __name__ == "__main__":
    chatbot()
