import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ==================================
# Janela Principal
# ==================================

janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("350x200")

# ==================================
# Função Login
# ==================================

def login():

    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "wagner" and senha == "123":

        nova_janela = tk.Toplevel()

        nova_janela.title("Menu Principal")
        nova_janela.geometry("300x200")

        lbl_boas_vindas = ttk.Label(
            nova_janela,
            text=f"Bem-vindo, {usuario}!",
            font=("Arial", 14)
        )

        lbl_boas_vindas.pack(pady=30)

    else:

        messagebox.showerror(
            "Erro",
            "Usuário ou senha inválidos!"
        )

# ==================================
# LOGIN
# ==================================

lbl_login = ttk.Label(
    janela,
    text="Login:"
)

# row = linha
# column = coluna
# padx = espaço horizontal
# pady = espaço vertical
# sticky="w" = alinhado à esquerda (West)

lbl_login.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

# ==================================
# CAMPO LOGIN
# ==================================

edt_login = ttk.Entry(
    janela,
    width=25
)

# Linha 0, coluna 1

edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

# ==================================
# SENHA
# ==================================

lbl_senha = ttk.Label(
    janela,
    text="Senha:"
)

lbl_senha.grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

# ==================================
# CAMPO SENHA
# ==================================

edt_senha = ttk.Entry(
    janela,
    width=25,
    show="*"      # Oculta os caracteres digitados
)

edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

# ==================================
# BOTÃO LOGIN
# ==================================

btn_login = ttk.Button(
    janela,
    text="Entrar",
    command=login
)

# columnspan=2 faz o botão ocupar
# as duas colunas do formulário

btn_login.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15
)

# ==================================
# LOOP PRINCIPAL
# ==================================

janela.mainloop()