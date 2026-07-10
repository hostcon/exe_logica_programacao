# EXERCÍCIO 6 - Agenda de Contatos
agenda = []

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato)
    print(f"✅ Contato {nome} adicionado!")

def listar_contatos():
    if not agenda:
        print("📭 Agenda vazia!")
        return
    print("\n--- AGENDA ---")
    for i, c in enumerate(agenda):
        print(f"{i+1}. {c['nome']} - {c['telefone']} - {c['email']}")

def buscar_contato():
    busca = input("Digite o nome para buscar: ")
    encontrados = [c for c in agenda if busca.lower() in c['nome'].lower()]
    if encontrados:
        print("\n🔍 Resultados da busca:")
        for c in encontrados:
            print(f"- {c['nome']} - {c['telefone']}")
    else:
        print("❌ Nenhum contato encontrado.")

# Menu Principal
while True:
    print("\n=== MINHA AGENDA ===")
    print("1 - Adicionar contato")
    print("2 - Listar todos")
    print("3 - Buscar contato")
    print("4 - Sair")
    
    op = input("Opção: ")
    if op == "1":
        adicionar_contato()
    elif op == "2":
        listar_contatos()
    elif op == "3":
        buscar_contato()
    elif op == "4":
        print("👋 Até logo!")
        break
    else:
        print("❌ Opção inválida!")