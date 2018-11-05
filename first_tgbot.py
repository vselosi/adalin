from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token = '693973082:AAHPxE9QT4Bhd1eO024bzjCyRixOrYL5K9g')
dispatcher = updater.dispatcher

def startComand(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = 'Hellow!')
def textMessage(bot, update):
    response = 'Got your message: ' + update.message.text
    bot_send_message(chat_id = update.message.chat_id, text = response)

start_command_handler = CommandHandler('start', startComand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean = True)

updater.idle()
