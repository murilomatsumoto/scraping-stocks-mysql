import requests
from datetime import datetime

class ApiStocks():

    @staticmethod
    def api_post(json_data, ticker):
        url_new_stock = 'http://localhost:8000/stocks/'
        response = requests.post(url_new_stock, json=json_data)

        if response.status_code == 201:
            data = response.json()  # Se a resposta é JSON
            new_stock_id = data.get('id')
            if new_stock_id is not None:
                print('Ação cadastrada, retornando ID')
                return new_stock_id
            else:
                print("Erro: ID não encontrado na resposta.")
            print(data)
        elif response.status_code == 400:
            error_response = response.json()
            result_error = error_response['ticker']
            if result_error[0] == 'stocks with this ticker already exists.':
                print('Ação já cadastrada, retornando ID')
                url_get_ticker_id = f'{url_new_stock}{ticker}'
                response = requests.get(url_get_ticker_id)
                if response.status_code == 200:
                    data = response.json()
                    stock_id = data.get('id')
                    print(f'stock id: {stock_id}, stock: {ticker}')
                    return stock_id


    @staticmethod
    def update_stock_price(id_stock, info):
        url_update_fundamentus = f'http://localhost:8000/stockprices/'
        data_atual = datetime.today()
        data_formatada = data_atual.strftime('%Y-%m-%d')
        
        json_update = {
        "date": data_formatada,
        "price": float(info[1].replace(',', '.')),
        "stock": id_stock,
        "p_l": float(info[2].replace('.', '').replace(',', '.')),
        "p_vp": float(info[3].replace('.', '').replace(',', '.')),
        "dividend_y": float(info[5].replace('.', '').replace(',', '.').replace('%', '')),
        }
        print(json_update)
        response = requests.post(url_update_fundamentus, json=json_update)

        print(response.status_code)
        if response.status_code == 201:
            print(f'preço da ação do dia {data_formatada} cadastrado com sucesso')
        elif response.status_code == 400:
            error_response = response.json()
            print(error_response)
            result_error = error_response['non_field_errors']
            if result_error[0] == 'The fields stock, date must make a unique set.':
                url_update_date_stock = f'{url_update_fundamentus}{id_stock}/{data_formatada}/'
                response = requests.put(url_update_date_stock, json=json_update)
                if response.status_code == 200:
                    print(f'preço da ação do dia {data_formatada} atualizado com sucesso')
            
# json_data = {'name': "", 'ticker': 'ITUB3'}
# ApiStocks.api_post(json_data=json_data, ticker=json_data['ticker'])
# ApiStocks.update_stock_price(443)
