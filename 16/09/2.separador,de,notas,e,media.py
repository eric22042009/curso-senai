notas = [7.5, 4.0, 9.2, 5.5, 3.8, 10.0, 6.5, 2.0]

media_turma = sum(notas) / len(notas)
print(f"Média da turma: {media_turma:.2f}")

aprovados = []
recuperacao = []

for nota in notas:
    if nota >= 6.0:
        aprovados.append(nota)
    else:
        recuperacao.append(nota)

print(f"\nTotal de aprovados: {len(aprovados)}")
print(f"Total em recuperação: {len(recuperacao)}")