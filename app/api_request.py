import requests

url = 'http://localhost:8000/stocks/'
response = requests.post(url, {'name': 'COPEL PNB', 'ticker': 'CPLE6'})

if response.status_code == 200:
    data = response.json()  # Se a resposta é JSON
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
