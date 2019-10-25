#!/usr/bin/python3
from pymongo import MongoClient, DESCENDING
import time

class BancoMongo():

    def __init__(self):
        try:
            client = MongoClient()
            self.db = client['chat']

        except Exception as e:
            print(f'ERRO {e}')
            exit()

    def cadastrar(self, name, mensagem):
        date = {
            'name': name,
            'mensagem': mensagem,
            'hora': time.strftime('%d-%m-%Y %H:%M:%S')}
        self.db.chat.insert(date)

    def select(self):
        ultimo = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
        while True:
            date = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
            if date != ultimo:
                ultimo = date
                print('[{}] {}: {} \n'.format(date[0]['hora'], date[0]['name'], date[0]['mensagem'] ))
                time.sleep(2)

if __name__ == "__main__":
    obj = BancoMongo()
    obj.select()

