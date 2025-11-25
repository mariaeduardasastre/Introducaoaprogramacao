opcao = 0

while opcao != 6:
    print("\n=== MENU ===")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Opção 4")
    print("5 - opção 5")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Você escolheu a Opção 1")
    elif opcao == 2:
        print("Você escolheu a Opção 2")
    elif opcao == 3:
        print("Você escolheu a Opção 3")
    elif opcao == 4:
        print("Você escolheu a Opção 4")
    elif opcao == 5:
        print("Você escolheu a opçao 5")
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida! Tente novamente.")
