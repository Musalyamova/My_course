import telebot

token = '7512213683:AAFjpqFOfaQ-89A6Rq2Q-LMHmSDlptRZ5YY'

bot = telebot.TeleBot(token) # переменная, которая хранит все необходимые функции для обработки и ответа на сообщения

text1 = "Ба! Знакомые все лица!"

@bot.message_handler(content_types = ['text'])
def echo(message):
    if "Alina" in message.text:
        bot.send_message(message.chat.id, text1)
    else:
        bot.send_message(message.chat.id, message.text)

#Постоянно обращается к серверам телеграм
bot.polling(none_stop=True) # начинает отправку запросов серверам телеграм, используя наш токен