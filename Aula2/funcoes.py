#! usr/bin/python3
# import fibonacci

# def media(x, y):
#     return (x + y) / 2


# fibonacci.calcula()

# var = 'Renato'

# def mudaNome():
#     global var
#     var  = 'Douglas'
#     print(var)

# mudaNome()

# print(var)


# *args
# def media_nacional(*media):
#     x = [numeros for numeros in media]
    
#     print(sum(x) / len(x))
    
# media_nacional(150, 500, 250)

# **Kargs


# def teste(**valores):
#     '''essa é uma docstring'''
#     print(valores)

# teste(var1 = 'teste', var2 = 'teste2')

# lambda

# potencia = lambda x,y: x ** y

# print(potencia(2, 2))




def teste(x, y):
    lista = [lambda x: x ** 5, lambda y: y * x]
    for a in lista:
        print(a(x), a(y))

teste(2, 5)