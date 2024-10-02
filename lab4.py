from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass

class EmailNotification(Notification):
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print(f"Sent email with title '{title}' to '{self.admin_email}' that says '{message}'.")

class SlackApi:
    def __init__(self, login: str, api_key: str):
        self.login = login
        self.api_key = api_key

    def send_message(self, chat_id: str, message: str) -> None:
        print(f"Sent Slack message to chat '{chat_id}' that says '{message}'.")

class SlackNotificationAdapter(Notification):
    def __init__(self, slack: SlackApi, chat_id: str):
        self.slack = slack
        self.chat_id = chat_id

    def send(self, title: str, message: str) -> None:
        full_message = f"{title}: {message}"
        self.slack.send_message(self.chat_id, full_message)

class SmsApi:
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    def send_sms(self, message: str) -> None:
        print(f"Sent SMS from '{self.sender}' to phone '{self.phone}' with message '{message}'.")

class SmsNotificationAdapter(Notification):
    def __init__(self, sms_api: SmsApi):
        self.sms_api = sms_api

    def send(self, title: str, message: str) -> None:
        full_message = f"{title}: {message}"
        self.sms_api.send_sms(full_message)

email_notification = EmailNotification("admin@example.com")
slack_api = SlackApi("user_login", "api_key_12345")
slack_notification = SlackNotificationAdapter(slack_api, "chat_id_001")
sms_api = SmsApi("+123456789", "CompanyName")
sms_notification = SmsNotificationAdapter(sms_api)

def notify_all(title: str, message: str):
    email_notification.send(title, message)
    slack_notification.send(title, message)
    sms_notification.send(title, message)

notify_all("System Update", "The system will be updated at 12:00 AM.")
