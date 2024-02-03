from datetime import datetime
import requests

data_atual = datetime.today()
data_formatada = data_atual.strftime('%Y-%m-%d')
print(data_formatada)

info = ('OPCT3', '6,12', '-18,22', '1,54', '0,791', '0,00%', '0,505', '5,88', '5,93', '-1,35', '10,68', '4,84', '13,34%', '5,27%', '1,41', '9,99%', '-8,45%', '3.991.470,00', '794.548.000,00', '1,56', '52,49%')
url_update_fundamentus = f'http://localhost:8000/stockprices/'
json_update = {
"date": data_formatada,
"price": float(info[1].replace(',', '.')),
"stock": 10,
"p_l": float(info[2].replace('.', '').replace(',', '.')),
"p_vp": float(info[3].replace('.', '').replace(',', '.')),
"dividend_y": float(info[5].replace('.', '').replace(',', '.').replace('%', '')),
}
print(json_update)

url_update_date_stock = f'{url_update_fundamentus}{10}/{data_formatada}/'
print(url_update_date_stock)
response = requests.put(url_update_date_stock, json=json_update)
print(response.status_code)