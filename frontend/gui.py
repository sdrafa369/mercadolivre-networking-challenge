import tkinter as tk
from tkinter import messagebox

from backend.switch_config import configurar_switch
from backend.backup import realizar_backup
from backend.validation import validar_configuracao


def executar_config():

    resultado = configurar_switch()

    messagebox.showinfo("Configuração", resultado)


def executar_backup():

    resultado = realizar_backup()

    messagebox.showinfo("Backup", resultado)


def executar_validacao():

    resultado = validar_configuracao()

    messagebox.showinfo("Validação", resultado)


janela = tk.Tk()

janela.title("Mercado Livre - Network Automation")

janela.geometry("400x300")


titulo = tk.Label(
    janela,
    text="Automação de Rede",
    font=("Arial", 18)
)

titulo.pack(pady=20)


btn_config = tk.Button(
    janela,
    text="Configurar Switch",
    width=25,
    command=executar_config
)

btn_config.pack(pady=10)


btn_backup = tk.Button(
    janela,
    text="Realizar Backup",
    width=25,
    command=executar_backup
)

btn_backup.pack(pady=10)


btn_validacao = tk.Button(
    janela,
    text="Validar Configuração",
    width=25,
    command=executar_validacao
)

btn_validacao.pack(pady=10)


janela.mainloop()