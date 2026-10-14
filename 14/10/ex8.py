import json

padrao = {"tema": "escuro", "notificacoes": True}

try:
    with open("configuracoes.json", "r", encoding="utf-8") as arquivo:
        config = json.load(arquivo)
    print("Configurações carregadas:")
    print(f"Tema: {config['tema']}")
    print(f"Notificações: {config['notificacoes']}")
except (FileNotFoundError, json.JSONDecodeError):
    print("Arquivo não encontrado ou inválido. Criando com configurações padrão...")
    with open("configuracoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(padrao, arquivo, indent=4, ensure_ascii=False)