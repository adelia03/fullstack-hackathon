import telebot
import sqlite3
from decouple import config 

token = config("TOKEN")

bot = telebot.TeleBot(token)

keyborard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton("Дети")
button2 = telebot.types.KeyboardButton("Детский дом")
button3 = telebot.types.KeyboardButton("Бездомнные")
button4 = telebot.types.KeyboardButton("Животные")
button5 = telebot.types.KeyboardButton("Дом престарелых")
keyborard.add(button1,button2,button3,button4,button5)

@bot.message_handler(commands=["start"])
def start_message(message):
    connect = sqlite3.connect("user.db")
    cursor = connect.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXITSTS login_id(
        id INTEGER,
    )""")
    connect.commit()

    peple_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE ID = {people_id}")

    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyborard)
    bot.send_photo(message.chat.id, "")
    bot.register_next_step_handler(message,reply_to_button)

@bot.message_handler(func=lambda x:True)
def reply_to_button(message):
    if message.text  == 'link':
        bot.send_message(message.chat.id, '')
    elif message.text == 'transition':
        bot.send_message(message.chat.id, '')
    else:
        bot.send_message(message.id,"Click on the button")
        bot.register_next_step_handler(message,reply_to_button)

bot.polling(none_stop=True, interval=0)              
