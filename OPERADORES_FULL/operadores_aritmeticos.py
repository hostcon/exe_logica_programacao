# ============================================================
#  OPERADORES ARITMÉTICOS E FORMATAÇÃO DE FLOAT EM PYTHON
#  Curso: Python Full Course for Free — Bro Code
#  Adaptado para o Brasil | SENAI/FIEP
# ============================================================


# ------------------------------------------------------------
#  1. ADIÇÃO  ( + )
#     Soma dois valores. Funciona com int e float.
# ------------------------------------------------------------

preco  = 49.90   # preço do produto
frete  = 12.50   # custo do frete

total  = preco + frete

print("=== ADIÇÃO ===")
print(f"Preço:  R$ {preco}")
print(f"Frete:  R$ {frete}")
print(f"Total:  R$ {total}")       # 62.4


# ------------------------------------------------------------
#  2. SUBTRAÇÃO  ( - )
#     Diferença entre dois valores.
# ------------------------------------------------------------

saldo = 1500.00  # saldo inicial na conta
saque =  350.00  # valor retirado

saldo = saldo - saque  # atualiza o saldo

print("\n=== SUBTRAÇÃO ===")
print(f"Saldo após saque: R$ {saldo}")   # 1150.0


# ------------------------------------------------------------
#  3. MULTIPLICAÇÃO  ( * )
#     Produto de dois valores. Muito usado em totais de pedido.
# ------------------------------------------------------------

preco_unit = 8.90   # preço unitário do feijão
quantidade = 5      # número de pacotes

total_pedido = preco_unit * quantidade

print("\n=== MULTIPLICAÇÃO ===")
print(f"Total do pedido: R$ {total_pedido}")   # 44.5


# ------------------------------------------------------------
#  4. DIVISÃO  ( / )
#     Sempre retorna float — mesmo 10 / 2 retorna 5.0, não 5!
# ------------------------------------------------------------

nota1 = 8.5
nota2 = 7.0
nota3 = 9.0

media = (nota1 + nota2 + nota3) / 3   # divisão sempre gera float

print("\n=== DIVISÃO ===")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média: {media}")              # 8.166666666666666
print(f"10 / 2 = {10 / 2}")          # 5.0  (float, não inteiro!)


# ------------------------------------------------------------
#  5. DIVISÃO INTEIRA  ( // )
#     Divide e descarta a parte decimal — retorna int.
#     Muito usado para converter segundos em minutos/horas.
# ------------------------------------------------------------

segundos_totais = 500

minutos = segundos_totais // 60   # quantos minutos completos cabem?
segundos_resto = segundos_totais % 60   # sobra quanto? (ver módulo abaixo)

print("\n=== DIVISÃO INTEIRA ===")
print(f"{segundos_totais} segundos = {minutos} minuto(s) e {segundos_resto} segundo(s)")
# 500 segundos = 8 minuto(s) e 20 segundo(s)

# Outro uso: descobrir se um número é par ou ímpar via índice
for i in range(6):
    tipo = "par" if i % 2 == 0 else "ímpar"
    print(f"  {i} // 2 = {i // 2}  →  {i} é {tipo}")


# ------------------------------------------------------------
#  6. MÓDULO / RESTO  ( % )
#     Retorna o resto da divisão inteira.
#     Usos comuns: verificar par/ímpar, extrair dígitos,
#     girar posições em listas (índice circular).
# ------------------------------------------------------------

print("\n=== MÓDULO (RESTO) ===")

# Resto de segundos após converter para minutos
print(f"500 % 60 = {500 % 60}")       # 20  (sobram 20 segundos)

# Verificar se CPF termina em dígito par
cpf_ultimo_digito = 7
print(f"Último dígito {cpf_ultimo_digito} é par? {cpf_ultimo_digito % 2 == 0}")  # False

# Índice circular — útil em filas e rodízios
equipe = ["Ana", "Bruno", "Carol", "Diego"]
print("Escala circular de atendimento:")
for turno in range(8):
    atendente = equipe[turno % len(equipe)]   # volta ao início quando acaba
    print(f"  Turno {turno + 1}: {atendente}")


# ------------------------------------------------------------
#  7. POTENCIAÇÃO  ( ** )
#     Base elevada ao expoente.
#     Mais rápido que math.pow() para inteiros.
#     Aceita expoentes negativos e fracionários.
# ------------------------------------------------------------

print("\n=== POTENCIAÇÃO ===")

# Área do círculo: π × r²
raio = 5
area = 3.14159 * raio ** 2
print(f"Área do círculo (r={raio}): {area}")   # 78.53975

