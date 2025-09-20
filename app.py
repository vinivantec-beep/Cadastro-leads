from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vinicius",
    database="projeto_faculdade"
)
cursor = conn.cursor()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    return render_template('index.html', produtos=produtos)


@app.route('/add_lead', methods=['POST'])
def add_lead():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    produto_id = request.form['produto_id']
    cursor.execute("INSERT INTO leads (nome, email, telefone, produto_id) VALUES (%s,%s,%s,%s)",
                   (nome, email, telefone, produto_id))
    conn.commit()
    return redirect('/')


@app.route('/leads')
def leads():
    cursor.execute(
        "SELECT l.id, l.nome, l.email, l.telefone, p.nome FROM leads l JOIN produtos p ON l.produto_id = p.id")
    leads = cursor.fetchall()
    return render_template('leads.html', leads=leads)


if __name__ == '__main__':
    app.run(debug=True)
