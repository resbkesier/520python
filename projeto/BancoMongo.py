#!/usr/bin/env python3
from pymongo import MongoClient, DESCENDING
import time
class BancoMongo():

    def __init__(self):
        try:
            client = MongoClient()
            self.db = client['chat']
        except Exception as e:
            print(e)
            exit()
    def cadastrar(self,nome,mensagem):
        date = {
            'nome' : nome,
            'mensagem' : mensagem,
            'hora': time.strftime('%d-%m-%Y %H:%M:%S')
        }
        self.db.chat.insert(date)

    def select(self):
        ultimoRegistro = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
        while True:
            atualRegistro = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
            if atualRegistro != ultimoRegistro:
                ultimoRegistro = atualRegistro
                dado = ultimoRegistro[0]
                print(f"[{dado['hora']}] {dado['nome']} : {dado['mensagem']} \n")
            time.sleep(1)

