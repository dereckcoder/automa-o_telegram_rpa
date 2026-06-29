# 🤖 Automação de Reset de Senhas com Python + Playwright + Telegram 

# Projeto de RPA (Robotic Process Automation) 
Desenvolvido em Python para automatizar o processo de reset de senhas através da integração entre Telegram Bot e Playwright.

O objetivo do projeto é eliminar processos manuais.

# 🚀 Funcionalidades
1 Solicitação de reset via Telegram

2 Validação automática dos dados recebidos

3 Processamento utilizando fila (queue.Queue)

4 Worker dedicado para execução do RPA

5 Automação Web utilizando Playwright

6 Login automático no sistema

7 Autenticação 2FA integrada ao Telegram

8 Envio da nova senha diretamente ao usuário

9 Sistema de Keep Alive para evitar logout por inatividade

10 Recuperação automática da sessão

# ⚠️ Observação Importante


Este projeto foi desenvolvido para automatizar um sistema específico, cuja interface, elementos HTML e fluxo de autenticação foram utilizados durante o desenvolvimento.

Embora a arquitetura do projeto (Telegram Bot, filas de processamento, Playwright, gerenciamento de sessão e autenticação 2FA) possa ser reutilizada em outros cenários, a automação em si não funcionará em outros sites sem adaptações.

Para utilizar este projeto em outro sistema, será necessário, no mínimo:

Ajustar os seletores do Playwright (locators);
Adaptar o fluxo de login;
Configurar a autenticação (caso exista 2FA);
Alterar o fluxo de navegação;
Implementar a lógica específica do novo sistema.

Em resumo, este repositório deve ser utilizado como uma base de arquitetura para RPAs em Python, servindo como referência para o desenvolvimento de novas automações, e não como uma solução universal para qualquer aplicação web.

# 📂 Estrutura do Projeto
automacao_telegram_rpa/

├── main.py

├── settings.py

├── requirements.txt

rpatelegram/

 ├── bot_telegram.py
 
rpaweb/

 ├── bot_rpa.py

 ├── login_site.py

 ├── reset_password.py

 ├── anti_inatividade.py

 ├── sessao_salva.py


# ⚙️ Requisitos
Python 3.12+

Playwright

pyTelegramBotAPI

Queue

Threading

Linux / Ubuntu (WSL recomendado)

Google Chrome ou Chromium

# 📦 Instalação /🔐 Configuração

Clone o projeto

Crie o ambiente virtual

pip install -r requirements.txt

Crie um arquivo .env

TOKEN_TELEGRAM= ;
ID_CONTATO_TELEGRAM=

SITE_USER= ;
SITE_SENHA= ;
URL_TELA_LOGIN= 

URL_TELA_FORMULARIO=;
URL_TELA_LAUNCHPAD=

# ▶️ Executando
python main.py

# 👨‍💻 Autor

Dereck de Lara

Projeto desenvolvido para estudos e facilitar meu trabalho = Automação de Processos (RPA).

# ⭐ Contribuição

Contribuições são bem-vindas.

Caso encontre algum bug ou tenha sugestões de melhorias, fique à vontade para abrir uma Issue ou Pull Request.

# 📄 Licença

Este projeto está licenciado sob a licença MIT.

