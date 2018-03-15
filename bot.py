import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Ну здравствуй, молодой пидорас, какое у тебя имя?')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Мне вообще ткак то на тебя похуй, иди сосать')

bot.polling()
