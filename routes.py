import os, random, pandas as pd, cgi, sqlite3 as sql, flask
from jinja2 import Template
from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import uuid

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.secret_key = os.urandom(24)
 

@app.route('/', methods=['GET', 'POST'])
def index():
    if "cnpj" in session:
        return render_template("main_restaurant.html")
    elif "cpf" in session:
        return render_template("/main.html")
    else:
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
                    session['cpf'] = session_cpf
                    session['uuid'] = str(uuid.uuid4())
                else:
                    print("bad")
                return redirect("/main")
            except Exception as e:
                return render_template("index_denied.html")
        elif request.form['index'] == "Registrar":
            return render_template("register.html")
        else:
            return render_template("restaurant_login.html")

@app.route('/access_restaurant', methods=['GET', 'POST'])
def access_restaurant():
    if request.method == 'POST':
        if request.form['index'] == "Login":
            try:
                CNPJ = request.form['CNPJ']
                password = request.form['password']
                with sql.connect("food.db") as con:
                    cur = con.cursor()
                    login_approve = cur.execute("SELECT * from restaurante where CNPJ=(?) and password=(?)",(CNPJ,password))
                for rows in login_approve:
                    session_cnpj = rows[0]
                if session_cnpj != None:
                    session['cnpj'] = session_cnpj
                    print(session_cnpj)
                else:
                    print("bad")
                return render_template("main_restaurant.html")
            except Exception as e:
                return render_template("restaurant_login_denied.html")
        else:
            return render_template("register_restaurant.html")

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        try:
            name = request.form['name']
            print(name)
            description = request.form['description']
            print(description)
            value = request.form['valor']
            print(value)
            with sql.connect("food.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into cardapio (produto,descricao,valor,CNPJ) VALUES (?,?,?,?)",(name,description,value,session["cnpj"]))
                con.commit()
                print("Record successfully added")
        except Exception as e:
            print("bad")
    return render_template("products_set.html")

@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        try:
            name = request.form['name']
            vehicle = request.form['vehicle']
            placa = request.form['placa']
            with sql.connect("food.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into entregador (nome,veiculo,placa,CNPJ) VALUES (?,?,?,?)",(name,vehicle,placa,session["cnpj"]))
                con.commit()
                print("Record successfully added")
        except Exception as e:
            print("bad")
    return render_template("delivery_set.html")

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

@app.route('/register_restaurant', methods=['GET', 'POST'])
def register_restaurant():
    if request.method == 'POST':
        try:
            nome_registro = request.form['user']
            nome_fantasia = request.form['nome']
            password = request.form['password']
            telefone = request.form['telefone']        
            email = request.form['email']
            CNPJ = request.form['CNPJ']
            categoria = request.form['categoria']
            funcionamento = request.form['funcionamento']
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            CEP = request.form['CEP']
            with sql.connect("food.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into restaurante (CNPJ,nome_registro,nome_fantasia,password,telefone,email,categoria,funcionamento,rua,numero,bairro,cidade,estado,CEP) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(CNPJ,nome_registro,nome_fantasia,password,telefone,email,categoria,funcionamento,rua,numero,bairro,cidade,estado,CEP))
                con.commit()
                print("Record successfully added")
        except Exception as e:
            return render_template("register_restaurant_miss.html")
    return render_template("restaurant_login.html")

@app.route('/main', methods=['GET', 'POST'])
def main():
    with sql.connect("food.db") as con:
        cur = con.cursor()
        cur.execute("SELECT CNPJ, nome_fantasia, categoria, funcionamento from restaurante")
        restaurant_info = cur.fetchall()
    return render_template("main.html", info=restaurant_info) 

@app.route('/shop/<cnpj>', methods=['GET', 'POST'])
def shop(cnpj):
    if request.method == 'POST':    
        try:
            order_number = session['uuid']
            print(order_number)
            for requests in request.form:
                if request.form[requests] != "":
                    print(requests)
                    print(request.form[requests])
                    with sql.connect("food.db") as con:
                        cur = con.cursor()
                        cur.execute("INSERT into pedido (CNPJ,produto_id,quantidade,CPF, uuio) VALUES (?,?,?,?,?)",(cnpj, requests, request.form[requests], session['cpf'], order_number))
                        con.commit()
                        print("Record successfully added")                    
        except Exception as e:
            print(e)
        return ('', 204)

@app.route('/shop_car', methods=['GET', 'POST'])
def shop_car():
    order_number = session['uuid']
    try:
        with sql.connect("food.db") as con:
            cur = con.cursor()
            cur.execute("SELECT r.nome_fantasia,c.produto, p.quantidade, c.valor from pedido p join restaurante r on (p.CNPJ=r.CNPJ) join cardapio c on (p.produto_id=c.ID) where uuio=(?)",(order_number,))
            shop_info = cur.fetchall() 
            print(shop_info)
            numero = float(shop_info[0][3])
            print(numero)

        return render_template("shop.html", shop_info=shop_info) 
    except Exception as e:
        return render_template("empty_shop.html")

@app.route('/restaurant/<cnpj>', methods=['GET', 'POST'])
def restaurant(cnpj):
    with sql.connect("food.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * from restaurante where CNPJ={cnpj}".format(cnpj=cnpj))
        restaurant_info = cur.fetchall()
        print(restaurant_info)
        cur.execute("SELECT ID, produto,descricao,valor from cardapio where CNPJ={cnpj}".format(cnpj=cnpj))
        produto_info = cur.fetchall()
        print(produto_info)
    return render_template("restaurant_info.html", info=restaurant_info, produto=produto_info) 

@app.route('/logout')
def logout():
    session.pop('cpf', None)
    session.pop('cnpj', None)

    return redirect("/", code=302)    

if __name__ == '__main__':
    app.run(debug = True)
