import queue
import threading
import telebot

from settings import token_telegram
from rpatelegram.bot_telegram import iniciar_bot_escuta_telegram
from rpaweb.bot_rpa import iniciar_worker

bot = telebot.TeleBot(token_telegram)

fila_trabalho = queue.Queue()
fila_mfadu = queue.Queue()
thread_worker = threading.Thread(target=iniciar_worker,args=(bot,fila_trabalho,fila_mfadu),daemon=False)

print("RPA ON RESET")

thread_worker.start()
iniciar_bot_escuta_telegram(bot,fila_trabalho,fila_mfadu)
bot.infinity_polling()