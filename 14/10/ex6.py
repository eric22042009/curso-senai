import json

def atualizar_preco(id_produto, novo_preco):
    try:
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        produtos = [
            {"id": 1, "nome": "Mouse", "preco": 50},
            {"id": 2, "nome": "Teclado", "preco": 120}
        ]

    for produto in produtos:
        if produto["id"] == id_produto:
            produto["preco"] = novo_preco

    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

    print("Preço atualizado!")

atualizar_preco(1, 65.90)