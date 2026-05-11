idade = int(input("Informe sua idade para configurar seu perfil: "))

if idade >= 18:
    print("Perfil Master: Acesso total a chat livre e criação de servidores.")
elif idade >= 13:
    print("Perfil Jovem: Acesso a jogos com chat filtrado.")
elif idade >= 7:
    print("Perfil Kids: Acesso apenas a jogos educativos e chat desativado.")
else:
    print("Acesso negado: Procure um responsável para criar sua conta.")