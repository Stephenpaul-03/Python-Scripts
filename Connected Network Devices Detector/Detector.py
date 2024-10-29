import socket
import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_network():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    ip_network = ipaddress.IPv4Network(f"{local_ip}/24", strict=False)
    return ip_network

def ping_device(ip):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '500', str(ip)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(str(ip))[0]
            except socket.herror:
                hostname = "Unknown"
            return (hostname, str(ip))
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
    return None

def get_devices(network):
    devices = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping_device, ip): ip for ip in network.hosts()}
        for future in as_completed(futures):
            result = future.result()
            if result:
                devices.append(result)
                print(f"Found device: {result[0]} - {result[1]}")
    return devices

def save(devices, filename="devices.txt"):
    with open(filename, "w") as file:
        for hostname, ip in devices:
            file.write(f"{hostname} - {ip}\n")

network = get_network()
devices = get_devices(network)
save(devices)

print("Devices saved to devices.txt")
