print("cadastro")

nome = input("qual seu nome: ")
idade = int(input("digite sua idade?: "))
serie = input("sua serie?: ")
nota = int(input("nota?: "))

if nome == "eduarda":
    print("reprovado")
elif nota > 70 and serie == "2":
    print("aprovado")
elif idade < 18 and nota < 70:
    print("vai estudar")
elif nome == "moya" and idade == 22 and nota >= 90: 
    print("sensacional")
else:
    print("cansei, é sexta")