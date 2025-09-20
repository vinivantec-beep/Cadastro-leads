import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vinicius",
    database="projeto_faculdade"
)
cursor = conn.cursor()

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
    conn.commit()
    print("Produto cadastrado!")

def cadastrar_lead():
    nome = input("Nome do lead: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    print("Produtos disponíveis:")
    for p in produtos:
        print(f"{p[0]} - {p[1]} ({p[2]})")
    produto_id = int(input("ID do produto de interesse: "))
    cursor.execute("INSERT INTO leads (nome, email, telefone, produto_id) VALUES (%s,%s,%s,%s)", 
                   (nome,email,telefone,produto_id))
    conn.commit()
    print("Lead cadastrado!")

def listar_leads():
    cursor.execute("SELECT l.id, l.nome, l.email, l.telefone, p.nome FROM leads l JOIN produtos p ON l.produto_id = p.id")
    for l in cursor.fetchall():
        print(l)

def menu():
    while True:
        print("\n1- Cadastrar produto\n2- Cadastrar lead\n3- Listar leads\n4- Sair")
        opc = input("Escolha: ")
        if opc=="1":
            cadastrar_produto()
        elif opc=="2":
            cadastrar_lead()
        elif opc=="3":
            listar_leads()
        elif opc=="4":
            break

menu()
