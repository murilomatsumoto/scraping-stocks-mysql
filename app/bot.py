from botcity.web import WebBot, Browser, By
import os
from dotenv import load_dotenv
from models.ticker import Ticker
from utils.Email import Email


load_dotenv('app/config/.env')
email = Email()

lista_ativos = ['ITSA4', 'B3SA3', 'MDIA3']

def url_access(webbot:WebBot):
    webbot.headless = False
    webbot.browser = Browser.FIREFOX
    webbot.driver_path = os.getenv('firefox_path')
    webbot.browse(os.getenv('url_acesso'))
    webbot.wait(1000)
    return True
    
def main():
    dicio_stock = {}
    lista_dicio = []
    webbot = WebBot()
    stock = Ticker()
    acesso = url_access(webbot=webbot)
    if acesso:
        for ticker in lista_ativos:
            webbot.wait(500)
            campo_busca = webbot.find_element('papel', By.NAME)
            if campo_busca:
                campo_busca.send_keys(ticker)
                botao_exibir = webbot.find_element('botao', By.CLASS_NAME)
                if botao_exibir:
                    botao_exibir.click()
                webbot.wait(1000)
                cotacao_element = webbot.find_element('data destaque w3', By.CLASS_NAME)
                if cotacao_element:
                    stock.cotacao = cotacao_element.text
                table_indicadores_fund = webbot.find_element('//*[@class="w728"][3]/tbody', By.XPATH)
                if table_indicadores_fund:
                    indices = table_indicadores_fund.find_elements_by_tag_name('td')
                    if indices:
                        for indice in indices:
                            if indice:
                                class_indice = indice.get_attribute('class')
                                if class_indice == 'label w2':
                                    chave = indice.text
                                if class_indice == 'data w2':
                                    valor = indice.text
                                    dicio_stock[chave] = valor
                                    lista_dicio.append(dicio_stock)
                    # for tabela in table_indicadores:
                    #     if tabela:
                    #         tags_tabela = tabela.find_elements_by_tag_name('td')
                    #         if 'Indicadores fundamentalistas' in tags_tabela:
                    #             print('ok')
                                
            
                # p_l_element = webbot.find_element('')
                webbot.browse(os.getenv('url_acesso'))
                webbot.wait(1000)
        print(lista_dicio)        
        webbot.close_page()

if __name__ == '__main__':
    main()
