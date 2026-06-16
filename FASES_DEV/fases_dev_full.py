# ===========================================================
# PROJETO INCREMENTAL — CADASTRO DE NOMES
# Evolução completa: variáveis -> listas -> laços -> condicionais
#                     -> arquivos -> tratamento de erros -> funções
# ===========================================================
#
# Este arquivo contém a HISTÓRIA do projeto. As primeiras fases
# foram escritas com código solto (sem funções) só para aprender
# o conceito isolado. A partir da Fase 6, esse mesmo código foi
# reorganizado dentro de funções — por isso as versões "soltas"
# das fases 1 a 5 estão comentadas abaixo: elas já cumpriram seu
# papel de ensino e foram SUBSTITUÍDAS pelas funções equivalentes.
#
# Nada foi perdido — é só a evolução natural de "fazer funcionar"
# para "fazer bem feito".


# -----------------------------------------------------------
# FASE 1 — Variável e entrada de dados (substituída na Fase 6)
# -----------------------------------------------------------
# nome = input("Digite seu nome: ")
# print("Olá,", nome)
#
# Por que foi descontinuada: cadastrava só UM nome por vez,
# sem guardar em lista. A Fase 2 resolveu isso.


# -----------------------------------------------------------
# FASE 2 — Lista e laço while (substituída pela função
# adicionar_nome() + pelo menu da Fase 7)
# -----------------------------------------------------------
# nomes = []
# while True:
#     nome = input("Digite um nome (ou 'sair' para terminar): ")
#     if nome == "sair":
#         break
#     nomes.append(nome)
# for n in nomes:
#     print(n)
#
# Por que foi descontinuada: o cadastro ficava fixo num laço só,
# sem opção de buscar, salvar ou tratar erro. Hoje quem cuida de
# adicionar um nome é a função adicionar_nome(), chamada dentro
# do menu interativo da Fase 7.


# -----------------------------------------------------------
# FASE 3 — Busca e condicional (substituída pela função
# buscar_nome() + listar_nomes())
# -----------------------------------------------------------
# busca = input("Buscar nome: ")
# if busca in nomes:
#     print(f"{busca} encontrado!")
# else:
#     print(f"{busca} não está na lista.")
# for i, n in enumerate(nomes, 1):
#     print(f"{i}. {n}")
#
# Por que foi descontinuada: a lógica de buscar e listar virou
# função própria, reaproveitável em qualquer parte do programa,
# em vez de código solto que só rodava uma vez.


# -----------------------------------------------------------
# FASE 4 — Arquivo: salvar e carregar (substituída pelas
# funções salvar_nomes() e carregar_nomes())
# -----------------------------------------------------------
# with open("nomes.txt", "w", encoding="utf-8") as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + "\n")
# print("Nomes salvos!")
#
# with open("nomes.txt", "r", encoding="utf-8") as arquivo:
#     nomes_carregados = arquivo.read().splitlines()
# print("Nomes carregados:", nomes_carregados)
#
# Por que foi descontinuada: essa versão não tratava o erro de
# arquivo inexistente (FileNotFoundError) — a Fase 5 resolveu
# isso, e a Fase 6 organizou tudo em função.


# -----------------------------------------------------------
# FASE 5 — Tratamento de erros (substituída: a validação virou
# parte da função adicionar_nome(), e o try/except de leitura
# virou parte da função carregar_nomes())
# -----------------------------------------------------------
# try:
#     with open("nomes.txt", "r", encoding="utf-8") as f:
#         nomes = f.read().splitlines()
# except FileNotFoundError:
#     print("Arquivo não encontrado. Iniciando vazio.")
#     nomes = []
#
# def validar_nome(nome):
#     if not nome.strip():
#         raise ValueError("Nome não pode ser vazio.")
#     return nome.strip()
#
# try:
#     nome = validar_nome(input("Nome: "))
#     nomes.append(nome)
# except ValueError as e:
#     print(f"Erro: {e}")
#
# Por que foi descontinuada: essa lógica de validar e tratar
# erro é exatamente o que está dentro das funções abaixo —
# não precisa mais existir solta no meio do arquivo.


# ===========================================================
# FASE 6 — Funções (CÓDIGO ATIVO — é o que o programa usa hoje)
# ===========================================================
# A partir daqui o código deixa de ser "descartável" e passa a
# ser reutilizável: cada função tem uma única responsabilidade.

ARQUIVO = "nomes.txt"


def carregar_nomes():
    """Lê o arquivo e devolve a lista de nomes salvos.
    Se o arquivo não existir, devolve lista vazia (Fase 5)."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def salvar_nomes(nomes):
    """Grava a lista de nomes no arquivo, um por linha (Fase 4)."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")


def adicionar_nome(nomes, nome):
    """Valida e adiciona um nome à lista (Fases 2 + 5).
    Lança ValueError se o nome estiver vazio."""
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    nomes.append(nome.strip())


def buscar_nome(nomes, busca):
    """Verifica se um nome existe na lista (Fase 3)."""
    return busca in nomes


def listar_nomes(nomes):
    """Exibe todos os nomes numerados (Fase 3 + enumerate)."""
    if not nomes:
        print("Nenhum nome cadastrado ainda.")
        return
    for i, n in enumerate(nomes, 1):
        print(f"{i}. {n}")


# ===========================================================
# FASE 7 — Sistema completo com menu (CÓDIGO ATIVO)
# ===========================================================

def menu():
    """Exibe as opções e devolve a escolha do usuário."""
    print("\n--- CADASTRO DE NOMES ---")
    print("1. Adicionar nome")
    print("2. Listar nomes")
    print("3. Buscar nome")
    print("4. Salvar e sair")
    return input("Opção: ")


# if __name__ == "__main__" garante que esse bloco só roda
# quando o arquivo é executado diretamente — não quando é
# importado em outro módulo (explicado na pergunta do "include")
if __name__ == "__main__":
    nomes = carregar_nomes()  # carrega os dados salvos antes de começar

    while True:  # repete o menu até o usuário escolher a opção 4
        opcao = menu()  # PAUSA aqui esperando o usuário digitar e dar enter

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

        else:
            print("Opção inválida. Escolha entre 1 e 4.")
