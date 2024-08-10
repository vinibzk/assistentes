import whois
import tldextract
import datetime

def formatar_data(data):
    """Formata a data para uma representação mais legível."""
    if isinstance(data, list):
        return ', '.join([d.strftime("%d-%m-%Y") if isinstance(d, datetime.datetime) else 'N/A' for d in data])
    elif isinstance(data, datetime.datetime):
        return data.strftime("%d-%m-%Y")
    return 'N/A'

def exibir_informacoes(informacoes):
    """Exibe todas as informações WHOIS disponíveis de forma organizada."""
    print("\nInformações WHOIS para o domínio:")
    for campo, valor in informacoes.items():
        if isinstance(valor, list):
            valor = ', '.join(str(v) for v in valor)
        print(f"{campo.replace('_', ' ').title()}: {valor if valor else 'N/A'}")

def obter_informacoes_whois(dominio):
    try:
        # Fazendo a consulta WHOIS para o domínio
        informacoes = whois.whois(dominio)
        
        # Exibindo todas as informações disponíveis
        exibir_informacoes(informacoes)
    except whois.parser.PywhoisError:
        print(f"Não foi possível obter informações WHOIS para o domínio '{dominio}'. O domínio pode não existir ou estar restrito.")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o domínio {dominio}: {e}")

def obter_dominio_do_link(link):
    # Extrai o domínio de um link completo
    ext = tldextract.extract(link)
    if ext.domain and ext.suffix:
        dominio = f"{ext.domain}.{ext.suffix}"
        return dominio
    else:
        print("O link fornecido não contém um domínio válido.")
        return None

def main():
    # Solicitar ao usuário para inserir o link do site
    link = input("Por favor, insira o link do site (exemplo: https://www.exemplo.com): ")
    
    # Extrair o domínio do link fornecido
    dominio = obter_dominio_do_link(link)
    
    # Se um domínio válido foi extraído, obter e exibir informações WHOIS
    if dominio:
        obter_informacoes_whois(dominio)

if __name__ == "__main__":
    main()
