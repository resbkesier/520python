#!/usr/bin/python3
import psycopg2



# class BancoMelhor():
    
#     def __init__(self):
#         self.usuario = 'root'
#         self.senha = '123456'
#         self.banco = 'mysql'
    
#     def select(self):
#         if self.usuario == 'root':
#             return 'Dados do Banco'
#         else:    
#             return None
    
#     def insert(self, dados):
#         if self.usuario == 'root':
#             return f'Dado {dados} inseridos'
#         else:
#             return None
    
#     def delete(self):
#         if self.usuario == 'root':
#             return 'Dado removido'
#         else:
#             return None

#     def update(self,id):
#         if self.usuario == 'root':
#             return 'Atualizado com sucesso'
#         else:
#             return None

#!/usr/bin/python3
import psycopg2
try:
    con = psycopg2.connect("host=127.0.0.1")
    dbname='projeto'
    user='admin'
    password=("4linux")
    cur = con.cursor()
    cur.execute("insert into scripts(nome,conteudo) values('devops','projeto de python')")
    con.commit()
    print("Registro criado com sucesso")
except ConnectionError as e:
    print("Erro: {}".format(e))
    print("Fazendo rollback")
    con.rollback()
finally:
    print("Finalizando conexao com o banco de dados")
    cur.close()
    con.close()

#Criar um banco de dados chamado biblioteca com dono no admin
#Criar duas tabelas, livros, clientes
# livros (nome VARCHAR(50),autor VARCHAR(50), paginas INT)
# clientes (nome VARCHAR(50), sobrenome(50))

'''
use dados
db.nomes.insert({"nome": "Daniel"})

db.nomes.remove({"nome": "Daniel"})

db.nomes.update({"nome": "Daniel"}, {"$set": {"nome": "julio"}})

db.nomes.updateMay({"nome": "Daniel"}, {"$set": {"nome": "julio"}})



'''