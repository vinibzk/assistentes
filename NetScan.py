import nmap
import ipaddress
import socket
import os
from tabulate import tabulate
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

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
            else:
                result.append([ip_str, 'Offline', 'Desconhecido'])

    except Exception as e:
        result.append([str(e)])

    return result