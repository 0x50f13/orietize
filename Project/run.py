#######################################
# (C)Copyrighting Evolution corp. 2018#
#######################################
import threading

from bot import Bot
from config import API_KEY, DEBUG
from web.web import site

mutex = threading.Lock()


class App:
    def __init__(self):
        self.bot = Bot(API_KEY)
        self.web = site

    def run(self):
        botThread = threading.Thread(target=self.bot.run)
        webThread = threading.Thread(target=self.web.run, kwargs={"host": "localhost", "port": 8080, "debug": DEBUG})
        botThread.start()
        webThread.start()


if __name__ == '__main__':
    app = App()
    app.run()
