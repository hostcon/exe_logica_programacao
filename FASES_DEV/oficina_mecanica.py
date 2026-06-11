# ==============================================================================
# [BANCO DE DADOS EM MEMÓRIA] - Conexão Global
# Este arquivo funciona como o nosso "servidor" temporário.
# Ele precisa estar no topo para que todas as funções tenham acesso a ele.
# ==============================================================================
oficina_geral = []

# ==============================================================================
# BLOCO 6: MODULARIZAÇÃO (FUNÇÕES)
# Conexão Lógica: Isolamos o fluxo para que o código não vire uma maçaroca.
# O sistema principal apenas chama essa função quando um novo carro chega.
# ==============================================================================
def cadastrar_ordem_servico():
    print("\n--- NOVA ORDEM DE SERVIÇO ---")

    # --------------------------------------------------------------------------
    # BLOCO 1: ENTRADA E ESTADO
    # Conexão Lógica: Capturando os dados iniciais do mundo real.
    # --------------------------------------------------------------------------
    cliente = input("Nome do Cliente: ")
    modelo_carro = input("Modelo do Veículo: ")

    # --------------------------------------------------------------------------
    # BLOCO 2: VALIDAÇÃO E TRATAMENTO DE ERROS (TRY/EXCEPT)
    # Conexão Lógica: Protegendo o Bloco 1. Se o usuário digitar letras no ano
    # ou na quilometragem, o "try" falha, o "except" captura e o "while" repete.
    # Isso garante que os dados que vão para o Bloco 3 sejam puramente numéricos.
    # --------------------------------------------------------------------------
    while True:
        try:
            ano_carro = int(input("Ano do Veículo (AAAA): "))
            if ano_carro < 1900 or ano_carro > 2026:
                print("Por favor, digite um ano válido.")
                continue
            break
        except ValueError:
            print("Erro: O ano deve ser um número inteiro!")

    while True:
        try:
            quilometragem = int(input("Quilometragem Atual: "))
            if quilometragem < 0:
                print("A quilometragem não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: A quilometragem deve ser um número inteiro!")

    # --------------------------------------------------------------------------
    # BLOCO 3: ESTRUTURAS CONDICIONAIS (DIAGNÓSTICO)
    # Conexão Lógica: O "if" analisa as variáveis validadas no Bloco 2.
    # Criamos uma variável booleana (True/False) para carregar esse "estado" 
    # para os próximos blocos.
    # --------------------------------------------------------------------------
    necessita_revisao_completa = False

    if quilometragem > 10000 or ano_carro < 2020:
        print("\n⚠️ Alerta do Sistema: Veículo necessita de revisão preventiva!")
        necessita_revisao_completa = True
    else:
        print("\n✅ Status: Manutenção de rotina.")

    # --------------------------------------------------------------------------
    # BLOCO 4: ESTRUTURAS DE REPETIÇÃO (LOOPS & ACUMULADORES)
    # Conexão Lógica: O "while" permite lançar N itens sem saber o limite.
    # A variável "total_orcamento" acumula os valores a cada rodada do laço.
    # A lista "lista_pecas" (Bloco 4) captura os nomes para não serem perdidos.
    # --------------------------------------------------------------------------
    lista_pecas = []
    total_orcamento = 0.0

    print("\n--- LANÇAMENTO DE PEÇAS E SERVIÇOS ---")
    while True:
        peca = input("Nome da peça/serviço (ou 'fim' para encerrar): ").strip()
        
        if peca.lower() == 'fim':
            break  # Quebra o laço e envia o fluxo para o fechamento

        # Tratamento de erro específico para o preço da peça
        try:
            preco = float(input(f"Preço de '{peca}': R$ "))
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
            
            # A LIGAÇÃO: Guardamos o nome na lista e somamos o valor no acumulador
            lista_pecas.append(peca)
            total_orcamento += preco
        except ValueError:
            print("Erro: Preço inválido! Item desconsiderado. Tente novamente.")

    # --------------------------------------------------------------------------
    # BLOCO 5: ESTRUTURAÇÃO DE DADOS (DICIONÁRIOS)
    # Conexão Lógica: O "Grande Encaixe do Lego". Juntamos os dados do Bloco 1,
    # o veredito do Bloco 3, a lista e o total do Bloco 4 em uma única estrutura.
    # --------------------------------------------------------------------------
    ordem_servico = {
        "cliente": cliente,
        "veiculo": modelo_carro,
        "ano": ano_carro,
        "km": quilometragem,
        "alerta_revisao": necessita_revisao_completa,
        "itens": lista_pecas,
        "total": total_orcamento,
        "status": "Em Aberto"
    }

    # CONEXÃO FINAL: Injetamos o dicionário da O.S. na nossa lista global (banco de dados)
    oficina_geral.append(ordem_servico)
    print(f"\nOrdem de Serviço de {cliente} gerada com sucesso!")


# ==============================================================================
# FUNÇÃO DE VISUALIZAÇÃO (PREPARAÇÃO PARA O FLASK)
# Conexão Lógica: Essa função simula exatamente o que o Flask fará na web:
# ela varre a lista global e exibe os dados estruturados de cada dicionário.
# ==============================================================================
def listar_todas_as_ordens():
    print("\n=============================================")
    print("       RELATÓRIO GERAL DA OFICINA            ")
    print("=============================================")
    
    if not oficina_geral:
        print("Nenhum veículo em manutenção no momento.")
        return

    # O "for" percorre a lista de dicionários
    for indice, ordem in enumerate(oficina_geral, 1):
        print(f"\n#OS: {indice} | Cliente: {ordem['cliente']} | Carro: {ordem['veiculo']}")
        print(f"Ano: {ordem['ano']} | KM: {ordem['km']}")
        print(f"Revisão Crítica: {'SIM' if ordem['alerta_revisao'] else 'NÃO'}")
        print(f"Itens Trocados: {', '.join(ordem['itens']) if ordem['itens'] else 'Nenhum item lançado'}")
        print(f"Total: R$ {ordem['total']:.2f}")
        print(f"Status: {ordem['status']}")
        print("-" * 45)


# ==============================================================================
# FLUXO PRINCIPAL DO SISTEMA (MENU INTERATIVO)
# Conexão Lógica: O coração do programa no console. Mantém o sistema rodando
# até que o usuário decida fechar o programa.
# ==============================================================================
while True:
    print("\n=== SISTEMA OFICINA INTELIGENTE ===")
    print("1. Cadastrar Nova Ordem de Serviço")
    print("2. Listar Ordens de Serviço (Relatório)")
    print("3. Sair do Sistema")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_ordem_servico()
    elif opcao == "2":
        listar_todas_as_ordens()
    elif opcao == "3":
        print("Fechando o sistema. Até logo, meu caro!")
        break
    else:
        print("Opção inválida! Tente novamente.")