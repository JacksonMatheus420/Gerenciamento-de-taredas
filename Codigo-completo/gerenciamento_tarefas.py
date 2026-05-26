# Gerenciamento de Tarefas Simples

tarefas = []

def mostrar_menu():
    print('\n===== GERENCIADOR DE TAREFAS ======')
    print("1 - Adicionar tarefas")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefas")
    print("4 - Remover tarefas")
    print("5 - Sair")

def adicionar_tarefas():
    tarefa = input("Digite a nova tarefa: ")

    tarefas.append({"nome": tarefa,
                   "concluida": False})

    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n ===== SUAS TAREFAS =====")

    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "X"
        print(f"{i + 1}. [{status}] {tarefa["nome"]}") 

def concluir_tarefa():
    listar_tarefas()

    if len(tarefas) == 0:
        return
    
    numero = int(input("Digite o número da tarefa concluída: "))

    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()

    if len(tarefas) == 0:
        return

    numero = int(input("Digite o número da tarefa para remover: "))

    if 1 <= numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{tarefa_removida['nome']}' removida!")
    else:
        print("Número inválido.")

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefas()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")                     