from letterboxd import LetterBoxd
from decouple import config
import telebot


bot = telebot.TeleBot(config("TELEGRAM_TOKEN"), parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, LetterBoxd.get_watchlist())


bot.infinity_polling()
