from telegram.ext import MessageHandler, Filters
class Test:
    def handle(self,bot,update):
        update.message.reply_text(update.message.text)
t=Test()
handler=MessageHandler(Filters.text, t.handle)