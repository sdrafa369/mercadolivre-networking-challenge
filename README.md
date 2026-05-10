# Mercado Livre - Networking Challenge

Projeto de automação de rede desenvolvido para o desafio técnico do Mercado Livre.

O projeto realiza automação de dispositivos Cisco utilizando Python, Netmiko e interface gráfica Tkinter, permitindo configuração automatizada de VLANs, alteração de hostname, backup e validação de configurações.

---

# Tecnologias Utilizadas

* Python 3
* Netmiko
* Tkinter
* Cisco IOS XE (CSR1000v)
* PNETLab
* Git/GitHub

---

# Funcionalidades

* Configuração automatizada de VLANs
* Alteração automática de hostname
* Salvamento de configuração na NVRAM
* Backup automático da running-config
* Validação de configuração
* Interface gráfica para operação

---

# Estrutura do Projeto

```text
mercadolivre-networking-challenge/
│
├── backend/
│   ├── switch_config.py
│   ├── backup.py
│   └── validation.py
│
├── frontend/
│   └── gui.py
│
├── backups/
├── screenshots/
├── README.md
└── requirements.txt
```

---

# VLANs Configuradas

| VLAN | Descrição      | Gateway      |
| ---- | -------------- | ------------ |
| 10   | VLAN_DADOS     | 192.168.10.1 |
| 20   | VLAN_VOZ       | 192.168.20.1 |
| 50   | VLAN_SEGURANCA | 192.168.50.1 |

---

# Topologia Utilizada

* Cisco CSR1000v no PNETLab
* Conexão SSH via Netmiko
* Automação executada através de interface gráfica Tkinter

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/sdrafa369/mercadolivre-networking-challenge.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Executando o Projeto

Execute a interface gráfica:

```bash
python -m frontend.gui
```

---

# Funcionalidades da Interface

A interface gráfica possui os seguintes botões:

* Configurar Switch
* Realizar Backup
* Validar Configuração

---

# Evidências

## Frontend

Adicionar screenshots da interface gráfica.

## Configuração Cisco

Adicionar screenshots dos comandos:

```cisco
show running-config
show ip interface brief
```

## Backup

Adicionar exemplo de arquivo salvo na pasta backups/.

## Validação

Adicionar screenshot mostrando a validação das configurações.

---

# Observações

O projeto foi desenvolvido utilizando ambiente virtualizado PNETLab com Cisco IOS XE CSR1000v para simulação de ambiente corporativo de rede.
