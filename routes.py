import os, random, pandas as pd, cgi, sqlite3 as sql, flask
from jinja2 import Template
from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.secret_key = os.urandom(24)
 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/access', methods=['GET', 'POST'])
def access():
    if request.method == 'POST':
        if request.form['index'] == "Login":
            try:
                CPF = request.form['CPF']
                password = request.form['password']
                with sql.connect("food.db") as con:
                    cur = con.cursor()
                    login_approve = cur.execute("SELECT * from user where CPF=(?) and password=(?)",(CPF,password))
                for rows in login_approve:
                    session_cpf = rows[0]
                if session_cpf != None:
                    print(session_id)
                else:
                    print("bad")
                return render_template("main.html")
            except Exception as e:
                return render_template("index_deneid.html")
        else:
            return render_template("register.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = request.form['user']
            password = request.form['password']
            telefone = request.form['telefone']
            email = request.form['email']
            CPF = request.form['CPF']
            RG = request.form['RG']
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
            with sql.connect("food.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into user (CPF,nome,password,telefone,email,RG,rua,numero,bairro,cidade,estado,CEP) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(CPF,user,password,telefone,email,RG,rua,numero,bairro,cidade,estado,CEP))
                con.commit()
                print("Record successfully added")
        except Exception as e:
            return render_template("register_miss.html")
    return render_template("index.html")

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        try:
            user = request.form['user']
            password = request.form['password']
            with sql.connect("game.db") as con:
                cur = con.cursor()
                new_value= cur.execute("SELECT (user,password) FROM user where user = %s and password =%s",'user','password')
                if new_value> 0:
                    return "the username exists"
                else:
                    return "SUCCESS!,Successfully entered into the Database"
                print("Record successfully added")
        except Exception as e:
            print("error in insert operation", e)  
        session['username'] = request.form['user']
        # con = sql.connect("game.db")
        # cur = con.cursor()
        # game = cur.execute("SELECT id from user where nm = (?)", (x,))
        # user_id = 0
        # for rows in game:
        #     user_id = rows[0]
        # session['id'] = user_id
        

    if 'username' in session:
        username = session['username']
        details="details"
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], str (details) + '.txt')
        return render_template("game.html", user_image = full_filename )


    return "You are not logged in <br><a href = '/'></b>" + \
    "click here to log in</b></a>"  

@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect("/", code=302)    

if __name__ == '__main__':
    app.run(debug = True)
