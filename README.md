# Email Automation Example

Este é um exemplo de projeto Python para automação de envio de e-mails com notificação no Windows. O projeto demonstra como configurar e enviar e-mails automaticamente usando o protocolo SMTP, bem como notificar o usuário sobre o sucesso ou falha do envio através de notificações nativas do Windows.

## Funcionalidades

- **Envio Automático de E-mails:** Envie e-mails de forma programática usando o protocolo SMTP com autenticação.
- **Notificações no Windows:** Receba notificações no Windows sobre o status do envio do e-mail, indicando sucesso ou falha.
- **Exemplo de Configuração com Variáveis de Ambiente:** Use um arquivo `.env` para armazenar de forma segura as credenciais de e-mail.

## Tecnologias Utilizadas

- **Python 3.12.4:** Linguagem de programação principal utilizada no projeto.
- **smtplib:** Biblioteca padrão do Python para enviar e-mails via SMTP.
- **dotenv:** Gerenciamento de variáveis de ambiente.
- **plyer:** Biblioteca para exibir notificações no sistema operacional.
- **venv:** Ambiente virtual do Python para gerenciar dependências do projeto.

## Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/email-automation-example.git
cd email-automation-example

2. Configurar o Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto.

bash

python -m venv venv

Ative o ambiente virtual:

    Windows:

    bash

.\venv\Scripts\activate

Linux/Mac:

bash

    source venv/bin/activate

3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no requirements.txt:

bash

pip install -r requirements.txt

4. Configurar o Arquivo .env

Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:

env

EMAIL_KEY=your_email_password_or_app_key
EMAIL_NAME=your_email_address@gmail.com

Substitua your_email_password_or_app_key pelo seu app key ou senha de e-mail, e your_email_address@gmail.com pelo seu endereço de e-mail.
5. Executar o Projeto

Com todas as configurações prontas, você pode executar o script principal:

bash

python main.py

O script solicitará o e-mail do destinatário, o assunto e a mensagem a ser enviada. Após a execução, você verá uma notificação no Windows indicando se o envio foi bem-sucedido ou se houve uma falha.
Estrutura do Projeto

    config.py: Carrega as variáveis de ambiente do arquivo .env.
    main.py: Script principal que gerencia o envio de e-mails.
    notefication.py: Gerencia as notificações do sistema sobre o status do envio do e-mail.
    requirements.txt: Lista das dependências necessárias para o projeto.
    README.md: Documentação do projeto (este arquivo).
