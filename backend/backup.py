from netmiko import ConnectHandler
from datetime import datetime

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.100",
    "username": "admin",
    "password": "admin123",
}

try:
    connection = ConnectHandler(**device)

    print("Conectado ao dispositivo!\n")

    running_config = connection.send_command("show running-config")

    hostname = connection.find_prompt().replace("#", "")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"backups/{hostname}_{timestamp}.txt"

    with open(filename, "w") as backup_file:
        backup_file.write(running_config)

    print("=" * 50)
    print("BACKUP REALIZADO COM SUCESSO")
    print("=" * 50)

    print(f"Arquivo salvo em: {filename}")

    connection.disconnect()

except Exception as e:
    print(f"Erro: {e}")