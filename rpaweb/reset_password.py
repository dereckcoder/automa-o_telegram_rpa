
from playwright.sync_api import Page, sync_playwright
from settings import url_tela_login
from settings import url_tela_formulario

def reset_senha(page: Page, login_z,url_tela_formulario: str):
    print(login_z)

    
    print("[reset] Acessando o formulario...")
 
    page.goto(url_tela_formulario)
    
    botao = page.get_by_role("button", name="Iniciar")
    botao.click()

    campo = page.locator("input.slpt-text-input-container-input")
    campo.wait_for(state="visible", timeout=10000)
    campo.fill(login_z)

    print("Colocou na caixa formulario...")

    botao = page.locator(f"li[role='option']:has-text('{login_z}')")
    botao.wait_for(state="visible", timeout=10000)

    texto = botao.inner_text()
    print(texto)
    
    botao = page.get_by_text(login_z)#troca troca###
    botao.wait_for(state="visible", timeout=10000)
    botao.click()

    botao = page.get_by_role("button", name="Enviar")
    botao.click()

    try:
        page.get_by_text("Seu formulário foi enviado.").wait_for(timeout=15000)
        menssagem_sen = page.locator("p").filter(has_text="Nova senha:").inner_text()
        print(menssagem_sen)
        return True

    except:
        print("Falha ao validar formulário...")
        return False







