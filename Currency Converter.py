# Currency Converter
import requests

def currency_converter():
    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the from currency (e.g., USD): ").upper()
    to_currency = input("Enter the to currency (e.g., EUR): ").upper()

    api_key = "your_api_key_here"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        exchange_rate = data['conversion_rates'][to_currency]
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
    else:
        print("Error fetching exchange rate")

if __name__ == "__main__":
    currency_converter()
