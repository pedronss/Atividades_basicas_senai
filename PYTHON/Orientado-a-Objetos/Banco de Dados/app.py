import os
import sqlite3
# Conectar (ou criar) um banco de dados SQLite chamado "meudatabase.db"

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criar uma nova tabela chamada "usuarios" caso não existe. Se já existir nada será feito
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')
# Inserir um novo registro na tabela "usuarios"
def inserir(nome,idade):
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
# Recuperando a lista de usuários
def listar():
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()

    for item in registros:
        print(f"ID: {item[0]}, Nome: {item[1]}, Idade: {item[2]}")
#Atualizar usuarios
def atualizar(nome,idade,id):
    cursor.execute(f"UPDATE usuarios SET nome=?,idade=? WHERE id=?",(nome,idade,id)) 
#Deletar usuario
def deletar(id):
    cursor.execute(f"DELETE FROM usuarios WHERE id=?",(id,))

while True:
    os.system('cls')
    print("O que deseja fazer?\n(1)Inserir usuário\n(2)Listar usuários\n(3)Editar usuários\n(4)Remover usuários\n")
    opcao=int(input(""))
    match opcao:
        case 1:
            nome=input("Nome: ")
            idade=int(input("Idade: "))
            inserir(nome,idade)
        case 2:
            os.system('cls')
            listar()
            input("Pressione enter para continuar")
        case 3:
            id=int(input("Id do usuário que deseja editar: "))
            nome=input("Nome: ")
            idade=int(input("Idade: "))
            atualizar(nome,idade,id)
        case 4:
            id=int(input("Id do usuário que deseja excluir: "))
            deletar(id)

conn.commit() 

conn.close()