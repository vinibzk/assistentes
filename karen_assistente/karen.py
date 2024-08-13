import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import os
import platform
from colorama import init, Fore, Style
from scan_ip import varrer_ip  # Importa a função de varredura de IPs
import re  # Importa o módulo para expressões regulares

# Inicializa o colorama
init(autoreset=True)

def listar_vozes():
    """Lista todas as vozes disponíveis e permite a seleção."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    print(Fore.CYAN + "\nLista de vozes disponíveis:")
    for indice, voz in enumerate(voices):
        print(Fore.YELLOW + f"{indice}: {voz.name} ({voz.languages})")

    escolha = int(input(Fore.GREEN + "Escolha o número da voz (ou -1 para padrão): "))
    if escolha == -1:
        voz_id = voices[0].id  # Seleciona a voz padrão
    else:
        voz_id = voices[escolha].id

    return voz_id

def falar(texto, voz_id, rate=180):
    """Fala o texto usando o pyttsx3 com a voz selecionada e a velocidade especificada."""
    engine = pyttsx3.init()
    engine.setProperty('voice', voz_id)
    engine.setProperty('rate', rate)  # Ajuste a velocidade aqui
    engine.say(texto)
    engine.runAndWait()

def obter_hora_atual():
    """Retorna a hora atual no formato HH:MM."""
    agora = datetime.now()
    return agora.strftime("%H:%M")

def obter_data_atual():
    """Retorna a data atual no formato DD/MM/AAAA."""
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y")

def saudacao():
    """Retorna uma saudação baseada na hora do dia."""
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def abrir_site(url):
    """Abre a URL fornecida no navegador padrão."""
    # Verifica se a URL começa com http:// ou https://, caso contrário adiciona http://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    # Adiciona um domínio padrão se a URL não tiver um
    if not re.search(r'\.\w+$', url):
        url += ".com"
    webbrowser.open(url)

def limpar_tela():
    """Limpa a tela do terminal de forma segura."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def listar_comandos():
    """Retorna uma lista dos comandos e suas alternativas."""
    comandos = {
        "desligar": ["desligar", "encerrar", "parar", "terminar"],
        "hora": ["que horas são", "me diga a hora", "hora atual", "qual é a hora", "qual a hora"],
        "data": ["qual é a data", "que dia é hoje", "data de hoje", "qual a data de hoje", "qual é a data atual"],
        "nome": ["qual é o meu nome", "meu nome é", "diga meu nome", "meu nome é agora"],
        "saudacao": ["saudação", "bom dia", "boa tarde", "boa noite"],
        "mudar_nome": ["mudar nome", "alterar nome", "trocar nome"],
        "abrir_site": ["abrir site"],
        "varrer_rede": ["varrer rede"],
        "comandos": ["quais são os comandos", "mostrar comandos", "listar comandos", "ajuda", "comandos disponíveis"]
    }

    lista_comandos = []
    for comando, alternativas in comandos.items():
        lista_comandos.append(f"{Fore.CYAN + comando.capitalize()}: {', '.join(alternativas)}")

    return "\n".join(lista_comandos)

def pausar_ate_comando(mensagem, voz_id, palavras_chave):
    """Pausa até receber um comando de voz específico."""
    falar(mensagem, voz_id)
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            try:
                audio = r.listen(fonte)
                comando = r.recognize_google(audio, language="pt-BR").lower()
                if any(palavra in comando for palavra in palavras_chave):
                    break
                else:
                    falar("Desculpe, não entendi. Diga 'fechar varredura de rede' para continuar.", voz_id)
            except sr.UnknownValueError:
                falar("Desculpe, não entendi o que você disse. Tente novamente.", voz_id)
            except sr.RequestError as e:
                falar(f"Erro de solicitação; verifique sua conexão com a internet. Erro: {e}", voz_id)

