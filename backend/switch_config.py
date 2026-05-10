from netmiko import ConnectHandler


def configurar_switch(
    hostname,

    vlan1_id,
    vlan1_nome,
    vlan1_ip,

    vlan2_id,
    vlan2_nome,
    vlan2_ip,

    vlan3_id,
    vlan3_nome,
    vlan3_ip,
):

    device = {
        "device_type": "cisco_ios",
        "host": "192.168.1.100",
        "username": "admin",
        "password": "admin123",
        "fast_cli": False,
        "session_log": "netmiko.log",
    }

    commands = [

        f"interface GigabitEthernet1.{vlan1_id}",
        f"encapsulation dot1Q {vlan1_id}",
        f"ip address {vlan1_ip} 255.255.255.0",
        f"description {vlan1_nome}",
        "no shutdown",

        f"interface GigabitEthernet1.{vlan2_id}",
        f"encapsulation dot1Q {vlan2_id}",
        f"ip address {vlan2_ip} 255.255.255.0",
        f"description {vlan2_nome}",
        "no shutdown",

        f"interface GigabitEthernet1.{vlan3_id}",
        f"encapsulation dot1Q {vlan3_id}",
        f"ip address {vlan3_ip} 255.255.255.0",
        f"description {vlan3_nome}",
        "no shutdown",
    ]

    try:

        connection = ConnectHandler(**device)

        output = connection.send_config_set(commands)

        print(output)

        connection.send_config_set(
            [f"hostname {hostname}"]
        )

        connection.save_config()

        connection.disconnect()

        return "Configuração aplicada com sucesso!"

    except Exception as e:
        return f"Erro: {e}"