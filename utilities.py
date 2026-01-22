from storage import salvar_tarefas

tarefas = []

def criar_tarefa():
    titulo = input("Digite o titulo da tarefa: ")
    concluida = False
    tarefa = {"titulo": titulo, "concluida": concluida }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' criada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Sim" if tarefa["concluida"] else "Não"
        print(f"{i}. {tarefa['titulo']} - Concluída: {status}")


def listar_tarefas_concluidas():
    tarefas_concluidas = [tarefa for tarefa in tarefas if tarefa["concluida"] == True]
    
    if not tarefas_concluidas:
        print("Nenhuma tarefa concluída encontrada.")
        return
    
    for i, tarefa in enumerate(tarefas_concluidas, start=1):
        status = "Sim" if tarefa["concluida"] else "Não"
        print(f"{i}. {tarefa['titulo']} - Concluída: {status}")


def concluir_tarefa():
    while True:
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
            break

        listar_tarefas()
        indice = input("Digite o número da tarefa a ser concluída ou digite menu para voltar ao menu:")

        if indice == "menu":
            break

        if not indice.isdigit():
            print("opção inválida.")
            continue

        elif int(indice) <= 0 or int(indice) > len(tarefas):
            print("Opção inválida.")
            continue
        
        indice = int(indice) - 1

        print(f"Tarefa '{tarefas[indice]}' marcada como concluída com sucesso!")
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        break

def remover_tarefa():
    while True:
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
            break
        
        listar_tarefas()
        indice = input("Digite o número da tarefa a ser removida ou digite menu para voltar ao menu:")

        if indice == "menu":
            break

        elif not indice.isdigit():
            print("Opção inválida.")
            continue

        elif int(indice) <= 0 or int(indice) > len(tarefas):
            print("Opção inválida.")
            continue   

        indice = int(indice) - 1

        del tarefas[indice]
        salvar_tarefas(tarefas)
        print("Tarefa removida com sucesso!")
        break