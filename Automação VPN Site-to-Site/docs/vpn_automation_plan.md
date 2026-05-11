# Plano de Automação VPN IPSec

## Objetivo

Automatizar a configuração de uma VPN IPSec site-to-site entre Fortigate e Palo Alto.

---

## Parâmetros da VPN

### Fortigate
- WAN IP: 192.168.1.100
- LAN: 192.168.10.0/24

### Palo Alto
- WAN IP: 192.168.1.150
- LAN: 192.168.20.0/24

### Tunnel Network
- 169.255.1.0/30

### IKE Phase1
- IKEv2
- DES-SHA1
- DH Group 14

### Phase2
- DES-SHA1
- PFS Group14

---

## Ferramentas/API

### Fortigate
- REST API
- SSH
- Netmiko

### Palo Alto
- XML API
- pan-os-python SDK
- SSH

---

## Passos da Automação

1. Validar conectividade entre peers
2. Criar objetos de rede
3. Criar Tunnel Interface
4. Configurar IKE Gateway
5. Configurar IPSec Tunnel
6. Criar rotas estáticas
7. Criar policies
8. Validar Phase1
9. Validar Phase2
10. Executar testes de conectividade

---

## Validação

### Fortigate
- diagnose vpn ike gateway list
- diagnose vpn tunnel list

### Palo Alto
- show vpn ike-sa
- show vpn ipsec-sa

---

## Alertas

O sistema deve alertar:
- Falha de autenticação
- Mismatch de proposal
- Peer inacessível
- Tunnel DOWN
- Erro de rota

---

## Desafios Encontrados

Durante os testes em laboratório foi identificada incompatibilidade criptográfica entre as imagens utilizadas.

O Fortigate suportava apenas DES, enquanto o Palo Alto suportava apenas 3DES/AES.