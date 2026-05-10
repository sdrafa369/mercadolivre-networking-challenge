from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "admin123",
}

commands = [

    "interface GigabitEthernet1.10",
    "encapsulation dot1Q 10",
    "ip address 192.168.10.1 255.255.255.0",
    "description VLAN_DADOS",
    "no shutdown",

    "interface GigabitEthernet1.20",
    "encapsulation dot1Q 20",
    "ip address 192.168.20.1 255.255.255.0",
    "description VLAN_VOZ",
    "no shutdown",

    "interface GigabitEthernet1.50",
    "encapsulation dot1Q 50",
    "ip address 192.168.50.1 255.255.255.0",
    "description VLAN_SEGURANCA",
    "no shutdown",
]

try:
    connection = ConnectHandler(**device)

    print("Conectado com sucesso!\n")

    print("=" * 50)
    print("CONFIGURANDO DISPOSITIVO...")
    print("=" * 50)

    output = connection.send_config_set(commands)

    print(output)

    hostname_output = connection.send_config_set(
        ["hostname SWITCH_AUTOMATIZADO"]
    )

    print(hostname_output)

    connection.save_config()

    print("\nConfiguração salva com sucesso!")

    connection.disconnect()

except Exception as e:
    print(f"Erro: {e}")