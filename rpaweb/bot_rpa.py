import time
import telebot
import threading
import queue

from playwright.sync_api import sync_playwright

from settings import id_contado_telegram
from settings import url_tela_login
from settings import site_user
from settings import site_senha
from settings import url_tela_formulario

from rpaweb.login_site import fazer_login_site
from rpaweb.reset_password import reset_senha
from rpaweb.anti_inatividade import manter_sessao_ativa
from rpaweb.sessao_salva import sessao_salva

def iniciar_worker(bot, fila_trabalho,fila_mfadu):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def garantir_sessao(page) -> bool:
            if sessao_salva(page):
                return True
            bot.send_message(id_contado_telegram, "⚠️ Sessão caiu. Refazendo login...")
           
            return fazer_login_site(page,site_user,site_senha,url_tela_login,bot,fila_mfadu,id_contado_telegram)     
        ultimo_anti_inatividade = time.time()
        while True:
            try:
                solicitacao = fila_trabalho.get(timeout=5)
                try:
                    login_z = solicitacao["LoginZ"]
                    chat_id = solicitacao["chat_id"]
                    print(solicitacao)

                    if not garantir_sessao(page):
                        bot.send_message(chat_id,"❌ Não foi possível recuperar a sessão.")
                        continue
                    
                    resultado = reset_senha(page,login_z,url_tela_formulario)
                    if resultado["status"] == "sucesso":
                        bot.send_message(chat_id,
                            f"✅ Reset realizado\n\n"
                            f"👤 {resultado['colaborador']}\n"
                            f"🔐 Nova senha: {resultado['nova_senha']}")
                    else:
                        bot.send_message(
                        chat_id,
                        f"❌ Erro no reset do {resultado['login_z']}")
                    time.sleep(20)

                    if garantir_sessao(page):
                        manter_sessao_ativa(page)
                        ultimo_anti_inatividade = time.time()
                    else:
                        bot.send_message(id_contado_telegram,"❌ Não foi possível recuperar a sessão após o reset.")

                except Exception as e:
                    bot.send_message(solicitacao["chat_id"],
                        f"❌ Erro inesperado: {e}")
                    print(solicitacao)
                finally:
                    fila_trabalho.task_done()
            except queue.Empty:
                agora = time.time()
                if agora - ultimo_anti_inatividade >= 20:
                    if garantir_sessao(page):
                        manter_sessao_ativa(page)
                        ultimo_anti_inatividade = time.time()
                    else:
                        bot.send_message(id_contado_telegram,"❌ Não foi possível recuperar a sessão no anti-inatividade.")

