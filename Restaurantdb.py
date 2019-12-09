from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE restaurante (CNPJ INTEGER PRIMARY KEY, nome_registro TEXT, nome_fantasia TEXT, password TEXT, email TEXT, telefone TEXT, categoria TEXT, funcionamento TEXT, rua TEXT, numero TEXT, bairro TEXT, cidade TEXT, estado TEXT, CEP TEXT)')
print ("Table created successfully")
conn.close()

class Food(db.Model):
    CNPJ= db.Column ('CNPJ', db.Integer,primary_key=True, unique=True)
    nome_registro = db.Column('nome_registro', db.String(80), unique=False, nullable=False)
    nome_fantasia = db.Column('nome_fantasia', db.String(80), unique=False, nullable=False)
    password = db.Column('password', db.String(80), unique=False, nullable=False)
    email = db.Column('email', db.String(80), unique=True, nullable=False)
    telefone = db.Column('telefone', db.String(80), unique=False, nullable=False)
    categoria = db.Column('categoria', db.String(80), unique=False, nullable=False)
    funcionamento = db.Column('funcionamento', db.String(80), unique=False, nullable=False)
    rua = db.Column('rua', db.String(200), unique=False, nullable=False)
    numero = db.Column('numero', db.String(80), unique=False, nullable=False)
    bairro = db.Column('bairro', db.String(80), unique=False, nullable=False)
    cidade = db.Column('cidade', db.String(80), unique=False, nullable=False)
    estado = db.Column('estado', db.String(80), unique=False, nullable=False)
    CEP = db.Column('CEP', db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"user('{self.CNPJ}', '{self.nome_registro}', '{self.nome_fantasia}', '{self.password}', '{self.email}', '{self.telefone}', '{self.categoria}', '{self.funcionamento}','{self.rua}', '{self.numero}', '{self.bairro}', '{self.cidade}', '{self.estado}', '{self.CEP}')"

