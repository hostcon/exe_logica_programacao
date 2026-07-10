# EXERCÍCIO 7 - Ordem de Serviço e Orçamento
import datetime

def gerar_os():
    print("\n=== NOVA ORDEM DE SERVIÇO ===\n")
    
    # Dados do cliente
    nome_cliente = input("Nome do cliente: ")
    veiculo = input("Modelo do veículo: ")
    placa = input("Placa: ")
    
    # Serviços/Peças
    itens = []
    total = 0.0
    
    print("\n--- ADICIONE OS ITENS DO SERVIÇO ---")
    while True:
        descricao = input("Descrição do serviço/peça (ou 'fim' para encerrar): ")
        if descricao.lower() == 'fim':
            break
        valor = float(input("Valor: R$ "))
        itens.append({"descricao": descricao, "valor": valor})
        total += valor
        print(f"✅ Item adicionado! Subtotal: R$ {total:.2f}")
    
    # Mão de obra (opcional)
    mao_obra = float(input("\nValor da mão de obra: R$ "))
    total += mao_obra
    
    # Data e número da OS
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    num_os = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Salvar em arquivo
    with open(f"OS_{num_os}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"=== ORDEM DE SERVIÇO Nº {num_os} ===\n")
        arquivo.write(f"Data: {data}\n")
        arquivo.write(f"Cliente: {nome_cliente}\n")
        arquivo.write(f"Veículo: {veiculo} - Placa: {placa}\n")
        arquivo.write("-" * 40 + "\n")
        for item in itens:
            arquivo.write(f"{item['descricao']}: R$ {item['valor']:.2f}\n")
        arquivo.write("-" * 40 + "\n")
        arquivo.write(f"Mão de obra: R$ {mao_obra:.2f}\n")
        arquivo.write(f"✅ TOTAL DO ORÇAMENTO: R$ {total:.2f}\n")
    
    print(f"\n✅ OS gerada com sucesso! Arquivo salvo: OS_{num_os}.txt")
    print(f"💰 Valor total do orçamento: R$ {total:.2f}")

# Executar
gerar_os()