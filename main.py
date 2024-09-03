import smtplib
from config import EMAIL_KEY, EMAIL_NAME
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notefication import notify  # Certifique-se de que o nome do arquivo e da função está correto

def send_email(recipient, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sending = EMAIL_NAME
    key = EMAIL_KEY

    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = sending
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Usa TLS para segurança
        server.login(sending, key)  # Faz login

        # Envia o e-mail
        server.sendmail(sending, recipient, msg.as_string())

        # Fecha a conexão
        server.quit()
        notify(success=True)  # Notifica sucesso

    except Exception as e:
        notify(success=False)  # Notifica falha

if __name__ == "__main__":
    # Solicita as entradas do usuário
    recipient = input("Digite o e-mail do destinatário: ")
    subject = input("Digite o assunto do e-mail: ")
    message = input("Digite a mensagem do e-mail: ")

    # Envia o e-mail usando a função
    send_email(recipient, subject, message)
