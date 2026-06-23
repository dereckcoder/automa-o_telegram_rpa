import queue
import telebot
from settings import token_telegram # importa token
from settings import id_contado_telegram # importa id contado admin
from bot_telegram import iniciar_bot_escuta_telegram




def main():

    bot = telebot.TeleBot(token_telegram)
    fila_trabalho = queue.Queue()

    iniciar_bot_escuta_telegram(
        bot,
        fila_trabalho
    )
if __name__ == "__main__":
    main()