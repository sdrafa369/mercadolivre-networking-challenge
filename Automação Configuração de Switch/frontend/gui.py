import tkinter as tk
from tkinter import messagebox

from backend.switch_config import configurar_switch
from backend.backup import realizar_backup
from backend.validation import validar_configuracao


def executar_config():

    resultado = configurar_switch(

        entry_hostname.get(),

        entry_vlan1_id.get(),
        entry_vlan1_nome.get(),
        entry_vlan1_ip.get(),

        entry_vlan2_id.get(),
        entry_vlan2_nome.get(),
        entry_vlan2_ip.get(),

        entry_vlan3_id.get(),
        entry_vlan3_nome.get(),
        entry_vlan3_ip.get(),
    )

    messagebox.showinfo("Configuração", resultado)


def executar_backup():

    resultado = realizar_backup()

    messagebox.showinfo("Backup", resultado)


def executar_validacao():

    resultado = validar_configuracao()

    messagebox.showinfo("Validação", resultado)


janela = tk.Tk()

janela.title("Mercado Livre - Network Automation")

janela.geometry("500x700")


titulo = tk.Label(
    janela,
    text="Automação de Rede Cisco",
    font=("Arial", 18)
)

titulo.pack(pady=10)


# HOSTNAME

tk.Label(janela, text="Hostname").pack()

entry_hostname = tk.Entry(janela, width=40)
entry_hostname.insert(0, "SWITCH_AUTOMATIZADO")
entry_hostname.pack(pady=5)


# VLAN 1

tk.Label(janela, text="VLAN 1 ID").pack()

entry_vlan1_id = tk.Entry(janela, width=40)
entry_vlan1_id.insert(0, "10")
entry_vlan1_id.pack()

tk.Label(janela, text="VLAN 1 Nome").pack()

entry_vlan1_nome = tk.Entry(janela, width=40)
entry_vlan1_nome.insert(0, "VLAN_DADOS")
entry_vlan1_nome.pack()

tk.Label(janela, text="VLAN 1 Gateway").pack()

entry_vlan1_ip = tk.Entry(janela, width=40)
entry_vlan1_ip.insert(0, "192.168.10.1")
entry_vlan1_ip.pack(pady=10)


# VLAN 2

tk.Label(janela, text="VLAN 2 ID").pack()

entry_vlan2_id = tk.Entry(janela, width=40)
entry_vlan2_id.insert(0, "20")
entry_vlan2_id.pack()

tk.Label(janela, text="VLAN 2 Nome").pack()

entry_vlan2_nome = tk.Entry(janela, width=40)
entry_vlan2_nome.insert(0, "VLAN_VOZ")
entry_vlan2_nome.pack()

tk.Label(janela, text="VLAN 2 Gateway").pack()

entry_vlan2_ip = tk.Entry(janela, width=40)
entry_vlan2_ip.insert(0, "192.168.20.1")
entry_vlan2_ip.pack(pady=10)


# VLAN 3

tk.Label(janela, text="VLAN 3 ID").pack()

entry_vlan3_id = tk.Entry(janela, width=40)
entry_vlan3_id.insert(0, "50")
entry_vlan3_id.pack()

tk.Label(janela, text="VLAN 3 Nome").pack()

entry_vlan3_nome = tk.Entry(janela, width=40)
entry_vlan3_nome.insert(0, "VLAN_SEGURANCA")
entry_vlan3_nome.pack()

tk.Label(janela, text="VLAN 3 Gateway").pack()

entry_vlan3_ip = tk.Entry(janela, width=40)
entry_vlan3_ip.insert(0, "192.168.50.1")
entry_vlan3_ip.pack(pady=10)


# BOTÕES

btn_config = tk.Button(
    janela,
    text="Configurar Switch",
    width=30,
    command=executar_config
)

btn_config.pack(pady=10)


btn_backup = tk.Button(
    janela,
    text="Realizar Backup",
    width=30,
    command=executar_backup
)

btn_backup.pack(pady=10)


btn_validacao = tk.Button(
    janela,
    text="Validar Configuração",
    width=30,
    command=executar_validacao
)

btn_validacao.pack(pady=10)


janela.mainloop()