import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ====================================================
# CRIAÇÃO DO BANCO
# ====================================================

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

conexao.commit()

# ====================================================
# FUNÇÃO CADASTRAR
# ====================================================

def cadastrar():

    usuario = edt_login.get()
    senha = edt_senha.get()

    if usuario == "" or senha == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha login e senha."
        )
        return

    try:

        cursor.execute(
            "INSERT INTO usuarios(login, senha) VALUES (?, ?)",
            (usuario, senha)
        )

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Usuário cadastrado!"
        )

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Erro",
            "Usuário já existe."
        )

# ====================================================
# FUNÇÃO LOGIN
# ====================================================

def login():

    usuario = edt_login.get()
    senha = edt_senha.get()

    cursor.execute(
        """
        SELECT * 
        FROM usuarios
        WHERE login = ?
        AND senha = ?
        """,
        (usuario, senha)
    )

    resultado = cursor.fetchone()

    if resultado:

        nova_janela = tk.Toplevel()

        nova_janela.title("Sistema")
        nova_janela.geometry("400x250")

        ttk.Label(
            nova_janela,
            text=f"Bem-vindo, {usuario}!",
            font=("Arial", 16)
        ).pack(pady=30)

    else:

        messagebox.showerror(
            "Erro",
            "Login inválido."
        )

# ====================================================
# JANELA
# ====================================================

janela = tk.Tk()

janela.title("Sistema de Login")
janela.geometry("600x250")

# ====================================================
# LOGIN
# ====================================================

lbl_login = ttk.Label(
    janela,
    text="Login:"
)

# row = linha
# column = coluna
# sticky="w" -> esquerda (west)

lbl_login.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

# ====================================================
# ENTRY LOGIN
# ====================================================

edt_login = ttk.Entry(
    janela,
    width=25
)

edt_login.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

# ====================================================
# SENHA
# ====================================================

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

# ====================================================
# ENTRY SENHA
# ====================================================

edt_senha = ttk.Entry(
    janela,
    width=25,
    show="*"      # Esconde a senha
)

edt_senha.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

# ====================================================
# BOTÃO LOGIN
# ====================================================

btn_login = ttk.Button(
    janela,
    text="Entrar",
    command=login
)

btn_login.grid(
    row=2,
    column=0,
    padx=10,
    pady=15
)

# ====================================================
# BOTÃO CADASTRAR
# ====================================================

btn_cadastrar = ttk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
)

btn_cadastrar.grid(
    row=2,
    column=1,
    padx=10,
    pady=15,
    sticky="w"
)

# ====================================================
# ÁREA DE IMAGEM
# ====================================================

# Frame servindo como local reservado
# para uma imagem futuramente

frame_imagem = ttk.LabelFrame(
    janela,
    text="Logo"
)

frame_imagem.grid(
    row=0,
    column=2,

    # ocupa as 3 linhas:
    # login, senha e botões
    rowspan=3,

    padx=20,
    pady=10,

    sticky="nsew"
)

# Placeholder

lbl_imagem = ttk.Label(
    frame_imagem,
    text="Imagem\n300 x 150"
)

lbl_imagem.pack(
    expand=True,
    padx=30,
    pady=30
)

# ====================================================
# CONFIGURAÇÃO DAS COLUNAS
# ====================================================

# Permite expansão da coluna da imagem

janela.columnconfigure(2, weight=1)

# ====================================================
# LOOP
# ====================================================

janela.mainloop()

# ====================================================
# FECHA CONEXÃO
# ====================================================

conexao.close()