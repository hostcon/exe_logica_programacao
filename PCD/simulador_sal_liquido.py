# EXERCÍCIO 1 - Salário Líquido
print("=== SIMULADOR DE SALÁRIO LÍQUIDO ===\n")

salario_bruto = float(input("Digite o valor do salário bruto: R$ "))
desconto_inss = float(input("Digite o percentual do INSS (ex: 9 para 9%): "))

valor_inss = salario_bruto * (desconto_inss / 100)
salario_liquido = salario_bruto - valor_inss

print(f"\n📊 Resumo:")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {valor_inss:.2f}")
print(f"✅ Salário Líquido: R$ {salario_liquido:.2f}")