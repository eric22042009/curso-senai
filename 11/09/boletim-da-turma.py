aprovados = 0
recuperacoes = 0
reprovados = 0

for i in range(1, 6):
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    
    media = (nota1 + nota2) / 2
    print("Media:", media)

    if media >= 6.0:
        print("Aprovado")
        aprovados = aprovados + 1
    elif media >= 4.0:
        print("Recuperação")
        recuperacoes = recuperacoes + 1
    else:
        print("Reprovado")
        reprovados = reprovados + 1

print("Aprovados:", aprovados)
print("Recuperações:", recuperacoes)
print("Reprovados:", reprovados)