import datetime


class Notification:
    def __init__(self, title, text):
        self.time = datetime.datetime.now()
        self.title = title
        self.text = text


class WebInterfaceManager:  # web interface wrapper
    notifications = []
    def notify(self,notification):
        self.notifications.append(notification)
    def get_notifications(self):
        r=self.notifications
        self.notifications=[]
        return r