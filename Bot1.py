import telebot
from telebot import apihelper

bot = telebot.TeleBot('1233009953:AAFQwx_3GRp53bFsoCVmib4yqYKdeyLEPwU')
apihelper.proxy = ("https" 'socks5://45.225.88.147:999')

@bot.message_handler(commands=['start'])
def lalala(message):
     bot.send_message(message.chat.id, 'медфорд')

     bot.polling(nond_stop=True, interval=0)