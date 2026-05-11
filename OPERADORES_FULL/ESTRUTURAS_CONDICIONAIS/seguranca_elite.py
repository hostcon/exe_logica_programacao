idade = int(input("Sua idade: "))
tem_autorizacao_pais = input("Possui autorização dos pais? (sim/nao): ").lower()
tem_convite_vip = input("Possui convite VIP? (sim/nao): ").lower()

# Lógica complexa: entra se for maior de 18 OU se tiver autorização dos pais
if idade >= 18 or (tem_autorizacao_pais == "sim"):
    print("Verificando credenciais...")
    
    if tem_convite_vip == "sim":
        print("Bem-vindo ao Servidor VIP do Roblox! 🚀")
    else:
        print("Bem-vindo ao Servidor Padrão! 🎮")
        
else:
    print("Acesso bloqueado. Volte quando tiver 18 anos ou uma autorização assinada.")