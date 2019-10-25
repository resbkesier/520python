#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqla import Adress, Base, Person


# parametros de conexão
engine = create_engine('sqlite:///exemple.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# new_person = Person(name='Nova Pessoa')
# session.add(new_person)
# session.commit()
# session.close()

# aparentemente para poder usar o metódo .name precisa-se colocar dentro de um for como abaixo:
resultado = session.query(Person ).all()

for i in resultado:
    print(i.name)