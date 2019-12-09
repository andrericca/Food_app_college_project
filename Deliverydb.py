from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE entregador (ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, veiculo TEXT, placa TEXT, CNPJ INTEGER, FOREIGN KEY(CNPJ) REFERENCES restaurante(CNPJ))')
print ("Table created successfully")
conn.close()

class Products(db.Model):
    ID= db.Column ('ID', db.Integer,primary_key=True, unique=True)
    nome = db.Column('nome', db.String(80), unique=False, nullable=False)
    veiculo = db.Column('veiculo', db.String(800), unique=False, nullable=False)
    placa = db.Column('placa', db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"user('{self.ID}', '{self.nome}', '{self.veiculo}', '{self.placa}')"
