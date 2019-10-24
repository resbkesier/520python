# !/usr/bin/python3

# ## manipulação de arquivos
# ponteiro =  open('texto.txt','w')

# ponteiro.write('Esta é para ser a segunda linha')

# ponteiro.close()

# with open('texto.txt','a') as ponteiro:
#     ponteiro.write('Essa modificação é com o with open\n')

# Criar uma lista com 5 indices
# Escrever no arquivo:
# 'indice {x} = {indice}'


# with open('texto.txt','a') as ponteiro:
#     a = 0
#     for indice in lista:
#         ponteiro.write(f'Indice {a} = {indice}\n')
#         a +=1

# with open('texto.txt', 'w') as ponteiro:
#     for indice, item in enumerate(lista):
#         print(f'indice {indice} = {item}')

# fazer iteração de duas listas da mesma maneira passada anterior

# with open('texto.txt', 'w') as ponteiro:
#     for indice, item in enumerate(lista + lista2):
#         ponteiro.write(f'indice {indice} = {item}\n')


# # trabahlando com readlines()
# with open('texto.txt', 'r') as ponteiro:
#     a = ponteiro.readlines()
#     print(a)

# Crie duas funções que recebem como parâmetro o nome do arquivo
# Uma para ler e outra para escrever

lista = ['indice1', 'indice2', 'indice3', 'indice3', 'indice5']
lista2 = ['chave1', 'chave2', 'chave3', 'chave4', 'chave5']


def ler_arquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as ponteiro:
            print(ponteiro.read())
    except FileNotFoundError:
        print('arquivo não encontrado')
    finally:
        ponteiro.close()


def escrever_arquivo(nomeArquivo, *conteudo):
    try:
        with open(nomeArquivo, 'w') as ponteiro:
            return ponteiro.write(conteudo)

    except TypeError as e:
        print('falta passar a mensagem', e)

    finally:
        ponteiro.close()

# escreve_arquivo('estou adicionando uma frase a esse arquivo')

# Funcção para escrever arquivo testando se o valor a ser inserido é uma lista e tratando dados

# def escrever_new(nomeArquivo, *conteudo):
#     try:
#         with open(nomeArquivo, 'a') as ponteiro:
#             escrita = [str(x) for x in escrita]
#             ponteiro.writelines(escrita)
#     except Exception as e:
#         print('Erro no modulo de escrever', e)

print(dir(ler_arquivo))