# Juros compostos: capital × (1 + taxa)^meses
capital = 1000.00
taxa_mensal = 0.01    # 1% ao mês
meses = 12
montante = capital * (1 + taxa_mensal) ** meses
print(f"Montante após {meses} meses: R$ {montante:.2f}")  # R$ 1126.83

# Raiz quadrada usando expoente fracionário (0.5 = ½)
numero = 144
raiz = numero ** 0.5
print(f"Raiz quadrada de {numero}: {raiz}")    # 12.0

# Potência negativa (equivale a 1/x^n)
print(f"2 ** -3 = {2 ** -3}")                  # 0.125  (= 1/8)


# ============================================================
#  FORMATAÇÃO DE CASAS DECIMAIS EM FLOAT
#  Sintaxe dentro de f-string: {valor:.Nf}
#  N = número de casas decimais desejado
# ============================================================

print("\n" + "=" * 50)
print("  FORMATAÇÃO DE FLOAT")
print("=" * 50)

valor = 1234.5678
pi    = 3.14159265358979

# --- Sem formatação: exibe todos os dígitos ---
print(f"\nSem formato:       {valor}")
# → 1234.5678

# --- .2f → 2 casas decimais (padrão para reais) ---
print(f":.2f (2 casas):    {valor:.2f}")
# → 1234.57  (arredonda a última casa)

# --- .0f → nenhuma casa decimal ---
print(f":.0f (0 casas):    {valor:.0f}")
# → 1235  (arredonda para inteiro, mas continua sendo float)

# --- .4f → 4 casas (precisão maior, ex: taxa de câmbio) ---
print(f":.4f (4 casas):    {pi:.4f}")
# → 3.1416

# --- :,.2f → separador de milhar + 2 casas ---
#   Atenção: em Python o separador de milhar é vírgula (,)
#   Para exibir no padrão brasileiro (ponto), substitua depois
print(f":,.2f (milhar):    {valor:,.2f}")
# → 1,234.57

# --- :.1% → porcentagem automática (multiplica por 100) ---
taxa_aprovacao = 0.876
print(f":.1% (porcento):   {taxa_aprovacao:.1%}")
# → 87.6%

# --- :.2e → notação científica ---
muito_pequeno = 0.000123456
print(f":.2e (científico): {muito_pequeno:.2e}")
# → 1.23e-04

# --- round() → arredonda e devolve um número (não só texto) ---
#   Use quando precisar do valor arredondado para calcular depois
x = round(pi, 2)
print(f"round(pi, 2):      {x}")          # 3.14  (float)
print(f"round(pi, 2) + 1 = {x + 1}")     # 4.14  (ainda é número!)


# ============================================================
#  EXEMPLO INTEGRADOR: NOTA FISCAL SIMPLIFICADA
#  Usa adição, multiplicação, divisão e formatação de float
# ============================================================

print("\n" + "=" * 50)
print("  NOTA FISCAL — EXEMPLO INTEGRADOR")
print("=" * 50)

itens = [
    ("Feijão Carioca 1kg",  8.90, 3),
    ("Arroz Branco 5kg",   22.50, 2),
    ("Óleo de Soja 900ml",  9.70, 4),
    ("Macarrão Espaguete",  4.30, 6),
]

subtotal = 0.0

print(f"\n{'PRODUTO':<25} {'QTD':>4} {'UNIT':>8} {'SUBTOTAL':>10}")
print("-" * 52)

for nome, preco_u, qtd in itens:
    sub = preco_u * qtd           # multiplicação
    subtotal += sub               # adição acumulativa
    print(f"{nome:<25} {qtd:>4} R${preco_u:>6.2f} R${sub:>8.2f}")

desconto_pct = 0.05               # 5% de desconto
desconto_val = subtotal * desconto_pct
total_final  = subtotal - desconto_val

print("-" * 52)
print(f"{'Subtotal':<38} R${subtotal:>8.2f}")
print(f"{'Desconto (5%)':<38} R${desconto_val:>8.2f}")
print(f"{'TOTAL':<38} R${total_final:>8.2f}")

# Divisão: valor médio por item
media_por_item = total_final / len(itens)
print(f"\nMédia por item: R$ {media_por_item:.2f}")

# Módulo e divisão inteira: parcelamento
parcelas = 3
valor_parcela = total_final / parcelas
centavos_resto = round((total_final % parcelas) * 100)   # resto em centavos
print(f"Parcelado em {parcelas}x: R$ {valor_parcela:.2f}/parcela")
print(f"  (diferença de {centavos_resto} centavo(s) na última parcela)")
