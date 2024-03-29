from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE user (CPF INTEGER PRIMARY KEY, nome TEXT, password TEXT, email TEXT, telefone TEXT, RG TEXT, rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, estado TEXT, CEP TEXT)')
print ("Table created successfully")
conn.close()

class User(db.Model):
    CPF= db.Column ('CPF', db.Integer, primary_key=True, unique=True)
    nome = db.Column('nome', db.String(80), unique=False, nullable=False)
    password = db.Column('password', db.String(80), unique=False, nullable=False)
    email = db.Column('email', db.String(80), unique=True, nullable=False)
    telefone = db.Column('telefone', db.String(80), unique=False, nullable=False)
    RG = db.Column('RG', db.String(80), unique=False, nullable=False)
    rua = db.Column('rua', db.String(200), unique=False, nullable=False)
    numero = db.Column('numero', db.String(80), unique=False, nullable=False)
    bairro = db.Column('bairro', db.String(80), unique=False, nullable=False)
    cidade = db.Column('cidade', db.String(80), unique=False, nullable=False)
    estado = db.Column('estado', db.String(80), unique=False, nullable=False)
    CEP = db.Column('CEP', db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.CPF}', '{self.nome}', '{self.password}', '{self.email}', '{self.telefone}', '{self.RG}', '{self.rua}', '{self.numero}', '{self.bairro}', '{self.cidade}', '{self.estado}', '{self.CEP}')"
