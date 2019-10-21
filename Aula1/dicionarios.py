apresentacao = {
    'pirata': 'argh',
    'paulista': 'Salve',
    'carioca': 'Eae',
    'acre': 'barulhos'
}



endereco = {'cep': '06763320',
            'logradouro': 'Rua Waldemar Tracchi',
            'numero':'128',
            'quantidade de buracos': 2}

print(endereco)

endereco.__setitem__('quantidade de postes', 4)

endereco['transito'] = 'médio'

print(endereco)



print(endereco['logradouro'])

print(endereco['quantidade de buracos'] + 10)

lista = list(endereco.keys())

lista[0] = '666666666666666666666666'

print(lista)