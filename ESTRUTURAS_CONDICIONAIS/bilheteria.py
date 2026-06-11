print("=== BILHETERIA AUTOMÁTICA ===")
idade = int(input("Bem-vindo! Qual é a sua idade? "))

if idade < 12:
    print("Você tem direito ao Ingresso Infantil. Valor: R$ 10,00.")
elif idade < 18:
    print("Você tem direito ao Ingresso Adolescente (Meia). Valor: R$ 15,00.")
elif idade < 60:
    print("Você deve comprar o Ingresso Adulto (Inteira). Valor: R$ 30,00.")
else:
    print("Você tem direito ao Ingresso Sênior. Valor: R$ 15,00.")