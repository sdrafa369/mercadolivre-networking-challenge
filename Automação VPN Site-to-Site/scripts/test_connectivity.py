import subprocess

hosts = [
    "192.168.1.100",
    "192.168.1.150"
]

for host in hosts:
    print(f"Testando conectividade com {host}")

    response = subprocess.run(
        ["ping", "-c", "2", host],
        capture_output=True,
        text=True
    )

    print(response.stdout)