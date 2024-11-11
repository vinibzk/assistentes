#!/usr/bin/env python3

import os
import time
from tabulate import tabulate
from colorama import init, Back, Fore, Style
from nmap import scan_network, get_ip_range
from whois import obter_informacoes_whois, obter_dominio_do_link, exibir_informacoes_whois

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def prompt_bot():
    print(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Digite um comando...")
    command = input(f"{Fore.GREEN}>>>{Style.RESET_ALL} ").strip()
    return command

def command_error(command):
    print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} O comando '{command}' não foi reconhecido.")
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")
    clear_screen()

def main():
    clear_screen()
    while True:
        command = prompt_bot()
        
        if command.lower() in ["sair", "fechar", "desligar", "exit", "off", "desligue", "durma", "sleep"]:
            break
        elif command.lower() in ["escanear rede", "escanear wifi", "varrer wifi", "varrer rede", "scan wifi"]:
            varrer_ip()
        elif command.lower() in ["escanear site", "escanear url", "varrer url", "varrer site"]:
            calc()
        else:
            command_error(command)

def varrer_ip():
    clear_screen()
    local_ip = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Insira o IP da rede local:\n{Fore.GREEN}>>>{Style.RESET_ALL} ").strip()
    ip_range = get_ip_range(local_ip)
    resultado = scan_network(ip_range)

    # Formata e exibe a tabela de IPs ativos com as cores
    ip_table = []
    for row in resultado:
        ip_str, status, hostname = row
        if status == 'Online':
            ip_table.append([Fore.CYAN + ip_str, Fore.GREEN + status, Fore.MAGENTA + hostname])
        else:
            ip_table.append([Fore.CYAN + ip_str, Fore.RED + status, Fore.MAGENTA + hostname])

    clear_screen()
    print(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Encontrei esses dispositivos: ")
    print()
    print(tabulate(ip_table, headers=[Fore.BLUE + "IP", Fore.BLUE + "STATUS", Fore.BLUE + "HOSTNAME"], tablefmt="grid"))
    print()
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

def consultar_whois():
    clear_screen()
    link = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Por favor, insira o link do site (exemplo: https://www.exemplo.com):\n{Fore.GREEN}>>>{Style.RESET_ALL} ").strip()
    dominio = obter_dominio_do_link(link)
    
    if dominio:
        informacoes = obter_informacoes_whois(dominio)
        if informacoes:
            exibir_informacoes_whois(informacoes)
        else:
            print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} Não foram encontradas informações para o domínio {dominio}.")
    else:
        print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} Não foi possível identificar o domínio a partir do link fornecido.")
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
