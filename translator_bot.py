#!C:\Users\SamRayaneh\Desktop\python-tel-bot\myvenv\Scripts\python.exe


import telebot
from telebot import types
from googletrans import Translator
import tkinter as tk

TOKEN = "6690725348:AAG1uA-qvssjUpYoBtBk9UMnwzS3A9TKtnA"
bot = telebot.TeleBot(TOKEN)
translator = Translator()



def translate_text(message):
    bot.reply_to(message, 'Please enter the texts:')
    bot.register_next_step_handler(message, translate)

def translate(message):
    text = message.text
    translation = translator.translate(text, dest='fa')
    bot.send_message(message.chat.id, translation.text)
    translate_text(message)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Enlish to persian')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Welcome to the translate bot!", reply_markup=markup)
    bot.register_next_step_handler(message, translate_text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

def open_gui():
    root = tk.Tk()
    root.title("Telegram Bot GUI")

    label = tk.Label(root, text="Enter text:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button_translate = tk.Button(root, text="Translate", command=lambda: translate(entry.get()))
    button_translate.pack()

    root.mainloop()

if __name__ == '__main__':
    bot.polling()
    open_gui()