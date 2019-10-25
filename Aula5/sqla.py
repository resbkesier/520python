# import sqlite3

# con = sqlite3.connect('example.db')

# cursor = con.cursor()


# cursor.execute('''
#                 CREATE TABLE person
#                 (id INTEGER PRIMARY KEY ASC,
#                      name VARCHAR(250) NOT NULL)
#                 ''')

# cursor.execute('''
#                 CREATE TABLE adress
#                 (id INTEGER PRIMARY KEY ASC,
#                      street_name VARCHAR(250) NOT NULL,
#                      street_number INT NOT NULL)
#                 ''')

# cursor.execute('''
#     INSERT INTO person VALUES (1, 'Daniel')
# ''')
# cursor.execute('''
#     INSERT INTO adress VALUES (1, 'Vergueiro',3057)
# ''')


# con.commit()
# con.close()


# con = sqlite3.connect('example.db')

# cursor = con.cursor()

# cursor.execute('SELECT * FROM person')

# print(cursor.fetchall())


# Maneira ORM
import os
import sys
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ =  'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Adress(Base):
    __tablename__ = 'adress'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(Integer)

engine = create_engine('sqlite:///exemple.db')
Base.metadata.create_all(engine)



