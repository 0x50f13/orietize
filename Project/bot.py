import glob
from os.path import join, basename, isfile, abspath
from util import load_module
from telegram.ext import Updater


from config import *
import datetime

class Bot:
    def __init__(self, token):
        self.status_str="OFFLINE"
        self.processed=0
        self.starttime=datetime.datetime.now()
        self.chats=[]
        self._updater = Updater(token=token)
        modules = self.find_modules(os.path.join(BASE_DIR, "handlers/"))
        for module in modules:
            mod=load_module(abspath(join("handlers/",module)))
            self._updater.dispatcher.add_handler(mod.handler)
        self.messages=dict()

    @staticmethod
    def error(bot, update, error):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, error)
    @staticmethod
    def find_modules(path):
        modules = glob.glob(path + "/*.py")
        return [basename(f) for f in modules if isfile(f) and not f.endswith('__init__.py')]

    def run(self):
        self.status_str="RUNNING"
        self._updater.start_polling()
