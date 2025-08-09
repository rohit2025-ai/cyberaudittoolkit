from modules.system_info import get_system_info

def main():
    info = get_system_info()
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

# main.py

from modules.network_scanner import scan_network

if __name__ == "__main__":
    devices = scan_network("192.168.1.0/24")
    for device in devices:
        print(f"IP: {device['IP']}, MAC: {device['MAC']}")