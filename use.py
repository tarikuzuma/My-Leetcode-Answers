import requests

amount = 1
base_currency = 'USD'
target_currency = 'PHP'

# Make a request to the API to get the latest exchange rates
response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
data = response.json()

# Extract the exchange rate for the target currency
exchange_rate = data['rates'][target_currency]

# Perform the conversion
converted_amount = amount * exchange_rate

# Print the result
print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")