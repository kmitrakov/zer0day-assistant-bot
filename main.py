import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def telegram_bot(telegram_token):
    bot = telebot.TeleBot(telegram_token)

    @bot.message_handler(commands=["start", "help"])
    def start_message(message):
        bot.send_message(
            message.chat.id,
            f"Привет, {message.from_user.username}!\n\nВот что я умею:\n"
            f"/help - показать список команд"
        )

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        bot.send_message(
            message.chat.id,
            f"Я не знаю такой команды..."
        )

    bot.polling()

if __name__ == "__main__":
    telegram_bot(TELEGRAM_TOKEN)