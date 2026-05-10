from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "admin123",
}

try:
    connection = ConnectHandler(**device)

    print("Conectado com sucesso!\n")

    output = connection.send_command("show ip interface brief")

    print(output)

    connection.disconnect()

except Exception as e:
    print(f"Erro: {e}")