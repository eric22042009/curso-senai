import json

livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937}
]

texto_json = json.dumps(livros, indent=4, ensure_ascii=False)
print(texto_json)