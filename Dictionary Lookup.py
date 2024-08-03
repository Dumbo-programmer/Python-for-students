#Dictionary Lookup
import requests

def dictionary_lookup():
    print("Welcome to the Dictionary Lookup!")
    word = input("Enter the word to look up: ")
    api_key = "your_api_key_here"

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        definitions = data[0]['meanings'][0]['definitions']
        for idx, definition in enumerate(definitions, 1):
            print(f"{idx}. {definition['definition']}")
    else:
        print("Word not found")

if __name__ == "__main__":
    dictionary_lookup()
