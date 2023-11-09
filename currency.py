#before executing run this command in terminal
#pip install requests
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

if __name__ == "__main__":
    base_currency = input("Enter the currency you want to convert: ").upper()
    target_currency = "INR"
    amount = float(input(f"Enter the amount in {base_currency}: "))
    
    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        result = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {result} {target_currency}")
    except KeyError:
        print("Invalid currency code or unable to fetch data. Please try again.")
