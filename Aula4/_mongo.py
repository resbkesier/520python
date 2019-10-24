#!/usr/bin/python3

import pymongo
class BancoMongo():
    def __init__(self):
        try:
            client = pymongo.MongoClient('127.0.0.1')
            self.db = client['dexterops']
            # for itens in db.fila.find():
                # print(itens)
        except Exception as e:
            print(e)

    def select(self):
        for itens in self.db.fila.find():
            print(itens)

    def insert(self):
        self.db.fila.insert({"valor1":"valor2"})

    def delete(self):
        self.db.fila.remove({})

    def update(self):
        self.db.fila.update({"valor1":"valor2"},{'$set':{'valor3':'valor4'}})

obj = BancoMongo()



obj.delete()
obj.select()