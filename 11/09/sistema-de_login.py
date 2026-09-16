usuario_correto = "aluno"
senha_correta = "1234"

tentativas = 1

while tentativas <= 3:
    user = input("Usuario: ")
    senha = input("Senha: ")
    
    if user == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break 
    elif tentativas == 3:
        print("Usuario bloqueado por excesso de tentativas!")
        tentativas = tentativas + 1
    else:
        print("Senha ou usuario incorreto. Tente de novo.")
        tentativas = tentativas + 1
