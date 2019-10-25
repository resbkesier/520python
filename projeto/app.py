from BancoMongo import BancoMongo
import threading
client = BancoMongo()

if __name__ == "__main__":
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=client.select)
        f.start()
    except Exception as e:
        print(e)
        exit()
    while f.isAlive:
        mens = input()
        client.cadastrar(user,mens)