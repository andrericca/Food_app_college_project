from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/andreyoshdia/Documents/secretapp/food.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('food.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE game (user_id TEXT, classe TEXT, guess TEXT, img TEXT)')
print ("Table created successfully")
conn.close()

class Food(db.Model):
    id = db.Column ( db.Integer,primary_key=True)
    user_id = db.Column('user_id', db.String(80), unique=True, nullable=False)
    classe = db.Column('classe', db.String(80), unique=True, nullable=False)
    guess = db.Column('guess', db.String(80), unique=True, nullable=False)
    img = db.Column('img', db.String(80), unique=True, nullable=False)


    def __repr__(self):
        return f"user('{self.id}','{self.classe}','{self.guess}','{self.img}')"
