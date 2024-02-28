from requests import post
from dotenv import load_dotenv
import os

load_dotenv()


email_address = os.environ.get('email')


def send_email(error):
    url = 'http://10.18.8.14:8085/api/v1/email/sendMessage'
    response = post(
        url,
        json={
            "subject": "Ошибка при синхронизации ckan",
            "text": f"{error}",
            "to": f"{email_address}"
        },
        headers={"Content-Type": "application/json"},
    )

    return response.json()
