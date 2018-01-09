import requests
base_url = 'https://api.fixer.io/latest?base=USD'
data = requests.get(base_url).json()
print(data)
