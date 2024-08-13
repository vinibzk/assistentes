# 🤖 Assistente Guideon

**Guideon** é um assistente virtual desenvolvido em Python, projetado para oferecer uma variedade de funcionalidades úteis através de um terminal interativo. Com Guideon, você pode realizar cálculos matemáticos, varrer redes para identificar dispositivos ativos e consultar informações WHOIS sobre domínios.

## Visão Geral

Guideon combina uma interface interativa e colorida com diversas funcionalidades práticas, tornando o uso de comandos do terminal mais eficiente e intuitivo.

## ⚙️ Funcionalidades

- **Cálculos Matemáticos**: Permite ao usuário inserir expressões matemáticas e obter o resultado diretamente no terminal.
- **Varredura de IPs**: Identifica dispositivos ativos na rede local, apresentando uma lista com status e hostname.
- **Consulta WHOIS**: Fornece informações WHOIS sobre um domínio, incluindo dados de registro e detalhes de contato.

## 📕 Requisitos

Para executar o Guideon, você precisará dos seguintes componentes:

- **Python 3**: Certifique-se de ter o Python 3 instalado no seu sistema.
- **Bibliotecas Python**: Instale as dependências necessárias usando `pip`:

 ```bash
  pip install colorama
  pip install tabulate
  pip install python-nmap
  pip install whois
  pip install tldextract
  ```
### 1. Clonar o Repositório
Clone o repositório do Guideon para o seu ambiente local:
```bash
   git clone https://github.com/vinibzk/assistentes
```
### 2. Executar o Código
Inicie o Guideon executando o script Python:
```bash
   python guideon.py
```
### 3. Interagir com o Assistente
Após iniciar o Guideon, você poderá usar as seguintes funcionalidades:

**Calcular Expressões:** Digite uma expressão matemática quando solicitado.
Exemplo: `2 * 2 = 4`.

**Varrer IPs:** Forneça o IP da rede local para listar dispositivos ativos. Exemplo: `192.168.1.254`.

**Consultar WHOIS:** Insira um link para obter informações WHOIS sobre o domínio.
Exemplo: `https://www.example.com`.

# Estrutura do Código
O projeto é composto pelos seguintes arquivos principais:

`guideon.py`: O script principal que contém a lógica do assistente Guideon.
`NetScan.py`: Módulo responsável por escanear a rede local e obter o intervalo de IPs para varredura.
`site_utils.py`: Contém funções auxiliares para obter informações WHOIS e extrair o domínio de um link.

# 📘 Exemplos
Aqui estão alguns exemplos de uso do Guideon:
### 🧮 Cálculo Matemático
```scss
[ GUIDEON ] Qual é a expressão matemática?
>>> 5 * (3 + 2)
[ GUIDEON ] 5 * (3 + 2) = 25.
```
### 🛜 Varredura de IPs
```lua
[ GUIDEON ] Insira o IP da rede local:
>>> 192.168.1.254
[ GUIDEON ] Encontrei esses Dispositivos:
+----------------+---------+----------------+
| IP             | STATUS  | HOSTNAME       |
+----------------+---------+----------------+
| 192.168.1.2    | Online  | device1.local  |
| 192.168.1.3    | Offline |                |
+----------------+---------+----------------+
```
### 🌐 Consulta WHOIS
```yaml
[ GUIDEON ] Por favor, insira o link do site:
>>> https://www.example.com
[ GUIDEON ] Informações WHOIS para example.com:
Registrar: Example Registrar
Data de Criação: 2020-01-01
```

# 🤖 Assistente Jarvis

**Jarvis** é um assistente virtual desenvolvido em Python, projetado para oferecer uma variedade de funcionalidades através de um terminal interativo. Com Jarvis, você pode realizar cálculos matemáticos, buscar informações na Wikipedia e interagir com o assistente por comandos de voz.

## Visão Geral

Jarvis combina uma interface interativa e colorida com diversas funcionalidades práticas, tornando o uso de comandos de voz e do terminal mais eficiente e intuitivo.

## ⚙️ Funcionalidades

- **Cálculos Matemáticos**: Permite ao usuário inserir expressões matemáticas e obter o resultado diretamente no terminal.
- **Busca na Wikipedia**: Realiza buscas e fornece resumos sobre temas encontrados na Wikipedia.
- **Interação por Voz**: Permite ao usuário interagir com o assistente usando comandos de voz.

## 📕 Requisitos

Para executar o Jarvis, você precisará dos seguintes componentes:

- **Python 3**: Certifique-se de ter o Python 3 instalado no seu sistema.
- **Bibliotecas Python**: Instale as dependências necessárias usando `pip`:
  ```bash
  pip install SpeechRecognition
  pip install pyttsx3
  pip install wikipedia
  pip install sympy
  pip install colorama
  ```
### 1. Clonar o Repositório
Clone o repositório do Jarvis para o seu ambiente local:
```bash
git clone https://github.com/vinibzk/assistentes
```
### 2. Executar o Código
Inicie o Jarvis executando o script Python:

```bash
python jarvis.py
```
### 3. Interagir com o Assistente
Após iniciar o Jarvis, você poderá usar as seguintes funcionalidades:

- **Calcular Expressões**: Diga um comando para calcular uma expressão matemática.
Exemplo: `2 * 2`.
- **Buscar na Wikipedia**: Diga um comando para buscar informações na Wikipedia. Exemplo: `procure por "algo"`.
- **Saudar o Assistente:** Diga `"oi"` para receber uma saudação do Jarvis.

# Estrutura do Código
O projeto é composto pelos seguintes arquivos principais:

- `jarvis.py`: O script principal que contém a lógica do assistente Jarvis.
- `utils.py`: (Opcional) Contém funções auxiliares para o Jarvis.

# Exemplos
Aqui estão alguns exemplos de uso do Jarvis:

### 🧮 Cálculo Matemático
```plaintext
[ JARVIS ] Diga a expressão matemática:
>>> 5 * (3 + 2)
[ JARVIS ] 5 * (3 + 2) = 25.
```
### 🔎 Busca na Wikipedia
```plaintext
[ JARVIS ] Diga o que você gostaria de saber:
>>> quem é Albert Einstein
[ JARVIS ] Resultado: Albert Einstein foi um físico teórico...
```
### 💭 Saudar o Assistente
```plaintext
[ JARVIS ] Diga "oi":
>>> oi
[ JARVIS ] Olá Vinícius, precisa de alguma coisa?
```
