#!/usr/bin/python3

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Você não comprar bebida e nem ter um titulo de eleitor')
else:
    if idade >= 16 and idade < 18:
        print('Você só pode ter titulo de eleitor')
    else:
        print('Você pode ter um titulo de eleitor e comprar bebida')
    

    