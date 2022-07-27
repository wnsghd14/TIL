import requests

order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers).json()
print(response.get('data').get('closing_price'))