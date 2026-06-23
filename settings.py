# configuraracao de senhas/token 
from dotenv import load_dotenv
import os

load_dotenv()

token_telegram = os.getenv("token_telegram")
id_contado_telegram = os.getenv("id_contado_telegram")
site_user = os.getenv("site_user")
site_senha = os.getenv("site_senha")
url_tela_login = os.getenv("url_tela_login")
url_tela_formulario = os.getenv("url_tela_formulario")


