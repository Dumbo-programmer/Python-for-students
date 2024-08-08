import requests

def dictionary_lookup():
    print("Welcome to the Dictionary Lookup!")
    
    while True:
        word = input("Enter the word to look up (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Goodbye!")
            break
        elif not word.isalpha():
            print("Invalid input. Please enter a valid word.")
            continue

        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            definitions = data[0]['meanings'][0]['definitions']
            print(f"\nDefinitions for '{word}':")
            for idx, definition in enumerate(definitions, 1):
                print(f"{idx}. {definition['definition']}")
            print("\n")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Error fetching word definition: {req_err}")
        except (KeyError, IndexError):
            print("Word not found or invalid response format.")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    dictionary_lookup()
