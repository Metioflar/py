alunos = {}



def adicionar_aluno():

    nome = input("Digite o nome do aluno: ")

    matricula = input("Digite o número de matrícula do aluno: ")

    alunos[matricula] = nome

    print("Aluno adicionado com sucesso!")



def remover_aluno():

    matricula = input("Digite o número de matrícula do aluno a ser removido: ")

    if matricula in alunos:

        del alunos[matricula]

        print("Aluno removido com sucesso!")

    else:

        print("Matrícula não encontrada.")



def verificar_alunos():

    print("Lista de alunos:")

    for matricula, nome in alunos.items():

        print(f"Matrícula: {matricula}, Nome: {nome}")



while True:

    print("\nEscolha uma opção:")

    print("1 - Adicionar aluno")

    print("2 - Remover aluno")

    print("3 - Visualizar alunos")

    print("4 - Sair")

    

    opcao = input("Digite o número da opção: ")

    

    if opcao == "1":

        adicionar_aluno()

    elif opcao == "2":

        remover_aluno()

    elif opcao == "3":

        verificar_alunos()

    elif opcao == "4":

        print("Saindo...")

        break

    else:

        print("Opção inválida. Tente novamente.")
