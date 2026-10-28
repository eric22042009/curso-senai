import sqlite3

with sqlite3.connect("loja.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL,
            estoque INTEGER
        )
    """)

nome = input("qual o nome do produto ")
preco = float(input("qual o preço do produto "))
estoque = int(input("qual a quantidade em estoque "))

with sqlite3.connect("loja.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES (?, ?, ?)
    """, (nome, preco, estoque))

print("Produto adicionado com sucesso!")