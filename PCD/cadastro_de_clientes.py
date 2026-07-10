# EXERCÍCIO 4 - Cadastro de Clientes e Estoque
clientes = []
estoque = []

print("=== SISTEMA DA OFICINA ===\n")

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Produto no Estoque")
    print("3 - Listar Clientes")
    print("4 - Listar Estoque")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        cliente = {"nome": nome, "telefone": telefone}
        clientes.append(cliente)
        print(f"✅ Cliente {nome} cadastrado com sucesso!")
        
    elif opcao == "2":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade em estoque: "))
        item = {"produto": produto, "quantidade": quantidade}
        estoque.append(item)
        print(f"✅ Produto {produto} adicionado ao estoque!")
        
    elif opcao == "3":
        print("\n--- LISTA DE CLIENTES ---")
        for c in clientes:
            print(f"👤 {c['nome']} - Tel: {c['telefone']}")
            
    elif opcao == "4":
        print("\n--- ESTOQUE ---")
        for e in estoque:
            print(f"📦 {e['produto']}: {e['quantidade']} unidades")
            
    elif opcao == "5":
        print("👋 Encerrando sistema...")
        break
    else:
        print("❌ Opção inválida!")