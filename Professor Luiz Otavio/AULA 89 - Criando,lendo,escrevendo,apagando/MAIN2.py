import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1)  # CONVERTE PARA JSON PARA TROCAR INFORMAÇÕES

with open('abc.json', 'w+') as file:
    file.write(d1_json)
