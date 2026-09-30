nome = input("Nome do usuário: ")
status = input('Status do acesso ("Sucesso" ou "Falha"): ')
 
with open("sistema_logs.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"[LOG] - Usuario: {nome} | Status: {status}\n")
 
    print("Evento registrado no log do sistema.")
 