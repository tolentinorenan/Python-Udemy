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
"""
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

# HTTPS://DOCS.PYTHON.ORG/3/LIBRARY/FUNCTIONS.HTML#OPEN