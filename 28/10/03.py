import sqlite3

with sqlite3.connect("loja.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL,
            estoque INTEGER
        )
        """
    )

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    print("--- LISTA DE PRODUTOS ---")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}")
