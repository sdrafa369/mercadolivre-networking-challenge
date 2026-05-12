# Automação de Configuração de Rede e VPN IPSec

Projeto desenvolvido para automação de configuração de dispositivos Fortigate e Palo Alto, utilizando Python e ferramentas de automação de rede.

---

# Parte 1

Automação de configuração de rede Cisco utilizando frontend web e backend Python.

## Funcionalidades

* Configuração de VLANs
* Alteração de hostname
* Backup de configuração
* Validação de configurações
* Frontend Web
* Backend Python

---

# Parte 2

Planejamento da automação de VPN IPSec Site-to-Site entre Fortigate e Palo Alto.

## Objetivos

* Definir parâmetros da VPN IPSec
* Planejar automação entre fabricantes diferentes
* Identificar APIs e ferramentas de integração
* Validar configuração do túnel
* Implementar estratégia de alertas e troubleshooting

---

# Tecnologias Utilizadas

* Python
* Flask
* Netmiko
* REST API
* pan-os-python
* FortiOS
* PAN-OS
* PNETLab

---

# Topologia

Fortigate <-----> Palo Alto

## Redes Utilizadas

| Equipamento | Rede LAN        | WAN           |
| ----------- | --------------- | ------------- |
| Fortigate   | 192.168.10.0/24 | 192.168.1.100 |
| Palo Alto   | 192.168.20.0/24 | 192.168.1.150 |

---

# Estrutura do Projeto

```text
backend/
frontend/
docs/
scripts/
README.md
```

---

# Limitações Encontradas

Durante os testes em laboratório foi identificada incompatibilidade entre os algoritmos criptográficos suportados pelas imagens utilizadas.

O Fortigate disponível suportava apenas algoritmos DES para IPSec, enquanto o Palo Alto suportava apenas 3DES/AES.

Apesar disso, toda a estrutura da VPN foi configurada e validada:

* Conectividade entre peers
* Tunnel Interfaces
* Virtual Router
* Zones
* Security Policies
* Rotas estáticas
* IKE Gateway
* IPSec Tunnel
* Proxy IDs

O troubleshooting realizado demonstrou o processo de diagnóstico e validação de interoperabilidade IPSec entre dispositivos de diferentes fabricantes.

Houve também diversas dificuldades com o laboratório devido ao pouco recurso que possuo de hardware.

* Pouca memória disponível no notebook (vide o print);
* Processador incapatível com algumas ferramentas.

---

# Scripts Incluídos

* deploy_fortigate.py
* deploy_paloalto.py
* test_connectivity.py

---

# Autor

Rafael Souza