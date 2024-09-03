from plyer import notification
from datetime import date

def notify(success=False):
    current_date = date.today().strftime('%A %d. %B %Y')
    
    if success:
        title = "Email enviado com sucesso!"
    else:
        title = "Falha ao enviar o email!"
    
    try:
        notification.notify(
            title=title,
            message=f"Hora da tentativa: {current_date}",
            timeout=5
        )
    except Exception as e:
        print(f"Erro ao tentar mostrar a notificação: {e}")


