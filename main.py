import utilities
from storage import carregar_tarefas
utilities.tarefas = carregar_tarefas()

while True:
    option = input("Escolha uma das opções: \n 1. Criar tarefa \n 2. Listar tarefas \n 3. Concluir tarefa \n 4. Listar tarefas concluídas \n 5. Remover tarefa \n 0. Sair: ")

    if option == "1":
        utilities.criar_tarefa()

    elif option == "2":
        utilities.listar_tarefas()

    elif option == "3":
        utilities.concluir_tarefa()

    elif option == "4":
        utilities.listar_tarefas_concluidas()

    elif option == "5":
        utilities.remover_tarefa()
        
    elif option == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
        continue