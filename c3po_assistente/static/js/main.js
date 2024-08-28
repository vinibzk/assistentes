function sendMessage() {
    const userInput = document.getElementById("user_input").value.trim();

    // Verifica se o campo de entrada não está vazio
    if (userInput === "") return;

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const messagesDiv = document.getElementById("messages");

        // Adiciona a mensagem do usuário
        messagesDiv.innerHTML += `<div class="message user"><strong>Você:</strong> ${userInput}</div>`;

        // Adiciona a resposta do assistente
        messagesDiv.innerHTML += `<div class="message bot"><strong>Assistente:</strong> ${data.response}</div>`;

        // Limpa o campo de entrada
        document.getElementById("user_input").value = '';

        // Rola a div de mensagens para o fim
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    });
}

// Adiciona evento de tecla ao input para enviar mensagem ao pressionar Enter
document.getElementById("user_input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
        event.preventDefault(); // Evita o comportamento padrão de enviar o formulário
    }
});

// Adiciona evento de clique ao botão para enviar a mensagem
document.getElementById("send-button").addEventListener("click", function() {
    sendMessage();
});
