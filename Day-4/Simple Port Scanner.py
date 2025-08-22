import socket

def scan_ports(target, ports):
    print(f"\n Scanning {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Fast scan
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except socket.error:
            print(f" Couldn't connect to {target}")
            break

if __name__ == "__main__":
    target_ip = input("Enter target IP or domain: ")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 8080]  # Common ports
    scan_ports(target_ip, ports_to_scan)
