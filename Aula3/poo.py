#!/usr/bin/python3
import random
from bancodedados import BancoMelhor
# POO - Programação orientada a objetos

#Criação de uma classe

# class Foo():
#     pass

#Atributos

# class Humano():
#     nome = 'Daniel'
#     idade = 24
#     altura = 1.80
#     peso = 'Desconhecido'

#Metodos

# class Funcionario():
#     def funcao(self): #Self é a referência ao objeto
#         pass

#objeto
#para criar um objeto precisamos realizar uma instância da classe
# objeto = Foo()

#Criando uma classe com métodos

# class Fazendeiro():
#     def carpinar(self): 
#         print('Carpinando...')

# #Criando um objeto fazendeiro
# gerson = Fazendeiro()
# #Utilizando o método de carpinagem
# gerson.carpinar() #Chamando o método

# #Criando uma classe com métodos e atributos
# class Meteorologista():
#     a = 3
#     #Método construtor, usado para passar atributos para os métodos
#     def __init__(self,nome,idade,tv = True):
#         #Definindo os atributos
#         self.nome = nome
#         self.idade = idade
#         self.tv = tv
#         self.emissora = 'Band'
#     #Definir métodos
#     def previsao(self):
#         print(f'Boa tarde, meu nome é {self.nome}')
#         if self.tv == True:
#             print(f'Faço parte da Emissora {self.emissora}')
#         print(f'Hoje está nublado')
#         print(f'Só pra constar eu tenho {self.idade}')
#     def trocaNome(self,nome):
#         self.nome = nome
#     # @classmethod
#     # def oi():
#     #     print('oi')
#     @staticmethod
#     def oi(self):
#         print('oi')

# laura = Meteorologista('Laura',43,False)
# laura.previsao()
# laura.trocaNome('Rapadura')
# laura.previsao()
# print(laura.a)
# laura.oi()

## Faça um cachorro com os seguintes atributos:
# nome
# idade
# sexo
# cor
# raca
#
# E os seguintes métodos
# latir
# comer
# caçar
# trocar nome

# class Cachorro():
#     def __init__(self,nome,idade,sexo,cor='Caramelo',raca='vira lata'):
#         self.nome = nome
#         self.idade = idade
#         self.sexo = sexo
#         self.cor = cor
#         self.raca = raca
#     def apresentacao(self):
#         atributos = [
#             self.nome, self.idade, self.sexo, self.cor,
#             self.raca
#         ]
#         for indice in atributos:
#             print(indice)

#     def latir(self):
#         return 'Au au'
#     def comer(self):
#         return 'alimentado'
#     def cacar(self):
#         return f'caça efetuada com sucesso, total de caças {random.randint(1000,1000000)}'
#     def trocarNome(self,nome):
#         if str(nome[-1:]) == 'a':
#             self.sexo = 'Femea'
#         else:
#             self.sexo = 'macho'
#         self.nome = nome
#     @classmethod
#     def funcaoObjeto(self,nome, idade, peso):
#         print('Oi, Estou sendo executada')
#         print(nome,idade,peso)

#mostrar nome, idade e peso na função com self
# Cachorro.funcaoObjeto('nome','idade','peso')

res = BancoMelhor()

print(res.insert('xoxoxoxo'))
print(res.select())
print(res.delete())
print(res.update(12))

###
# Criar uma classe humano, com os seguintes atributos:
# idade
# nome
# genero
#
#E os seguintes métodos:
#Andar
#comer
#dormir
#
# fazer herança da classe humano para a classe funcionário
# e acrescentar o método trabalhar
#
# Executar todos os métodos utilizando o return

class Humano():
    def __init__(self,idade,nome,genero):
        self.idade = idade
        self.nome = nome
        self.genero = genero
    def andar(self):
        return 'Andando'
    def comer(self):
        return 'Comendo'
    def dormir(self):
        return 'Dormindo'

class Funcionario(Humano):
    def __init__(self,profissao,nome,idade,genero):
        super().__init__(nome,idade,genero)
        self.profissao = profissao
    def trabalhar(self):
        return 'Trabalhando'

funcionario = Funcionario('Jogador de futebol','Gabigol',23,'Homo')


humano = Humano(19,'Lucas','Masculino')

print(dir(funcionario))

print(funcionario.dormir())