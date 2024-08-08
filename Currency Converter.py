import requests

def currency_converter():
    print("Welcome to the Currency Converter!")
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                print("Amount must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    from_currency = input("Enter the from currency (e.g., USD): ").upper().strip()
    to_currency = input("Enter the to currency (e.g., EUR): ").upper().strip()

    api_key = "your_api_key_here"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if to_currency in data['conversion_rates']:
            exchange_rate = data['conversion_rates'][to_currency]
            converted_amount = amount * exchange_rate
            print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
        else:
            print(f"Currency code '{to_currency}' not found.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching exchange rate: {req_err}")
    except KeyError:
        print("Error: Invalid currency code or API response.")

if __name__ == "__main__":
    currency_converter()
