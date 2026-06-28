from playwright.sync_api import Page

from settings import url_tela_formulario
from settings import url_tela_launchpad

def manter_sessao_ativa(page: Page):
    print("Voltando para launchpad...")

    page.goto(url_tela_launchpad)
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
    print("Voltando para formulário...")

    page.goto(url_tela_formulario)
    page.wait_for_load_state("networkidle")
    print("foi")
    