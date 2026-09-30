tema = input('Escolha o tema ("Claro" ou "Escuro"): ')
 
with open("config.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(tema)
 
print(f"Tema '{tema}' salvo em config.txt (conteúdo anterior substituído).")