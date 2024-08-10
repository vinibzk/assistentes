#!/usr/bin/env python3

__author__ = 'Vinicius Mendes'
__version__ = '0.1.0'

import os
import time
import speech_recognition as sr
import pyttsx3
import wikipedia
import sympy as sp
from colorama import Fore, Style, init

init(autoreset=True)  # Faz o reset automático das cores e estilos após cada impressão.

recognizer = sr.Recognizer()  # Inicializa o reconhecedor de áudio.
engine = pyttsx3.init()  # Inicializa o motor de síntese de fala.

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_color(text, color=Fore.CYAN):
    print(f"{color}{text}{Style.RESET_ALL}")

def listen_command():
    try:
        with sr.Microphone() as source:
            print_with_color('Estou escutando...', Fore.GREEN)
            recognizer.adjust_for_ambient_noise(source)  # Ajusta para ruído de fundo.
            audio = recognizer.listen(source)  # Captura o áudio.
            command = recognizer.recognize_google(audio, language='pt-BR').lower()

            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
                print_with_color(f'Comando detectado: {command}', Fore.YELLOW)
                engine.say(command)
                engine.runAndWait()
                return command
    except sr.UnknownValueError:
        print_with_color('Não entendi o que você disse. Por favor, tente novamente.', Fore.RED)
    except sr.RequestError as e:
        print_with_color(f'Erro ao se conectar ao serviço de reconhecimento: {e}', Fore.RED)
    except Exception as e:
        print_with_color(f'Erro: {e}', Fore.RED)
    
    return None

def execute_command():
    command = listen_command()
    if command is None:
        return

    query = None

    if any(phrase in command for phrase in ['procure por', 'quem é', 'diga-me sobre', 'me fale sobre', 'o que é']):
        for phrase in ['procure por', 'quem é', 'diga-me sobre', 'me fale sobre', 'o que é']:
            if phrase in command:
                query = command.replace(phrase, '').strip()
                break
        if query:
            wikipedia.set_lang('pt')
            try:
                result = wikipedia.summary(query, sentences=2)
                print_with_color(f'Resultado: {result}', Fore.CYAN)
                engine.say(result)
                engine.runAndWait()
            except wikipedia.exceptions.DisambiguationError as e:
                print_with_color(f'Múltiplos resultados encontrados para "{query}": {e.options}', Fore.YELLOW)
            except wikipedia.exceptions.PageError:
                print_with_color(f'A página para "{query}" não foi encontrada.', Fore.RED)
            except Exception as e:
                print_with_color(f'Erro ao procurar por "{query}": {e}', Fore.RED)
    
    elif any(phrase in command for phrase in ['calcule', 'resolva', 'quanto é', 'faça a conta', 'qual é']):
        for phrase in ['calcule', 'resolva', 'quanto é', 'faça a conta', 'qual é']:
            if phrase in command:
                expression = command.replace(phrase, '').strip()
                perform_calculation(expression)
                break

    elif 'oi' in command:
        response = "Olá Vinícius, precisa de alguma coisa?"
        print_with_color(response, Fore.GREEN)
        engine.say(response)
        engine.runAndWait()

def perform_calculation(expression):
    try:
        result = sp.sympify(expression)
        response = f'A expressão matemática "{expression}" resulta no valor: {result}.'
        print_with_color(response, Fore.GREEN)
        engine.say(response)
        engine.runAndWait()
    except Exception as e:
        error_message = f'Houve um erro ao calcular a expressão: {e}'
        print_with_color(error_message, Fore.RED)
        engine.say(error_message)
        engine.runAndWait()

# Loop principal
if __name__ == "__main__":
    clear_screen()
    print_with_color('Iniciando o sistema de reconhecimento de voz...', Fore.MAGENTA)
    while True:
        execute_command()
        time.sleep(2)
        clear_screen()
        print_with_color('Pronto para o próximo comando...', Fore.GREEN)
