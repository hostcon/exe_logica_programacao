# EXERCÍCIO 2 - Comparador Álcool x Gasolina
print("=== QUAL COMBUSTÍVEL COMPENSA MAIS? ===\n")

preco_alcool = float(input("Preço do litro do ÁLCOOL: R$ "))
preco_gasolina = float(input("Preço do litro da GASOLINA: R$ "))

relacao = preco_alcool / preco_gasolina

print(f"\n🔎 A relação é: {relacao:.2f}")

if relacao < 0.70:
    print("✅ COMPENSA ABASTECER COM ÁLCOOL!")
else:
    print("✅ COMPENSA ABASTECER COM GASOLINA!")