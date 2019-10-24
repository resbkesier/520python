
# exemplo


def modifica(funcao):
    def oi():
        a = funcao()
        return f'{a} {oi}'
    return oi


def paramentro(nome):
    return nome

# funcao_decorada = modifica(paramentro('Nome'))
# print(funcao_decorada)


def corazul(texto):
    def modificatexto():
        a = texto
        print(f'\033[94m{a}\033[0m')
    return modificatexto


@corazul
def mostratexto():
    return 'Turma python fundamentals'


mostratexto()
