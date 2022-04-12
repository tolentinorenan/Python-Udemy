import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

lista = [1,2,3,4,5]

# print(__name__)  # ELA RETORNA O NOME DO MODULO APENAS SE O MODULO SE O MODULO ESTIVER SENDO IMPORTADO POR OUTRO


if __name__ == '__main___':  # PARA O QUE EU ESCREVER LOGO ABAIXO NAO SEJA IMPORTADO PARA OUTROS MODULOS
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
