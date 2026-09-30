while True:
    nome = input('Digite um nome (ou "Sair" para encerrar): ').strip().title()
 
    if nome == "Sair":  # .title() transforma "sair" em "Sair"
        break
    if nome == "":  # ignora entradas vazias
        print("Nome inválido, tente novamente.")
        continue
 
    with open("cadastro_nomes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")
 
    print("Cadastro finalizado e salvo no arquivo!")
 