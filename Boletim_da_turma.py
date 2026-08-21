aprovado = 0 
recuperação = 0
reprovado = 0 


for i in range(5):
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    media = (n1 + n2) / 2


    if media >= 6:
        print("aprovado")
        aprovado += 1

    elif media >=4:
        print("recuperação")
        recuperação += 1
        
    else:
        print("reprovado")
        reprovado += 1

print("aprovados:", aprovado)
print("recuperações:", recuperação)
print("reprovado:", reprovado)