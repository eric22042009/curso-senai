import json

produto = {"nome": "frigideira", "preco": 20, "quantidade": 3, "categorias": ["cozinha", "panelas"]}

with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(produto, arquivo, indent=4, ensure_ascii=False)


