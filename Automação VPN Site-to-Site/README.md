# Automação de Configuração de Rede e VPN IPSec

Projeto desenvolvido para automação de configuração de dispositivos Fortigate e Palo Alto.

## Parte 1
- Configuração de VLANs
- Alteração de hostname
- Backup de configuração
- Frontend Web
- Backend Python

## Parte 2
Planejamento de automação de VPN IPSec entre Fortigate e Palo Alto.

## Tecnologias
- Python
- Flask
- Netmiko
- REST API
- FortiOS
- PAN-OS
- PNETLab

## Topologia

Fortigate <---> Palo Alto

## Limitações Encontradas

Durante os testes, foi identificada incompatibilidade entre os algoritmos criptográficos suportados pelas imagens utilizadas no laboratório.

O Fortigate disponível suportava apenas algoritmos DES, enquanto o Palo Alto suportava apenas 3DES/AES.

Apesar disso, toda a estrutura de VPN foi configurada e validada:
- Rotas
- Zones
- Policies
- Tunnel Interfaces
- IKE Gateway
- Proxy-ID
- Conectividade entre peers