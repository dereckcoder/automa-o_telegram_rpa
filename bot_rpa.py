import queue
import telebot
import time
from playwright.sync_api import Page
from settings import url_tela_login
from settings import site_user
from settings import site_senha 
from settings import url_tela_formulario
from playwright.sync_api import sync_playwright


#def fazer_login_site(bot: telebot.TeleBot, fila_trabalho: queue.Queue, page: Page) -> bool:
def fazer_login_site(page,url_tela_login):
    print("🔐 [LOGIN] Acessando o portal do teste site...")
    
    page.goto(url_tela_login)
    page.wait_for_timeout(3000)
    print("boa")
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page()
    
    fazer_login_site(page, url_tela_login)
    

