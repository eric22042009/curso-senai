import sqlite3


preco_max = float(input("Digite o preço máximo: R$ "))


conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()


cursor.execute("SELECT * FROM produtos WHERE preco <= ?", (preco_max,))
produtos = cursor.fetchall()


print("\n--- Produtos Encontrados ---")
for p in produtos:
    print(f"Nome: {p[1]} | Preço: R$ {p[2]:.2f}")


conexao.close()