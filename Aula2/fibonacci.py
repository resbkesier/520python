#! usr/bin/python3

def calcula(valor=80):
    a = 1
    d = 1
    va = 0
    while d <= valor:   
        print(d)
        va = d
        d += a
        a = va
if __name__ == "__main__":
    
    calcula()