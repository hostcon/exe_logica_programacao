import webbrowser

idade = int(input("Digite sua idade para acessar o portal: "))

if idade >= 18:
    print("Acesso liberado! Abrindo Roblox...")
    # O comando abaixo abre o navegador automaticamente
    webbrowser.open("https://www.roblox.com") 
else:
    print("Acesso restrito. Você precisa ter 18 anos ou mais para esta área.")
    print("Redirecionando para a área infantil...")