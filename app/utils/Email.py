import os
from dotenv import load_dotenv
from botcity.plugins.email import BotEmailPlugin, MailServers


load_dotenv()

 
class Email:
    def __init__(self):   
        self.SMTP = 'smtp.gmail.com'
        self.porta = 587
        self.usuario = os.getenv('email')
        self.senha = os.getenv('senha')

    def envia_email(self, assunto, email, destinatarios: list, arquivos: list = None):
        print('Gerando e-mail')

        try:
            # Conteúdo HTML
            msg = email
            # Instancia a variável
            botemail = BotEmailPlugin()
            # Configure IMAP com o servidor Gmail
            botemail.configure_imap("imap.gmail.com", 993)     
            # Configure SMTP
            botemail.configure_smtp(self.SMTP, self.porta)
            # Login
            botemail.login(self.usuario, self.senha)
        
            # Definindo os dados do mail
            to = destinatarios
            subject = assunto
            body = msg
            if arquivos:
                botemail.send_message(subject, body, to, use_html=True, attachments=arquivos)
            else:
                botemail.send_message(subject, body, to, use_html=True)

            botemail.disconnect()

        except Exception as e:
            print(f'Algum problema na transmissão do e-mail: {e.__traceback__}. Erro: {e}')
            
    def email_monitoramento(self, destinatarios:list, dicionario:list, vazio: bool = False):
        # log.info("Criando e-mail de notificação monitoramento")
        corpoEmail = ''
        if vazio == False:
            cabecalhoEmail = "<h4>Atenção, esse é um e-mail automático. Favor não responder!</h4><h4>Atualização diária das cotações da sua carteira:</h4>"
            corpoEmail += 'Atualização'
            for p in dicionario:
                corpoEmail += "digitar a acao"
                corpoEmail += "digitar a data"
                corpoEmail += f"<h4>colocar indicadores</h4><h4>"
                corpoEmail += '-------------------------------'
        else:
            cabecalhoEmail = "<h4>Atenção, esse é um e-mail automático. Favor não responder!</h4><h4>Atualização diária das cotações da sua carteira:</h4>"   
        
        rodapeEmail = "<br><br><h4>Atenciosamente.</h4><h4>Murilo Matsumoto Ramos - Desenvolvedor RPA.</h4>"

        # log.info("Enviando e-mail de notificação")
        email = Email()
        email.envia_email('Monitoramento - Carteira de Ações',cabecalhoEmail + corpoEmail + rodapeEmail, destinatarios)
        
