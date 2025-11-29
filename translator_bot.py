import telebot
from telebot import types
from googletrans import Translator
import requests

TOKEN = "6690725348:AAG1uA-qvssjUpYoBtBk9UMnwzS3A9TKtnA"
bot = telebot.TeleBot(TOKEN)
translator = Translator()

def remove_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    try:
        r = requests.get(url)
        print("Webhook delete response:", r.text)
    except Exception as e:
        print("Webhook delete failed:", e)


remove_webhook()


def translate_next(message):
    text = message.text
    translation = translator.translate(text, dest='fa')
    bot.send_message(message.chat.id, translation.text)

    bot.send_message(message.chat.id, "Send another text:")
    bot.register_next_step_handler(message, translate_next)


# --------------------------
#        /start
# --------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn = types.KeyboardButton("English → Persian")
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Welcome! Choose an option:",
        reply_markup=markup
    )


@bot.message_handler(func=lambda msg: msg.text == "English → Persian")
def ask_text(message):
    bot.send_message(message.chat.id, "Send the English text:")
    bot.register_next_step_handler(message, translate_next)


@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "Please select an option from the menu.")


print("Bot is running...")
bot.infinity_polling()
