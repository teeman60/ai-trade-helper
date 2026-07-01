import requests

class AlertEngine:

    def send_telegram(self, token, chat_id, message):

        url = f"https://api.telegram.org/bot{token}/sendMessage"

        requests.post(url, json={
            "chat_id": chat_id,
            "text": message
        })
