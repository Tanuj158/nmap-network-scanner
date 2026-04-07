import nmap

def scan_target(target):
    print(f"\n[+] Scanning Target: {target}\n")

    nm = nmap.PortScanner()

    try:
        nm.scan(hosts=target, arguments='-sS -T4')
    except Exception as e:
        print("Error:", e)
        return

    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")

            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]['name']
                state = nm[host][proto][port]['state']
                print(f"Port: {port} | State: {state} | Service: {service}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_target(target)