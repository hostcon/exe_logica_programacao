# EXERCÍCIO 9 - Locadora de Ferramentas / Biblioteca
from datetime import datetime, timedelta

acervo = []
emprestimos = []

def cadastrar_item():
    tipo = input("Tipo (ferramenta/livro): ")
    nome = input("Nome do item: ")
    codigo = input("Código de identificação: ")
    item = {"tipo": tipo, "nome": nome, "codigo": codigo, "disponivel": True}
    acervo.append(item)
    print(f"✅ {nome} cadastrado com sucesso!")

def emprestar_item():
    codigo = input("Código do item a emprestar: ")
    for item in acervo:
        if item["codigo"] == codigo and item["disponivel"]:
            nome_cliente = input("Nome do cliente: ")
            data_emprestimo = datetime.now()
            data_devolucao = data_emprestimo + timedelta(days=3)  # 3 dias de prazo
            
            emprestimo = {
                "cliente": nome_cliente,
                "item": item["nome"],
                "codigo": codigo,
                "data_emprestimo": data_emprestimo.strftime("%d/%m/%Y"),
                "data_devolucao": data_devolucao.strftime("%d/%m/%Y")
            }
            emprestimos.append(emprestimo)
            item["disponivel"] = False
            print(f"✅ Empréstimo realizado! Devolver até: {data_devolucao.strftime('%d/%m/%Y')}")
            return
    print("❌ Item não disponível ou não encontrado!")

def listar_emprestimos():
    if not emprestimos:
        print("📭 Nenhum empréstimo ativo.")
        return
    print("\n--- EMPRÉSTIMOS ATIVOS ---")
    for e in emprestimos:
        print(f"📌 {e['cliente']} - {e['item']} (Devolução: {e['data_devolucao']})")

# Menu principal
while True:
    print("\n=== SISTEMA DE LOCAÇÃO ===")
    print("1 - Cadastrar item")
    print("2 - Realizar empréstimo")
    print("3 - Listar empréstimos")
    print("4 - Sair")
    
    op = input("Opção: ")
    if op == "1":
        cadastrar_item()
    elif op == "2":
        emprestar_item()
    elif op == "3":
        listar_emprestimos()
    elif op == "4":
        print("👋 Sistema encerrado!")
        break
    else:
        print("❌ Opção inválida!")