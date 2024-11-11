import whois
import datetime
import tldextract
from colorama import init, Back, Fore, Style
from tabulate import tabulate

init(autoreset=True)

def formatar_data(data):
    #Formata a data para uma representação mais legível."""
    if isinstance(data, list):
        return ', '.join([d.strftime("%d-%m-%Y") if isinstance(d, datetime.datetime) else 'N/A' for d in data])
    elif isinstance(data, datetime.datetime):
        return data.strftime("%d-%m-%Y")
    return 'N/A'

def exibir_informacoes_whois(informacoes):
    # Exibe todas as informações WHOIS disponíveis de forma organizada e colorida.
    print(f"\n{Fore.BLUE}Informações WHOIS para o domínio:{Fore.RESET}")
    info_table = []
    for campo, valor in informacoes.items():
        if isinstance(valor, list):
            valor = ', '.join(str(v) for v in valor)
        info_table.append([campo.replace('_', ' ').title(), valor if valor else 'N/A'])

    # Imprime a tabela com informações WHOIS
    print(tabulate(info_table, headers=[Fore.BLUE + "Campo", Fore.BLUE + "Valor"], tablefmt="grid"))

def obter_informacoes_whois(dominio):
    try:
        # Fazendo a consulta WHOIS para o domínio
        informacoes = whois.whois(dominio)
        return informacoes
    except whois.parser.PywhoisError:
        print(f"{Fore.RED}Não foi possível obter informações WHOIS para o domínio '{dominio}'. O domínio pode não existir ou estar restrito.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Ocorreu um erro ao consultar o domínio {dominio}: {e}{Fore.RESET}")
    return None

def obter_dominio_do_link(link):
    # Extrai o domínio de um link completo.
    ext = tldextract.extract(link)
    if ext.domain and ext.suffix:
        dominio = f"{ext.domain}.{ext.suffix}"
        return dominio
    else:
        print(f"{Fore.RED}O link fornecido não contém um domínio válido.{Fore.RESET}")
        return None
