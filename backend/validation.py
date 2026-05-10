from netmiko import ConnectHandler

def validar_configuracao():

    device = {
        "device_type": "cisco_ios",
        "host": "192.168.1.100",
        "username": "admin",
        "password": "admin123",
    }

    try:

        connection = ConnectHandler(**device)

        running_config = connection.send_command("show running-config")

        validations = {
            "Hostname": "hostname SWITCH_AUTOMATIZADO",
            "VLAN 10": "interface GigabitEthernet1.10",
            "VLAN 20": "interface GigabitEthernet1.20",
            "VLAN 50": "interface GigabitEthernet1.50",
        }

        result = ""

        for item, command in validations.items():

            if command in running_config:
                result += f"[OK] {item}\n"

            else:
                result += f"[ERRO] {item}\n"

        connection.disconnect()

        return result

    except Exception as e:
        return f"Erro: {e}"