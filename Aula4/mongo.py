import pymongo

class Mongao():

    def __init__(self):    
        try:
            client = pymongo.MongoClient('127.0.0.1')
            print('\nConexão estabelecida!\n')
            
            self.db = client['dexterops']
            # print(db.collection_names())
            # db.fila.insert({'_id': 4, 'Serviço': 'mongo', 'status': 4.0})
            self.db.fila.remove({'_id': 2})
            for itens in self.db.fila.find():
                print(itens)
        
        except Exception as e: 
            print(e)

    def insert(self, id, servico, status):
        self.db.fila.insert({'_id': f'{id}', 'Serviço': f'{servico}', 'status': f'{status}'})
        for itens in self.db.fila.find():
            print(itens)
    
    def select(self):
        pass
        
    def update(self):
        pass
    
    def delete(self):
        pass

mongo = Mongao()

mongo.insert('56', 'Aula', '34')