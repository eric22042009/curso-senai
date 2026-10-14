import json

json_string = '{"usuario": "dev_python", "nivel": "intermediario", "ativo": true}'

dados = json.loads(json_string)

if dados["ativo"]:
    print(f"Bem-vindo, {dados['usuario']}! Seu nível é {dados['nivel']}.")
else:
    print("Usuário inativo.")