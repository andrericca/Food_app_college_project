from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE cardapio (ID INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, descricao TEXT, valor TEXT, CNPJ INTEGER, FOREIGN KEY(CNPJ) REFERENCES restaurante(CNPJ))')
print ("Table created successfully")
conn.close()

class Products(db.Model):
    ID= db.Column ('ID', db.Integer,primary_key=True, unique=True)
    produto = db.Column('produto', db.String(80), unique=False, nullable=False)
    descricao = db.Column('descricao', db.String(800), unique=False, nullable=False)
    valor = db.Column('valor', db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"user('{self.ID}', '{self.produto}', '{self.descricao}', '{self.valor}')"
