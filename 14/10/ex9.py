import json

ARQUIVO = "alunos.json"

def carregar_alunos():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_alunos(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

def cadastrar():
    nome = input("Nome do aluno: ")
    nota = float(input("Nota: "))
    alunos = carregar_alunos()
    alunos.append({"nome": nome, "nota": nota})
    salvar_alunos(alunos)
    print("Aluno cadastrado!")

def listar():
    alunos = carregar_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")

def buscar():
    busca = input("Nome para buscar: ").lower()
    alunos = carregar_alunos()
    encontrou = False
    for aluno in alunos:
        if busca in aluno["nome"].lower():
            print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")
            encontrou = True
    if not encontrou:
        print("Aluno não encontrado.")

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar novo aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno pelo nome")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")