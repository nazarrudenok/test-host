import telebot

bot = telebot.TeleBot('7124524639:AAH4BTiJH38C8YHN8HPdNQTTJ5iotTxfqNI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hello bro')

bot.polling()