dicio = {
    "papel": "SQIA3",
    "cotação": "27,37",
    "pl": "2.744,55",
    "pvp": "3,76",
    "psr": "3,666",
    "divyield": "0,20%",
    "pativo": "1,500",
    "pcapgiro": "27,05",
    "pebit": "43,24",
    "pativ_circliq": "-3,72",
    "evebit": "47,04",
    "evebitda": "16,48",
    "mrg_ebit": "8,48%",
    "mrg_líq": "0,45%",
    "liq_corr": "1,44",
    "roic": "4,04%",
    "roe": "0,14%",
    "liq2meses": "35.787.700,00",
    "patrim_líq": "639.749.000,00",
    "dívbrut_patrim": "0,67",
    "cresc_rec5a": "46,25%",
}
print(len(list(dicio.keys())))
print(len(list(dicio.values())))

dados = ('SQIA3', '27,37', '2.744,55', '3,76', '3,666', '0,20%', '1,500', '27,05', '43,24', '-3,72', '47,04', '16,48', '8,48%', '0,45%', '1,44', '4,04%', '0,14%', '35.787.700,00', '639.749.000,00', '0,67', '46,25%')
from db.mysql import Mysql
# print(len(dados))

# Mysql().consulta_mysql('ativos')
Mysql().inserir_registro(tabela='ativos', dados=dados)
# ativos = Mysql().describe('ativos')
# print(ativos)
# soma = 0
# for item in ativos:
#     print(item[0])
#     soma += 1
# print(soma)