#!/usr/bin/python3

# criar tupla
print('1 - ')
tupla_al = (1,2,'casa',5,7,45,32,2, 'a','d', 'x', 's', 'c')
print(tupla_al)
# acessar primeiro indice
print('\n2 - ')
print(tupla_al[0])
# Mostrar o terceiro indice em formato title
print('\n3 - ')
print(tupla_al[2].title())
# Mostrar a terceira letra do terceiro Indice
print('\n4 - ')
print(tupla_al[2][2])
# Converter a tupla para uma lista e mudar o primeiro indice para outro valor
print('\n5 - ')
lista_al = list(tupla_al)
lista_al[0] = 'teste'
print(lista_al)