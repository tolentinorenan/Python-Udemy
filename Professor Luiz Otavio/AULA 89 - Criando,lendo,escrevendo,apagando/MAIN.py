# file = open('abc.txt', 'w+')  # 1 - cria arquivo abc.txt 2 - w+ = leitura/escrita
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0,0) # MOVE O CURSOR PARA O COMEÇO DO ARQUIVO PARA LER NOVAMENTE
# print('Lendo Linhas: ')
# print(file.read())
# print('############')
#
# file.seek(0,0)
# print(file.readline(), end='') # LE LINHA POR LINHA  # END NAO QUEBRA ALINHA
# print(file.readline(), end='') # LE LINHA POR LINHA
# print(file.readline(), end='') # LE LINHA POR LINHA
#
# file.seek(0,0)
# #  print(file.readlines())  # ESSA LE TODAS AS LINHAS E COLOCA EM UMA LIST
# for linha in file.readlines():
#     print(linha,end='')  # PODEMOS FAZER UM FOR AQUI TAMBEM
#
# file.close()  # terminou de trabalhar FECHA !

"""
"""
"""
EXEMPLO 2
"""
# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

"""
EXEMPLO 3 - GERENCIADOR DE CONTEXTO
A DIFERENÇA QUE NAO PRECISA MANDAR FECHAR O ARQUIVO
W - ESCREVE
R - APENA LE
A -  ATIVA O APPEND MODE, ADICIONA COISAS NO ARQUIVO SEM APAGAR 
"""
# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())

"""
EXEMPLO 4 - CRIANDO OUTRA LINHA
DIFERENÇA ENTRE A+ E W+ É QUE O W+ APAGA AS ESCRITAS TODA VEZ QUE É EXECUTADO 
A+ VAI ESCREVENDO NA LINHA DEBAIXO SEM APAGAR OS ANTERIORES
"""
with open('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.write('Outra linha2\n')
    print(file.read())

import os

os.remove('abc.txt') # APAGA O ARQUIVO :(



# HTTPS://DOCS.PYTHON.ORG/3/LIBRARY/FUNCTIONS.HTML#OPEN