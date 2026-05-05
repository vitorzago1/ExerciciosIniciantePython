def exibir_menu():
    print("\n--- GERENCIADOR DE TAREFAS v1.0 ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def main():
    tarefas = []
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Digite a descrição da tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
        elif escolha == '2':
            print("\n--- SUAS TAREFAS ---")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
        elif escolha == '3':
            try:
                indice = int(input("Digite o número da tarefa para remover: "))
                tarefas.pop(indice - 1)
                print("Tarefa removida!")
            except:
                print("Número inválido.")
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()