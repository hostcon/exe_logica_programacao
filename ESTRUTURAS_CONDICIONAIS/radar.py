print("=== RADAR DE TRÂNSITO ===")
velocidade = int(input("Qual a velocidade do carro (em km/h)? "))

limite = 80

if velocidade > limite:
    km_acima = velocidade - limite
    valor_multa = km_acima * 5.00
    
    print("🚨 ALERTA: Você foi multado por excesso de velocidade!")
    print(f"Sua multa é de R$ {valor_multa:.2f}")
else:
    print("✅ Velocidade dentro do limite. Boa viagem!")