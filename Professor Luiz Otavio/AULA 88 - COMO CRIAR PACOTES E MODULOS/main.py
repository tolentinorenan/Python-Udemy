""""
"""

"""
E-COMMERCE
"""
preco = 49.90
"""
EXEMPLO 1
"""
#  import vendas.calc_precos
# preco_com_aumento = vendas.calc_precos.aumento(valor = preco, porcentagem = 15)

"""
EXEMPLO 2
"""
# from vendas import calc_precos
# preco_com_aumento = calc_precos.aumento(valor = preco, porcentagem = 15)

"""
EXEMPLO 3 
"""
# from vendas.calc_precos import aumento,reducao
#
# preco_com_aumento = aumento(valor=preco, porcentagem=15)
# preco_com_reducao = reducao(valor=preco, porcentagem=15)


"""
EXEMPLO 4 
"""

from vendas.calc_precos import aumento, reducao
from vendas.formata import preco

preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)