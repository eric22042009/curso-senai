qtd_jogadores = 6
iniciante = 0
intermediario = 0
avancado = 0
maior_pontuacao = -1
nome_lider = ""

for i in range(1, qtd_jogadores + 1):
    nome = input(f"Jogador {i} - nome: ")
    pontos = int(input(f"Jogador {i} - pontuação: "))

    if pontos <= 20:
        nivel = "iniciante"
        iniciante += 1
    elif pontos <= 50:
        nivel = "intermediário"
        intermediario += 1
    else:
        nivel = "avançado"
        avancado += 1

    print(f"{nome}: {pontos} pontos -> {nivel}")

    if pontos > maior_pontuacao:
        maior_pontuacao = pontos
        nome_lider = nome

print("\nResumo do campeonato:")
print(f"Líder: {nome_lider} com {maior_pontuacao} pontos")
print(f"Iniciantes: {iniciante}")
print(f"Intermediários: {intermediario}")
print(f"Avançados: {avancado}")
