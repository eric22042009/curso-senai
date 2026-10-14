import json

with open("produto.json", "r", encoding="utf-8") as arquivo:
    produto = json.load(arquivo)

print(f"Produto: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['quantidade']} unidades")

