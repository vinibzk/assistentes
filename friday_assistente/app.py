from flask import Flask, render_template, request, jsonify
import json
import random
from network_scanner import get_ip_range, scan_network

app = Flask(__name__)

# Carrega as respostas do assistente a partir do arquivo JSON
try:
    with open('responses.json', 'r', encoding='utf-8') as f:
        assistant_responses = json.load(f)
except FileNotFoundError:
    assistant_responses = {}
    print("Arquivo 'responses.json' não encontrado. Certifique-se de que ele está presente no diretório.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message', '').lower()
    user_ip = request.form.get('ip', '').strip()  # Obtém o IP do formulário
    
    default_ip = "192.168.1.1"  # IP padrão para a varredura de rede

    if not user_message:
        return jsonify({'assistant_message': "Mensagem não fornecida."})

    if user_message in ['varredura de rede', 'varrer rede']:
        if not user_ip:
            user_ip = default_ip  # Usa o IP padrão se não for fornecido

        try:
            ip_range = get_ip_range(user_ip)
            devices = scan_network(ip_range)
            response = {
                'assistant_message': "Aqui está o resultado da varredura de rede:",
                'devices': devices
            }
        except Exception as e:
            response = {
                'assistant_message': "Ocorreu um erro ao realizar a varredura de rede.",
                'error': str(e)
            }
    elif user_message in ['limpar chat', 'limpar tela']:
        response = {
            'assistant_message': "Chat limpo.",
            'clear_chat': True  # Adiciona um sinal para o frontend limpar o chat
        }
    else:
        response_list = assistant_responses.get(user_message, [
            "Desculpe, não entendi. Pode reformular?",
            "Não tenho uma resposta para isso. Pode tentar outra coisa?",
            "Poderia me dar mais detalhes?",
            "Estou aqui para ajudar com outras questões também.",
            "Não tenho uma resposta específica para isso no momento."
        ])
        response = {
            'assistant_message': random.choice(response_list)
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
