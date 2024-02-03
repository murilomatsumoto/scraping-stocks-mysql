from datetime import datetime

data_atual = datetime.today()
data_formatada = data_atual.strftime('%Y-%m-%d')
print(data_formatada)

price = '34,2'


json_update = {
"date": data_formatada,
"price": float(price.replace(',', '.')),
"stock": 2
}

print(json_update)