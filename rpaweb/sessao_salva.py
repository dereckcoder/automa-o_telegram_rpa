from playwright.sync_api import Page

def sessao_salva(page: Page) -> bool:
    url = page.url.lower()

    if "startslo" in url:
        return False
    if "login" in url or "startsso" in url or "idp" in url:
        return False
    if page.locator("#username").count() > 0:
        return False
    if page.locator("#password").count() > 0:
        return False
    if page.get_by_text("O processo de logout foi concluído com sucesso").count() > 0:
        return False
    if page.get_by_text("Painel atual:").count() > 0:
        return True
    if page.get_by_role("button", name="Iniciar").count() > 0:
        return True
    if page.locator("input.slpt-text-input-container-input").count() > 0:
        return True
    return False