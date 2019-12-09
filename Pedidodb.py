from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE pedido (ID INTEGER PRIMARY KEY AUTOINCREMENT, CNPJ INTEGER, produto_id INTEGER, quantidade INTEGER, CPF INTEGER, valor TEXT, horario DATETIME, entregador_id INTEGER, uuio TEXT, FOREIGN KEY(CNPJ) REFERENCES restaurante(CNPJ), FOREIGN KEY(CPF) REFERENCES user(CPF), FOREIGN KEY(entregador_id) REFERENCES entregador(ID), FOREIGN KEY(produto_id) REFERENCES cardapio(ID))')
print ("Table created successfully")
conn.close()

class Pedido(db.Model):
    ID = db.Column ('ID', db.Integer,primary_key=True, unique=True)
    CNPJ = db.Column('CNPJ', db.Integer, unique=False, nullable=False)
    quantidade = db.Column('quantidade', db.Integer, unique=False, nullable=False)
    CPF = db.Column('CPF', db.Integer, unique=False, nullable=False)
    valor = db.Column('valor', db.String(80), unique=True, nullable=False)
    horario = db.Column('horario', db.DateTime, unique=False, nullable=False)
    entregador_id = db.Column('entregador_id', db.Integer, unique=False, nullable=False)
    uuid = db.Column('uuid', db.String(800), unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.ID}', '{self.CNPJ}', '{self.quantidade}', '{self.CPF}', '{self.valor}', '{self.horario}', '{self.entregador_id}', '{self.uuid}')"
