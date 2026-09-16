alunos = []

for i in range(1, 6):
    nome = input(f"Digite o nome do aluno {i}: ")
    nome_formatado = nome.strip().title()

    if nome_formatado in alunos:
        print("Aluno já cadastrado na lista!")
    else:
        alunos.append(nome_formatado)

print("\nLista final de alunos cadastrados:")
print(alunos)
