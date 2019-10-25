from banco import BancoMongo
import threading


if __name__ == "__main__":
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=client.select)
        f.start()
    except Exception as e:
        print(f'Falha ao criar a Thread: {e}')

    # while f.is_alive:
    #     mens = input()
    #     banco.cadastrar(user, mens)
        

