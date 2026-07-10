# EXERCÍCIO 10 - Controle de Presença e Tarefas
alunos = {}
tarefas = []

# Cadastro de alunos (para chamada)
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    alunos[nome] = {"presenca": 0, "faltas": 0}
    print(f"✅ Aluno {nome} cadastrado!")

# Chamada diária
def fazer_chamada():
    data = input("Data da aula (dd/mm/aaaa): ")
    print("\n--- CHAMADA ---")
    for nome in alunos:
        status = input(f"{nome} - Presente? (s/n): ")
        if status.lower() == 's':
            alunos[nome]["presenca"] += 1
        else:
            alunos[nome]["faltas"] += 1
    print(f"✅ Chamada do dia {data} registrada!")

# Relatório de presença
def relatorio_presenca():
    print("\n--- RELATÓRIO DE PRESENÇA ---")
    for nome, dados in alunos.items():
        total = dados["presenca"] + dados["faltas"]
        if total > 0:
            freq = (dados["presenca"] / total) * 100
            print(f"{nome}: {dados['presenca']} presenças, {dados['faltas']} faltas ({freq:.1f}% de frequência)")

# Lista de tarefas
def gerenciar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
    else:
        for i, t in enumerate(tarefas):
            status = "✅" if t["concluida"] else "⏳"
            print(f"{i+1}. {status} {t['descricao']}")
    
    print("\n1 - Adicionar tarefa")
    print("2 - Concluir tarefa")
    print("3 - Voltar")
    op = input("Opção: ")
    
    if op == "1":
        desc = input("Descrição da tarefa: ")
        tarefas.append({"descricao": desc, "concluida": False})
        print("✅ Tarefa adicionada!")
    elif op == "2":
        idx = int(input("Número da tarefa a concluir: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            print(f"✅ Tarefa '{tarefas[idx]['descricao']}' concluída!")
        else:
            print("❌ Número inválido!")

# Menu principal
while True:
    print("\n=== SISTEMA DA TURMA ===")
    print("1 - Cadastrar aluno")
    print("2 - Fazer chamada")
    print("3 - Relatório de presença")
    print("4 - Gerenciar tarefas")
    print("5 - Sair")
    
    op = input("Opção: ")
    if op == "1":
        cadastrar_aluno()
    elif op == "2":
        fazer_chamada()
    elif op == "3":
        relatorio_presenca()
    elif op == "4":
        gerenciar_tarefas()
    elif op == "5":
        print("👋 Até a próxima turma!")
        break
    else:
        print("❌ Opção inválida!")