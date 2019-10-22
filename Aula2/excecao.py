#!/usr/bin/python3

# tratamento de exceções
# try:
#     int(input('Digite um valor: '))

# except ValueError as e:
#     print('Isso não é um número, tente novamente')

# finally:
#     print('eu sou o finally')


# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         if idade < 16:
#             print('Você não comprar bebida e nem ter um titulo de eleitor')
#             break
#         else:
#             if idade >= 16 and idade < 18:
#                 print('Você só pode ter titulo de eleitor')
#                 break
#             else:
#                 print('Você pode ter um titulo de eleitor e comprar bebida')
#             break
#         break

#     except Exception:
#         print('Isso não é um número, digite novamente.')
#         continue


# criar um campo de login onde o login com a palavra policial é proibida
# é gerado um erro NameError

while True:
    try:
        login = input('Digite o login: ')

        if login.title() == 'Policial':
            raise NameError('policial é uma palavra proibida')
        else:
            print(f'Bem vindo {login}, acesso permitido')
            break
    except NameError as e:
        print(e)
        continue
