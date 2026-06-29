import queue
from playwright.sync_api import Page, sync_playwright
from settings import url_tela_login
from settings import site_user 
from settings import site_senha


def fazer_login_site(page: Page, site_user, site_senha, url_tela_login: str,bot,fila_mfadu,id_admin: str) -> bool: 
    
    print("🔐 [LOGIN] Acessando o portal do site...")
    page.goto(url_tela_login)

    # manipulacao o prenecimento nos campos de user e senha
    page.wait_for_load_state("networkidle")
    page.locator("#username").wait_for(state="visible", timeout=10000) # Espera até 10 segundos o campo surgir
    page.locator("#username").fill(site_user)
    page.locator("#password").wait_for(state="visible", timeout=10000) # Espera até 10 segundos o campo surgir
    page.locator("#password").fill(site_senha)
    page.locator("#signOnButton").wait_for(state="visible")
    page.locator("#signOnButton").click()
     
    # etapa de autenticação 2FA com DUO 
    print("Aguardando botao 1 duo...")
    """
    # etapa 1 2FA - ignorar temporariamente 
    botao = page.locator("div.display-flex button.button")
    botao.wait_for(state="visible", timeout=10000)
    botao.click() 
    """ 
    # etapa 2 2FA - outras opções
    botao = page.locator("button.VerifiedPush--other-options-button")
    botao.wait_for(state="visible", timeout=10000)
    botao.click(force=True)
    # etapa 3 2FA - codigo/acesso/duo/mobile
    botao = page.locator("button.auth-method").nth(1) # seleciona o intem 1
    botao.wait_for(state="visible", timeout=10000)
    botao.click()
    # etapa 4 2FA - codigo 2fa
    campo_codigo = page.locator("#passcode-input")
    campo_codigo.wait_for(state="visible", timeout=10000)
    bot.send_message(id_admin,"manda o codigo ai Mestre master grum")
    try:
        token_duo = fila_mfadu.get(timeout=120)
        campo_codigo.fill(token_duo)
    except:
        bot.send_message(id_admin,"tempo")
        return False
    # etapa 5 2FA - botao/verificar
    botao = page.locator("[data-testid='verify-button']")
    botao.wait_for(state="visible", timeout=10000)
    botao.click()
    print("✅ Login efetuado com sucesso!")
    
    try:
        page.get_by_text("Painel atual:").wait_for(timeout=30000)
        return True
    except:
        print("Falha ao validar 2FA...")
        return False
##################################################################