def main():
    voz_id = listar_vozes()
    nome_usuario = None

    falar(f"{saudacao()} Bem-vindo ao assistente pessoal. Como posso ajudar?", voz_id)

    while True:
        limpar_tela()
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            print(Fore.GREEN + "Fale algo (ou diga 'desligar')")
            try:
                audio = r.listen(fonte)
                comando = r.recognize_google(audio, language="pt-BR")
                print(Fore.YELLOW + "Você disse:", comando)
            except sr.UnknownValueError:
                print(Fore.RED + "Desculpe, não entendi o que você disse.")
                falar("Desculpe, não entendi o que você disse.", voz_id)
                continue
            except sr.RequestError as e:
                print(Fore.RED + f"Erro de solicitação; verifique sua conexão com a internet. Erro: {e}")
                falar("Erro de solicitação; verifique sua conexão com a internet.", voz_id)
                continue

        comando = comando.lower()

        if any(phrase in comando for phrase in ["desligar", "encerrar", "parar", "terminar"]):
            falar("Encerrando assistente.", voz_id)
            break

        elif any(phrase in comando for phrase in ["que horas são", "me diga a hora", "hora atual", "qual é a hora", "qual a hora"]):
            hora_atual = obter_hora_atual()
            falar(f"São {hora_atual}.", voz_id)
            print(Fore.CYAN + f"São {hora_atual}.")

        elif any(phrase in comando for phrase in ["qual é a data", "que dia é hoje", "data de hoje", "qual a data de hoje", "qual é a data atual"]):
            data_atual = obter_data_atual()
            falar(f"A data de hoje é {data_atual}.", voz_id)
            print(Fore.CYAN + f"A data de hoje é {data_atual}.")

        elif "qual é o meu nome" in comando:
            if nome_usuario:
                falar(f"Seu nome é {nome_usuario}.", voz_id)
                print(Fore.CYAN + f"Seu nome é {nome_usuario}.")
            else:
                falar("Você ainda não definiu um nome. Por favor, diga qual é o seu nome.", voz_id)
                with mic as fonte:
                    r.adjust_for_ambient_noise(fonte)
                    try:
                        audio = r.listen(fonte)
                        nome_usuario = r.recognize_google(audio, language="pt-BR")
                        falar(f"Nome definido como {nome_usuario}.", voz_id)
                        print(Fore.CYAN + f"Nome definido como {nome_usuario}.")
                    except sr.UnknownValueError:
                        print(Fore.RED + "Não consegui entender o nome. Tente novamente.")
                        falar("Não consegui entender o nome. Tente novamente.", voz_id)
                    except sr.RequestError as e:
                        print(Fore.RED + f"Erro de solicitação; verifique sua conexão com a internet. Erro: {e}")
                        falar("Erro de solicitação; verifique sua conexão com a internet.", voz_id)

        elif "meu nome é" in comando:
            _, nome = comando.split("meu nome é", 1)
            nome_usuario = nome.strip()
            falar(f"Nome definido como {nome_usuario}.", voz_id)
            print(Fore.CYAN + f"Nome definido como {nome_usuario}.")

        elif "saudação" in comando:
            saudacao_atual = saudacao()
            falar(saudacao_atual, voz_id)
            print(Fore.CYAN + saudacao_atual)

        elif "mudar nome" in comando:
            falar("Por favor, diga o novo nome.", voz_id)
            with mic as fonte:
                r.adjust_for_ambient_noise(fonte)
                try:
                    audio = r.listen(fonte)
                    novo_nome = r.recognize_google(audio, language="pt-BR")
                    nome_usuario = novo_nome.strip()
                    falar(f"Nome alterado para {nome_usuario}.", voz_id)
                    print(Fore.CYAN + f"Nome alterado para {nome_usuario}.")
                except sr.UnknownValueError:
                    print(Fore.RED + "Não consegui entender o novo nome. Tente novamente.")
                    falar("Não consegui entender o novo nome. Tente novamente.", voz_id)
                except sr.RequestError as e:
                    print(Fore.RED + f"Erro de solicitação; verifique sua conexão com a internet. Erro: {e}")
                    falar("Erro de solicitação; verifique sua conexão com a internet.", voz_id)

        elif "abrir site" in comando:
            falar("Por favor, diga o nome do site.", voz_id)
            with mic as fonte:
                r.adjust_for_ambient_noise(fonte)
                try:
                    audio = r.listen(fonte)
                    site = r.recognize_google(audio, language="pt-BR")
                    abrir_site(site)
                    falar(f"Abrindo {site}.", voz_id)
                    print(Fore.CYAN + f"Abrindo {site}.")
                except sr.UnknownValueError:
                    print(Fore.RED + "Não consegui entender o nome do site. Tente novamente.")
                    falar("Não consegui entender o nome do site. Tente novamente.", voz_id)
                except sr.RequestError as e:
                    print(Fore.RED + f"Erro de solicitação; verifique sua conexão com a internet. Erro: {e}")
                    falar("Erro de solicitação; verifique sua conexão com a internet.", voz_id)

        elif "varrer rede" in comando:
            falar("Iniciando a varredura de rede. Diga 'fechar varredura de rede' para parar e voltar ao menu.", voz_id)
            resultados = varrer_ip("192.168.1.254")  # Aqui é possível ajustar o IP de destino se necessário
            print(Fore.GREEN + "\nResultados da varredura de rede:")
            for resultado in resultados:
                print(Fore.YELLOW + resultado)
            pausar_ate_comando("Os resultados foram exibidos. Diga 'fechar varredura de rede' para voltar ao menu principal.", voz_id, ["fechar varredura de rede"])

        elif "comandos" in comando or "listar comandos" in comando or "mostrar comandos" in comando or "quais são os comandos" in comando or "ajuda" in comando:
            comandos = listar_comandos()
            falar("Aqui está a lista de comandos disponíveis.", voz_id)
            print(Fore.CYAN + comandos)
            pausar_ate_comando("Aqui estão todos os comandos. Diga 'fechar comandos' para voltar ao menu principal.", voz_id, ["fechar comandos"])

        else:
            falar("Comando não reconhecido. Tente novamente ou diga 'comandos' para obter uma lista dos comandos disponíveis.", voz_id)

if __name__ == '__main__':
    main()
