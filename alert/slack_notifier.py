# slack_notifier.py

import json
import requests

class SlackNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message):
        payload = {"text": message}
        response = requests.post(self.webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        return response.status_code
