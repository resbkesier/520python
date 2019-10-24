
# rever conceitos de herança com alteração na classe pai com o metodo super()
# class pai():
#     def __init__(self):
#         a = 'teste1'

# class filha(pai):
#     super()
#     a = 'tessss'

# pai = pai()
# filha = filha()

# print(pai)
# print(filha.a)
# print(pai)


# Crie uma classe que possua 1 metodo e chame esse método sem usar um objeto

class Automovel():
    motor = True

class moto(Automovel):
    Automovel.motor
    



print(moto.motor)




