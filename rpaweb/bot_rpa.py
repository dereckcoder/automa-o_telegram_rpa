import queue
import time
import telebot
import threading

from playwright.sync_api import Page, sync_playwright
from settings import token_telegram # importa token
from settings import id_contado_telegram # importa id contado admin
from rpatelegram.bot_telegram import iniciar_bot_escuta_telegram

from rpaweb.login_site import fazer_login_site
from settings import url_tela_login
from settings import site_user 
from settings import site_senha

from rpaweb.reset_password import reset_senha
from settings import url_tela_formulario


def iniciar_worker(bot, fila_trabalho):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        fazer_login_site(page,site_user,site_senha,url_tela_login)

        while True:

            solicitacao = fila_trabalho.get()

            login_z = solicitacao["LoginZ"]
            print(solicitacao)

            nova_senha = reset_senha(page,login_z,url_tela_formulario)

            bot.send_message(solicitacao["chat_id"],f"Nova senha: {nova_senha}")

            fila_trabalho.task_done()