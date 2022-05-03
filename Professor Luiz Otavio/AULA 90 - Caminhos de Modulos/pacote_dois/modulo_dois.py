"""
"""
"""
A IMPORTAÇÃO A SEGUIR NÃO VAI FUNCIONAR POIS NO PYTHON AS IMPORTAÇÕES
FUNCIONAM DO ARQUIVO DE ENTRADA PARA FRENTE.( ARQUIVO DE ENTRADA É TODO AQUELE QUE É 
CONSIDERADO __MAIN__ O PRIMEIRO A SER EXECUTADO ).
ENTAO TEMOS QUE EXECUTAR O MAIN 
"""


from pacote_um.modulo_um import variavel1
variavel2 = 'variavel2'

print(variavel1)


"""
UM HACKEZINHO PARA ENGANAR O PYTHON SERIA AS LINHAS DE CODIGOS ABAIXO
Vamos tentar importar o Sys e o Os
Vamos pegar o sys.path e adicionar o caminho completo da pasta superior
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise