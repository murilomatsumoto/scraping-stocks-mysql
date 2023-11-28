import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("app/config/.env")


class Mysql:
    def __init__(self) -> None:
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.host = os.getenv("host")
        self.database = os.getenv("database")
        self.conn = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
        )

    def consulta_mysql(self, tabela):
        cursor = self.conn.cursor()
        cursor.execute(f"select * from {tabela}")
        # Recuperar os resultados
        resultados = cursor.fetchall()

        # Iterar pelos resultados
        for registro in resultados:
            print(registro)

        # Fechar o cursor e a conexão
        cursor.close()
        self.conn.close()

    def inserir_registro(self, tabela, dados):
        cursor = self.conn.cursor()

        # Construir a consulta SQL de inserção
        query = f"INSERT INTO {tabela} (papel, cotação, pl, pvp, psr, divyeld, pativo, pcapgiro, pebit, pativ_circliq, evebit, evebitda, mrg_ebit, mrg_líq, liq_corr, roic, roe, liq2meses, patrim_líq, dívbrut_patrim, cresc_rec5a) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Substitua "coluna1", "coluna2", "coluna3" pelos nomes das colunas da tabela

        # Executar a consulta de inserção
        cursor.execute(query, dados)

        # Confirmar a transação
        self.conn.commit()

        # Fechar o cursor
        cursor.close()

    def describe(self, tabela):
        # Criar um cursor para executar comandos SQL
        cursor = self.conn.cursor()

        # Executar a consulta DESCRIBE ou SHOW COLUMNS
        cursor.execute(f"DESCRIBE {tabela}")  # Ou cursor.execute(f"SHOW COLUMNS FROM {table_name}")

        # Recuperar os resultados
        columns_description = cursor.fetchall()

        # Fechar o cursor e a conexão
        cursor.close()
        self.conn.close()

        return columns_description