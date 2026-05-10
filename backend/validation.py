from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "admin123",
}

try:
    connection = ConnectHandler(**device)

    print("=" * 50)
    print("VALIDANDO CONFIGURAÇÕES...")
    print("=" * 50)

    running_config = connection.send_command("show running-config")

    validations = {
        "Hostname": "hostname SWITCH_AUTOMATIZADO",
        "VLAN 10": "interface GigabitEthernet1.10",
        "VLAN 20": "interface GigabitEthernet1.20",
        "VLAN 50": "interface GigabitEthernet1.50",
    }

    for item, command in validations.items():

        if command in running_config:
            print(f"[OK] {item} configurado corretamente.")

        else:
            print(f"[ERRO] {item} NÃO encontrado.")

    connection.disconnect()

except Exception as e:
    print(f"Erro: {e}")