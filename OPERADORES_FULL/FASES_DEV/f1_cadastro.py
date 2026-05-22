# -----------------------------------------
# FASE 1 — Variável e entrada de dados
# O programa recebe UM nome e exibe na tela
# -----------------------------------------

# input() pausa o programa e espera o usuário digitar
# o que foi digitado é guardado na variável 'nome'
nome = input("Digite seu nome: ")

# print() exibe o valor guardado na variável
print("Olá,", nome)

# -----------------------------------------
# FASE 2 — Lista e laço while
# Agora guardamos VÁRIOS nomes
# -----------------------------------------

# [] cria uma lista vazia — vai crescer a cada cadastro
nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para terminar): ")
    if nome == "sair":
        break
    nomes.append(nome)
for n in nomes:
    print(n)

# (código das fases anteriores mantido acima)
# -----------------------------------------
# FASE 3 — Busca com condicional
# -----------------------------------------
busca = input("Buscar nome: ")
if busca in nomes:
    print(f"{busca} encontrado!")
else:
    print(f"{busca} não está na lista.")
for i, n in enumerate(nomes, 1):
    print(f"{i}. {n}")

# (código das fases anteriores mantido acima)
# -----------------------------------------
# FASE 4 — Salvar e carregar de arquivo
# -----------------------------------------

with open("nomes.txt", "w", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")
print("Nomes salvos!")
with open("nomes.txt", "r", encoding="utf-8") as arquivo:
    nomes_carregados = arquivo.read().splitlines()
print("Nomes carregados:", nomes_carregados)

# (código das fases anteriores mantido acima)
# -----------------------------------------
# FASE 5 — Tratamento de erros
# -----------------------------------------

# try tenta executar o bloco
# except captura o erro específico se ele acontecer
try:
    with open("nomes.txt", "r", encoding="utf-8") as f:
        nomes = f.read().splitlines()
except FileNotFoundError:
    print("Arquivo não encontrado. Iniciando vazio.")
    nomes = []

def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    return nome.strip()

try:
    nome = validar_nome(input("Nome: "))
    nomes.append(nome)
except ValueError as e:
    print(f"Erro: {e}")


# -----------------------------------------
# FASE 6 — Organização em funções
# Cada função faz UMA coisa — princípio básico
# -----------------------------------------
ARQUIVO = "nomes.txt"

def carregar_nomes():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def salvar_nomes(nomes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")

def adicionar_nome(nomes, nome):
    if not nome.strip():
        raise ValueError("Nome vazio.")
    nomes.append(nome.strip())

def buscar_nome(nomes, busca):
    return busca in nomes

def listar_nomes(nomes):
    for i, n in enumerate(nomes, 1):
        print(f"{i}. {n}")

nomes = carregar_nomes()

# -----------------------------------------
# FASE 7 — Sistema completo com menu
# Todas as funções se unem aqui
# -----------------------------------------

# (todas as funções das fases anteriores acima)
def menu():
    print("\n--- CADASTRO DE NOMES ---")
    print("1. Adicionar nome")
    print("2. Listar nomes")
    print("3. Buscar nome")
    print("4. Salvar e sair")
    return input("Opção: ")

if __name__ == "__main__":
    nomes = carregar_nomes()
    while True:
        opcao = menu()
        if opcao == "1":
            try:
                adicionar_nome(nomes, input("Nome: "))
                print("Adicionado!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            listar_nomes(nomes)
        elif opcao == "3":
            busca = input("Buscar: ")
            achou = buscar_nome(nomes, busca)
            print("Encontrado!" if achou else "Não encontrado.")
        elif opcao == "4":
            salvar_nomes(nomes)
            print("Salvo. Até logo!")
            break


