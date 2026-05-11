# 1. Definimos as credenciais "cadastradas" no sistema
usuario_correto = "instrutor"
senha_correta = "senai123"

print("=== 🔐 SISTEMA DE ACESSO SENAI ===")

# 2. Entrada de dados do aluno
usuario_input = input("Usuário: ").lower()
senha_input = input("Senha: ")

# 3. Lógica de múltiplas condições
if usuario_input == usuario_correto and senha_input == senha_correta:
    print("\n✅ Acesso Liberado!")
    print("Bem-vindo ao painel de controle, Instrutor Wagner.")
    
elif usuario_input == usuario_correto and senha_input != senha_correta:
    print("\n❌ Senha incorreta!")
    print("Dica: A senha padrão termina com '123'.")
    
elif usuario_input != usuario_correto and senha_input == senha_correta:
    print("\n👤 Usuário não encontrado, mas a senha coincide com outro perfil.")
    
else:
    print("\n🚫 ACESSO NEGADO!")
    print("Usuário e senha não constam na nossa base de dados.")