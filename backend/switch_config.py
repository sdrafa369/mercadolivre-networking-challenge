from netmiko import ConnectHandler

def configurar_switch():

    device = {
        "device_type": "cisco_ios",
        "host": "192.168.1.100",
        "username": "admin",
        "password": "admin123",
        "fast_cli": False,
         "session_log": "netmiko.log",
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
        "wr",
    ]

    try:

        connection = ConnectHandler(**device)

        output = connection.send_config_set(commands)

        connection.send_config_set(
            ["hostname SWITCH_AUTOMATIZADO"]
        )

        connection.save_config()

        connection.disconnect()

        return "Configuração aplicada com sucesso!"

    except Exception as e:
        return f"Erro: {e}"