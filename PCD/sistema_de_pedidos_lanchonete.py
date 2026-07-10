# EXERCÍCIO 5 - Caixa da Lanchonete
cardapio = {
    "1": {"nome": "X-Burguer", "preco": 15.00},
    "2": {"nome": "X-Salada", "preco": 18.00},
    "3": {"nome": "X-Bacon", "preco": 22.00},
    "4": {"nome": "Refrigerante", "preco": 7.00},
    "5": {"nome": "Suco Natural", "preco": 9.00}
}

print("=== LANCHONETE DO SEU ZÉ ===\n")
print("--- CARDÁPIO ---")
for cod, item in cardapio.items():
    print(f"{cod} - {item['nome']} - R$ {item['preco']:.2f}")

total_pedido = 0.0
pedido = []

while True:
    codigo = input("\nDigite o código do produto (ou 0 para finalizar): ")
    if codigo == "0":
        break
    if codigo in cardapio:
        qtd = int(input("Quantidade: "))
        subtotal = cardapio[codigo]["preco"] * qtd
        total_pedido += subtotal
        pedido.append(f"{qtd}x {cardapio[codigo]['nome']}")
        print(f"✅ Adicionado: {qtd}x {cardapio[codigo]['nome']} - Subtotal: R$ {subtotal:.2f}")
    else:
        print("❌ Código inválido!")

print("\n--- RESUMO DO PEDIDO ---")
for item in pedido:
    print(f"- {item}")
print(f"💰 Total do pedido: R$ {total_pedido:.2f}")

pagamento = float(input("Valor recebido do cliente: R$ "))
troco = pagamento - total_pedido
print(f"🔄 Troco: R$ {troco:.2f}")
print("✅ Pedido finalizado com sucesso!")