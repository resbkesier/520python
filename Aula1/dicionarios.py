import json
# apresentacao = {
#     'pirata': 'argh',
#     'paulista': 'Salve',
#     'carioca': 'Eae',
#     'acre': 'barulhos'
# }


# endereco = {'cep': '06763320',
#             'logradouro': 'Rua Waldemar Tracchi',
#             'numero':'128',
#             'quantidade de buracos': 2}

# print(endereco)

# endereco.__setitem__('quantidade de postes', 4)

# endereco['transito'] = 'médio'

# print(endereco)


# print(endereco['logradouro'])

# print(endereco['quantidade de buracos'] + 10)

# lista = list(endereco.keys())

# lista[0] = '666666666666666666666666'

# print(lista)

# criar o seguinte dicionario:
##
# acessar o estado de são paulo, e mostrar a quantidade de pessoas em milhoes
# Acessar o estado do rio de janeiro e mostrar a região
# Modificar o nome do rioDeJaneiro para Rio de Janeiro
# Adicionar minasgerais ao dicionário com as seguintes características:
#
# nome -  minas gerais
# região - sudeste
# municipios - 853
# populacao - 20,87


#mostrar a população de minas gerais em milhões


dados = {
    'cidade': {
        'saoPaulo': {
            'nome': 'Sao Paulo',
            'regiao': 'sudeste',
                    'municipios': 645,
                    'populacao': 12.18
        },
        'rioDeJaneiro': {
            'nome': 'rioDeJaneiro',
            'regiao': 'sudeste',
            'municipios': 92,
                    'populacao': 6.32
        }
    }
}


# print(dados['cidade']['saoPaulo']['populacao'] * 1000000)
# print(dados['cidade']['rioDeJaneiro']['regiao'])
# dados['cidade']['rioDeJaneiro']['nome'] = 'Rio de Janeiro'
# dados['cidade']['minasGerais'] = {
#             'nome': 'Minas Gerais',
#             'regiao': 'sudeste',
#             'municipios': 853,
#                     'populacao': 20.87
#         }
# print(dados)
# print(dados['cidade']['minasGerais']['populacao'] * 100000)

print(json.dumps(dados, sort_keys=True, indent=4))