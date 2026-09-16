
qtd_clientes = 10
soma_avaliacoes = 0
respostas_validas = 0
contador = 0

while contador < qtd_clientes:
    avaliacao = int(input(f"Cliente {contador + 1} - avaliação (1 a 5): "))

    if avaliacao < 1 or avaliacao > 5:
        print("Valor inválido! Digite um número entre 1 e 5.")
    else:
        if avaliacao == 1:
            classificacao = "ruim"
        elif avaliacao in (2, 3):
            classificacao = "regular"
        elif avaliacao == 4:
            classificacao = "boa"
        else:
            classificacao = "excelente"

        print(f"Avaliação {avaliacao} -> {classificacao}")
        soma_avaliacoes += avaliacao
        respostas_validas += 1
        contador += 1

media_geral = soma_avaliacoes / respostas_validas
print(f"\nMédia geral das avaliações: {media_geral:.2f}")
