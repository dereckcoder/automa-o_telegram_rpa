from playwright.sync_api import Page
from settings import url_tela_formulario
from settings import url_tela_launchpad

# controle de anti-inatividade 
def manter_sessao_ativa(page: Page):
    page.goto(url_tela_launchpad)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    page.mouse.move(300, 300)
    page.mouse.click(300, 300)
    page.keyboard.press("Tab")

    page.goto(url_tela_formulario)
    botao = page.get_by_role("button", name="Iniciar")
    botao.click()
    
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
