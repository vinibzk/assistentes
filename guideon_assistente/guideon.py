#!/usr/bin/env python3

__author__ = "Vinicius Mendes"
__version__ = "0.0.1"

import os
import time
from colorama import init, Fore, Style
from tabulate import tabulate
from NetScan import scan_network, get_ip_range  # Importa as funções de NetScan.py
from site_utils import obter_informacoes_whois, obter_dominio_do_link, exibir_informacoes_whois  # Importa funções de site_utils.py

# Inicializa o colorama para suportar cores no terminal
init(autoreset=True)

def clear_screen():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def header():
    clear_screen()
    nome = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Como você gostaria de ser chamado?\n{Fore.GREEN}>>>{Style.RESET_ALL} ")
    print()
    clear_screen()
    print(f"{Fore.BLUE}[ GUIDEON ] {Style.RESET_ALL} Ótima escolha, {Fore.YELLOW}{nome}{Style.RESET_ALL}!")
    time.sleep(3)
    perguntar(nome)

def perguntar(nome):
    while True:
        clear_screen()
        resposta = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Como posso ajudar?\n{Fore.GREEN}>>>{Style.RESET_ALL} ")
        print()
        if resposta.lower() == 'sair':
            clear_screen()
            print(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Até logo!")
            break
        elif "calcule" in resposta.lower() or "cálculo" in resposta.lower() or "calc" in resposta.lower() or "faça um cálculo" in resposta.lower():
            executar_calculo()
        elif "varrer ip" in resposta.lower() or "scan ip" in resposta.lower() or "listar ips" in resposta.lower():
            varrer_ip()
        elif "whois" in resposta.lower() or "informações whois" in resposta.lower():
            consultar_whois()
        else:
            clear_screen()
            print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} Desculpe, não tenho informações sobre:\n'{resposta}'.")
            input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

def executar_calculo():
    clear_screen()
    expressao = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Qual é a expressão matemática?\n{Fore.GREEN}>>>{Style.RESET_ALL} ")
    try:
        clear_screen()
        resultado = eval(expressao)
        print(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} {expressao} = {Fore.YELLOW}{resultado}{Style.RESET_ALL}.")
        print()
    except Exception as e:
        print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} Houve um erro ao calcular a expressão:\n{e}")
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

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
    print(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Encontrei esses Dispositivos: ")
    print()
    print(tabulate(ip_table, headers=[Fore.BLUE + "IP", Fore.BLUE + "STATUS", Fore.BLUE + "HOSTNAME"], tablefmt="grid"))
    print()
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

def consultar_whois():
    clear_screen()
    link = input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Por favor, insira o link do site (exemplo: https://www.exemplo.com):\n{Fore.GREEN}>>>{Style.RESET_ALL} ")
    dominio = obter_dominio_do_link(link)
    
    if dominio:
        informacoes = obter_informacoes_whois(dominio)
        if informacoes:
            exibir_informacoes_whois(informacoes)
        else:
            print(f"{Fore.RED}[ GUIDEON ]{Style.RESET_ALL} Não foram encontradas informações para o domínio {dominio}.")
    input(f"{Fore.BLUE}[ GUIDEON ]{Style.RESET_ALL} Pressione Enter para continuar...")

header()
