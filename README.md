# assistentes
Repositório contendo o código e recursos para três assistentes virtuais: Karen, Guideon e Jarvis. Cada assistente tem sua própria pasta com arquivos e configurações.

Guideon
Guideon é um assistente virtual desenvolvido em Python que oferece uma variedade de funcionalidades úteis através de um terminal interativo. Este assistente é capaz de realizar cálculos matemáticos, varrer redes para identificar dispositivos ativos e consultar informações WHOIS sobre domínios.

Funcionalidades
Cálculos Matemáticos: Permite ao usuário inserir uma expressão matemática e retorna o resultado.
Varredura de IPs: Identifica dispositivos ativos na rede local através da varredura de IPs.
Consulta WHOIS: Obtém informações WHOIS para um domínio, fornecendo detalhes sobre o registro do site.
Requisitos
Certifique-se de ter o Python 3 instalado no seu sistema. Além disso, você precisará instalar as seguintes bibliotecas Python:

colorama
tabulate
Você pode instalar essas bibliotecas usando pip:

bash
Copiar código
pip install colorama tabulate
Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
Execute o código:

bash
Copiar código
python guideon.py
Siga as instruções no terminal para interagir com o assistente Guideon. Você pode:

Calcular Expressões: Digite uma expressão matemática quando solicitado.
Varrer IPs: Forneça o IP da rede local para listar dispositivos ativos.
Consultar WHOIS: Insira um link para obter informações WHOIS sobre o domínio.
Estrutura do Código
guideon.py: O script principal que contém a lógica do assistente Guideon.
NetScan.py: Contém funções para escanear a rede e obter o intervalo de IPs.
site_utils.py: Inclui funções para obter informações WHOIS e extrair o domínio do link.
Contribuição
Se você deseja contribuir para o projeto, sinta-se à vontade para enviar pull requests. Verifique o guia de contribuição para mais detalhes.

Licença
Este projeto está licenciado sob a MIT License.

