# EXERCÍCIO 8 - Simulador de Férias e 13º Salário
import datetime

print("=== SIMULADOR TRABALHISTA ===\n")

salario = float(input("Salário mensal: R$ "))
meses_trabalhados = int(input("Meses trabalhados no ano (1 a 12): "))

# Cálculo do 13º
decimo_terceiro = (salario / 12) * meses_trabalhados

# Cálculo das férias (considerando 30 dias)
ferias = salario + (salario / 3)  # Salário + 1/3 constitucional

print("\n📊 RESULTADOS:")
print(f"✅ 13º Salário proporcional: R$ {decimo_terceiro:.2f}")
print(f"✅ Férias (30 dias + 1/3): R$ {ferias:.2f}")

# Desafio extra: Se o aluno tirar férias em um mês específico
opcao = input("\nDeseja calcular com desconto do INSS? (s/n): ")
if opcao.lower() == 's':
    inss_13 = decimo_terceiro * 0.09
    inss_ferias = ferias * 0.09
    print(f"Desconto INSS sobre 13º: R$ {inss_13:.2f}")
    print(f"Desconto INSS sobre férias: R$ {inss_ferias:.2f}")
    print(f"13º líquido: R$ {decimo_terceiro - inss_13:.2f}")
    print(f"Férias líquidas: R$ {ferias - inss_ferias:.2f}")