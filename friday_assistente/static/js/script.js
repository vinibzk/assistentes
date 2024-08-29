document.addEventListener('DOMContentLoaded', function() {
    const userInput = document.getElementById('user-input');
    const charCount = document.getElementById('char-count');
    const sendButton = document.getElementById('send-button');
    const maxChars = 100; // Definindo o limite de caracteres

    // Atualiza o contador de caracteres
    function updateCharCount() {
        const currentLength = userInput.value.length;
        charCount.textContent = `${currentLength}/${maxChars}`;
        // Adiciona uma classe para estilizar o contador se exceder o limite
        if (currentLength > maxChars) {
            charCount.style.color = '#ff0000'; // Alerta em vermelho se exceder o limite
        } else {
            charCount.style.color = '#00bcd4'; // Cor padrão
        }
    }

    // Adiciona um ouvinte de evento para cada alteração no input
    userInput.addEventListener('input', updateCharCount);

    // Adiciona um ouvinte de evento para enviar mensagem com Enter
    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });

    // Função para criar e adicionar mensagens ao chat
    function appendMessage(who, message) {
        const chatBox = document.getElementById('chat-box');
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${who}-message`);
        messageDiv.innerHTML = message; // Usa innerHTML para incluir HTML, como tabelas
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Rolagem para o fundo
    }

    // Função de envio da mensagem
    function sendMessage() {
        const message = userInput.value.trim();
        if (message.length > maxChars) {
            alert('Limite de caracteres excedido!');
            return;
        }
        if (message) {
            appendMessage('user', message);
            
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({
                    'message': message
                })
            })
            .then(response => response.json())
            .then(data => {
                // Adiciona a resposta do assistente
                appendMessage('assistant', data.assistant_message);

                if (data.clear_chat) {
                    // Limpa o chat se o backend enviar o sinal de limpeza
                    document.getElementById('chat-box').innerHTML = '';
                }

                if (data.devices) {
                    // Cria uma tabela HTML a partir dos dados dos dispositivos
                    let table = '<table border="1"><tr><th>IP</th><th>Status</th><th>Hostname</th></tr>';
                    data.devices.forEach(device => {
                        table += `<tr><td>${device[0]}</td><td>${device[1]}</td><td>${device[2]}</td></tr>`;
                    });
                    table += '</table>';
                    appendMessage('assistant', table);
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                appendMessage('assistant', 'Ocorreu um erro ao processar sua solicitação.');
            });

            userInput.value = ''; // Limpa o campo após o envio
            updateCharCount(); // Atualiza o contador de caracteres
        }
    }

    // Adiciona um ouvinte de evento para o botão de envio
    sendButton.addEventListener('click', sendMessage);

    // Animações do botão de envio e campo de entrada
    userInput.addEventListener('focus', function() {
        userInput.style.boxShadow = '0 0 10px rgba(0, 188, 212, 0.7)';
    });

    userInput.addEventListener('blur', function() {
        userInput.style.boxShadow = 'none';
    });

    // Inicializa o contador de caracteres
    updateCharCount();
});
