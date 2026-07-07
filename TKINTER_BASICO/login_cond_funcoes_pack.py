import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ==================================
# Janela Principal
# ==================================

janela = tk.Tk()
janela.title("Financiamento de Imóveis")
janela.geometry("400x250")

# ==================================
# Login
# ==================================

lbl_login = ttk.Label(
    janela,
    text="Login",
    font=("Arial", 12)
)

# Anchor NW = Norte-Oeste (canto superior esquerdo)
lbl_login.pack(anchor="nw", pady=2, padx=10)

edt_login = tk.Entry(janela, width=25)
edt_login.pack(anchor="nw", pady=2, padx=10)

# ==================================
# Senha
# ==================================

lbl_senha = ttk.Label(
    janela,
    text="Senha",
    font=("Arial", 12)
)

lbl_senha.pack(anchor="nw", pady=2, padx=10)

# show="*" esconde os caracteres digitados
edt_senha = tk.Entry(
    janela,
    width=25,
    show="*"
)

edt_senha.pack(anchor="nw", pady=2, padx=10)

# ==================================
# Função Login
# ==================================

def login():

    usuario = edt_login.get()
    senha = edt_senha.get()

    # Ambos devem estar corretos
    if usuario == "wagner" and senha == "123":

        # Nova janela
        nova_janela = tk.Toplevel()

        nova_janela.title("Sistema")
        nova_janela.geometry("300x200")

        ttk.Label(
            nova_janela,
            text=f"Bem-vindo, {usuario}!",
            font=("Arial", 14)
        ).pack(pady=30)

    else:
        messagebox.showerror(
            "Erro",
            "Usuário ou senha inválidos."
        )

# ==================================
# Botão Login
# ==================================

botao = tk.Button(
    janela,
    text="Login",
    command=login
)

botao.pack(anchor="nw", pady=10, padx=10)

# ==================================
# Executa aplicação
# ==================================

janela.mainloop()