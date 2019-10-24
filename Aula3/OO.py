#! usr/bin/python3
from bancodedados import BancoMelhor
# POO - Programação a objetos

# Criação de classe

class Foo():
    pass

# Atributos

class Human():
    nome = 'Renato'
    idade = 26
    altura = 1.73
    peso = 81.3

#Metodos

class Funcionario():

    def funcionario(self):
        pass

#Objetos
# Para criar um objeto precisamos realizar uma instância da classe
obj = Foo()

# utilizando os métodos de uma classe
obj.__class__


# Exemplo completo

class Fazendeiro():

    def capinar(self):
        print('capinando...')
        print('capinando...')
        print('capinando...')
        print('capinando...')
        print('capinando...')
        print('terminei uai')

# gerson = Fazendeiro()

# gerson.capinar()


# Criando uma classe com métodos e atributos

class Meteorologista():

    # método construtor passa atributos para os métodos
    #Atributos
    def __init__(self, nome, idade, tv= True):
        self.nome = nome
        self.idade = idade
        self.tv = tv
        self.emissora = 'Band'
        self.__teste = 33

    # Métodos
    def previsao_tempo(self):
        print(f'Boa tarde, meu nome é {self.nome}')
        if self.tv == True:
            print(f'Faço parte da Emissora {self.emissora}')
        print('Hoje está nublado')
        print(f'Só pra constar eu tenho {self.idade}')
    
    def __oculto(self):
        pass
    
    def trocaNome(self, nome):
        self.nome = nome

# laura = Meteorologista('Laura', 43)
# laura.trocaNome('Rapadura')
# laura.previsao_tempo()



# Faça um cachorro com os seguntes atributos:
#idade, sexo, cor, raça.
# e os métodos: latir, comer caçar, trocar nome








class Cachorro():

    def __init__(self, nome, cor, raca, sexo):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.sexo = sexo
    
    def latir(self):
        return 'latindo...'
    
    def comer(self):
        return 'comendo...'
    
    def cacar(self):
        return 'caçando...'
    
    def trocaNome(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f'nome: {self.nome}\ncor: {self.cor}\nraça: {self.raca}\nsexo: {self.sexo}'
    
    @staticmethod
    def teste(nome, idade, peso):
        print(f'nome: {nome}\nidade: {idade}\npeso: {peso}')

# cachorroBeje = cachorro('chola','beje','vira-lata', 'fêmea')
# print(cachorroBeje.__str__())
# print(cachorroBeje.latir())
# print(cachorroBeje.comer())
# print(cachorroBeje.cacar())
# cachorroBeje.trocaNome('Lola')
# print('O novo nome é', cachorroBeje.nome)

Cachorro.teste('Bill', '7', '25.5')


app = BancoMelhor()
print(app.insert('user'))