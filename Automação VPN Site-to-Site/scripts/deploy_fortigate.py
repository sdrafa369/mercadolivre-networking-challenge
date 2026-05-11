from netmiko import ConnectHandler

fortigate = {
    "device_type": "fortinet",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "admin"
}

commands = [
    "config vpn ipsec phase1-interface",
    "edit VPN-PALOALTO",
    "set interface port1",
    "set ike-version 2",
    "set peertype any",
    "set net-device enable",
    "set proposal des-sha1",
    "set dhgrp 14",
    "set remote-gw 192.168.1.150",
    "set psksecret SenhaVPN@2026",
    "next",
    "end",

    "config vpn ipsec phase2-interface",
    "edit VPN-PALOALTO-P2",
    "set phase1name VPN-PALOALTO",
    "set proposal des-sha1",
    "set dhgrp 14",
    "set src-subnet 192.168.10.0 255.255.255.0",
    "set dst-subnet 192.168.20.0 255.255.255.0",
    "next",
    "end",

    "config router static",
    "edit 1",
    "set dst 192.168.20.0 255.255.255.0",
    "set device VPN-PALOALTO",
    "next",
    "end"
]

connection = ConnectHandler(**fortigate)

output = connection.send_config_set(commands)
print(output)

connection.disconnect()