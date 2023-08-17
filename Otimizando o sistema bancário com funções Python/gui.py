import tkinter as tk
from tkinter import messagebox
from banking_system_v2 import *

# Código das funções e variáveis omitido para manter o foco na parte relacionada à GUI

# Função chamada quando o botão de login é clicado
def login_button_click():
    cpf = cpf_entry.get()
    senha = senha_entry.get()

    if cpf in users and users[cpf]["senha"] == senha:
        messagebox.showinfo("Login", f"Bem-vindo, {users[cpf]['nome']}!")
        # Chame a função ou exiba a tela relevante após o login bem-sucedido
    else:
        messagebox.showerror("Login", "CPF ou senha inválidos. Tente novamente.")

# Criar a janela principal
window = tk.Tk()
window.title("Sistema Bancário")
window.geometry("600x600")

# Criar os widgets da GUI
cpf_label = tk.Label(window, text="CPF:")
cpf_entry = tk.Entry(window)

senha_label = tk.Label(window, text="Senha:")
senha_entry = tk.Entry(window, show="*")

login_button = tk.Button(window, text="Login", command=login_button_click)

# Posicionar os widgets na janela
cpf_label.pack()
cpf_entry.pack()
senha_label.pack()
senha_entry.pack()
login_button.pack()

# Iniciar o loop de eventos da GUI
window.mainloop()
