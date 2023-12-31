from letterboxd import LetterBoxd
from telegram import Telegram

offset = 0
telegram = Telegram()


def send_text(chat_id, msg):
    telegram.send_message(message=msg, chat_id=chat_id)


while True:
    updates = telegram.get_updates(offset)

    if updates:
        if offset == 0:
            offset = updates[0]["update_id"]

        user_id = updates[0]["message"]["from"]["id"]
        chat_id = updates[0]["message"]["chat"]["id"]
        message_text = updates[0]["message"]["text"]

        if message_text.startswith("/"):
            if message_text == "/start":
                coincidences = "\n".join(LetterBoxd.get_watchlist())

                send_text(chat_id, coincidences)

        offset += 1
