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

conexao.close()

print("Banco e tabela criados com sucesso!")


