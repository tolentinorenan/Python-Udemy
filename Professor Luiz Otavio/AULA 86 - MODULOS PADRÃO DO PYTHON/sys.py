"""
PARA INSTALAR UM MODULO, VAMOS NO TERMINAL E EXECUTA O COMANDO PIP, EXEMPLO:
PIP INSTALL MYSQL
PIP UNISTALL MYSQL - PARA REMOVER
"""


"""
EXEMPLO 1
"""
# import sys # IMPORTAMOS O MODULOS INTEIRO
# from sys import platform # importa uma função especifica do modulo sys
# from sys import platform as so # cria um apelido para platform

# print(platform)  # printa a plataforma que esta executando o codigo

"""
EXEMPLO 2
"""
# import random # GERA NUMERO ALEATORIOS
#
# for i in range(10):
#     print(random.randint(0,10)) # gera numeros aleatorios entre 0 e 10


"""
EXEMPLO 3
"""

# from random import randint as randint_original
#
# def randint (*args):
#     return 'hahahaha'
#
# for i in range(10):
#     print(randint_original(0,10))
#
# print(randint)

"""
EXEMPLO 4
"""
from random import randint, random  # se quisermos importar mais de um modulo da função

for i in range(10):
    print(randint(0,10), random())  # RANDOM GERA NUMERO ALEATORIO TB POREM ENTRE 0 E 1
