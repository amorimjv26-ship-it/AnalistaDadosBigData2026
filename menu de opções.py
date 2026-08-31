print("\n--- 3. MENU DE OPÇÕES SIMPLES ---")

print("1 - Iniciar | 2 - Configurações | 3 - Ajuda | 4 - Sair")

opcao = int(input("Escolha uma opção"))

match opcao:
    case 1:
        print("Iniciando sistema...")
    case 2: 
        print("Abrindo configurções...")
    case 3: 
        print("Exibindo ajuda...")
    case 4:
        print("Saindo...")
    case _:
        print("Opção inválida")

        print("Entrada inválida.")
