#! /usr/bin/python3


# x = 1

# while x <  100:
#     print('Socorro')
#     x += 1
    

# print(x)

# lista = ['arroz', 'feijao', 'macarrao', 'banana', 'maça', 'laranja']

# for item in lista:
#     print(item)


# print(item)

#pegar uma lista de numeros, multiplicar por 3 cada numero usando o for e colocar os 
# valores em uma variavel

numeros = [1,2,3,4,5,6,7,8,9,2]
lista_multiplicados = []
for numero in numeros:
    lista_multiplicados.append(numero * 3)
print(lista_multiplicados)
    
#ou

x = [i*3 for i in numeros]
print(x)

lista = []
for numero in range(6):
    lista.append(numero * 3)
    print(numero)
print(lista)