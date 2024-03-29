from botcity.web import WebBot, Browser, By
import os
from dotenv import load_dotenv
from models.ticker import Ticker
from utils.Email import Email
import botcity.web.parsers
from api_request import ApiStocks
from db.mysql import Mysql



load_dotenv('app/config/.env')

def url_access(webbot:WebBot):
    webbot.headless = False
    webbot.browser = Browser.FIREFOX
    webbot.driver_path = os.getenv('firefox_path')
    webbot.browse(os.getenv('url_acesso'))
    webbot.wait(1000)
    return True
    
def main():

    webbot = WebBot()
    stock = Ticker()
    acesso = url_access(webbot=webbot)
    if acesso:
        webbot.wait(500)
        busca_empresa = webbot.find_element('//*[@class="avancada"]/span/a[1]', By.XPATH)
        print('acessando busca avançada')
        if busca_empresa:
            busca_empresa.click()
            webbot.wait(1000)
            botao_buscar = webbot.find_element('buscar', By.CLASS_NAME)
            if botao_buscar:
                botao_buscar.click()
                print('clicando em buscar')
                webbot.wait(1000)
                tabela_ativos = webbot.find_element('resultado', By.ID)
                print('capturando resultado')
                dict_table_ativos = botcity.web.parsers.table_to_dict(tabela_ativos)
            webbot.browse(os.getenv('url_acesso'))
            webbot.wait(1000)
            for dicio in dict_table_ativos:
                info = tuple(dicio.values())     
                try:
                    print(info)
                    json_data = {'name': "", 'ticker': info[0]}
                    # print(json_data)
                    id_stock = ApiStocks.api_post(json_data=json_data,  ticker=json_data['ticker'])
                    
                    if id_stock:
                        
                        ApiStocks.update_stock_price(id_stock=id_stock, info=info)
                        
                        
                except:
                    pass
    webbot.close_page()

if __name__ == '__main__':
    main()
