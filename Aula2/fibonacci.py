#! usr/bin/python3
from funcoes import teste

teste()

lista = []
def calcula(valor=80):
    a = 1
    d = 1
    va = 0
    while d <= valor:   
        lista.append(d)
        va = d
        d += a
        a = va
    lista.sort(reverse=True)
    print(lista)

    


if __name__ == "__main__":
    calcula()