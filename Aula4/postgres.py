import psycopg2

'''
try:
    con = psycopg2.connect("host=127.0.0.1\
    dbname=biblioteca\
    user=admin\
    password=4linux")

    res = con.cursor()
    res.execute("insert into clientes(nome, sobrenome) values('lucas', 'Barbosa')") # insert
    #res.execute("delete from clientes where nome = 'lucas';") # delete
    con.commit()
    res.execute("select * from clientes")
    print(res.fetchall())
    res.close()
except Exception as e:
    print(e)
    con.close()
'''

class Bancopsql():
    def __init__(self):
        try:
            self.con = psycopg2.connect("host=127.0.0.1\
                                    dbname=biblioteca\
                                    user=admin\
                                    password=4linux")

            self.cur = self.con.cursor()
            
        except Exception as e:
            print(f'falha na conexão {e}')
            self.con.close()
        
    def select(self, tabela, item='*'):
        self.cur.execute(f'SELECT {item} FROM {tabela}')
        print(self.cur.fetchall())
    
    def update(self, tabela, coluna, novo, nomeAntigo):
        self.cur.execute(f"UPDATE {tabela} SET {coluna}='{novo}' WHERE nome = '{nomeAntigo}' ")
        self.con.commit()
    
    def delete(self, nomeTabela):
        self.cur.execute(f"DELETE FROM clientes where nome = '{nomeTabela}'")
        self.con.commit()

    def insert(self, nome, sobrenome):
        self.cur.execute(f"insert into clientes(nome, sobrenome) values('{nome}', '{sobrenome}')")
        print('Dado inserido!')
        self.con.commit()

banco = Bancopsql()
# banco.select('clientes')
#banco.update('clientes', 'nome', 'Renato', 'Camaççro')
banco.delete('Renato')
