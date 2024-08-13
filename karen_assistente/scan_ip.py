import nmap
import ipaddress
import socket
from tabulate import tabulate
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def get_ip_range(local_ip):
    """Calcula o intervalo de IP com base no IP local fornecido."""
    ip = ipaddress.ip_address(local_ip)
    network = ipaddress.ip_network(ipaddress.ip_interface(f"{local_ip}/24").network, strict=False)
    return network

def get_hostname(ip):
    """Tenta resolver o hostname a partir do IP usando socket."""
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except (socket.herror, socket.gaierror):
        return 'Desconhecido'

def scan_network(ip_range):
    """Realiza a varredura da rede e retorna os resultados em uma lista de tabelas."""
    nm = nmap.PortScanner()
    result = []
    online_devices = []

    try:
        # Varredura de ping para verificar se os IPs estão ativos
        nm.scan(hosts=str(ip_range), arguments='-sn')  # -sn significa "Ping Scan" (sem varredura de portas)

        active_ips = nm.all_hosts()
        # Dados para a tabela de IPs ativos
        for ip in ip_range.hosts():
            ip_str = str(ip)
            if ip_str in active_ips:
                # Resolução de nome do host
                hostname = get_hostname(ip_str)
                result.append([ip_str, 'Online', hostname])
                online_devices.append((ip_str, hostname))  # Armazena IP e hostname de dispositivos online
            else:
                result.append([ip_str, 'Offline', 'Desconhecido'])

    except Exception as e:
        result.append([str(e)])

    return result, online_devices  # Retorna também a lista de dispositivos online

def varrer_ip(default_ip="192.168.1.254"):
    """Realiza a varredura da rede no IP fornecido e retorna dispositivos online."""
    ip_range = get_ip_range(default_ip)
    resultado, dispositivos_online = scan_network(ip_range)

    # Formata e exibe a tabela de IPs ativos com as cores
    ip_table = []
    for row in resultado:
        ip_str, status, hostname = row
        if status == 'Online':
            ip_table.append([Fore.CYAN + ip_str + Style.RESET_ALL, Fore.GREEN + status + Style.RESET_ALL, Fore.MAGENTA + hostname + Style.RESET_ALL])
        else:
            ip_table.append([Fore.CYAN + ip_str + Style.RESET_ALL, Fore.RED + status + Style.RESET_ALL, Fore.MAGENTA + hostname + Style.RESET_ALL])

    print(Fore.CYAN + "Dispositivos encontrados na rede 192.168.1.254:" + Style.RESET_ALL)
    print()
    print(tabulate(ip_table, headers=["IP", "STATUS", "HOSTNAME"], tablefmt="grid"))
    print()

    return dispositivos_online  # Retorna a lista de dispositivos online
