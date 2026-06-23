import queue # fila telegram
import telebot # bot telegram 
import re # formatacao de texto
from settings import token_telegram # importa token
from settings import id_contado_telegram # importa id contado admin

def iniciar_bot_escuta_telegram(bot: telebot.TeleBot, fila_trabalho: queue.Queue):

    @bot.message_handler(commands=["start", "help"])
    def comando_start(message):
        texto = ("🤖 *BOT ALIANÇA SUL RPA - SISTEMA INICIADO*\n\n"
            "Para solicitar um reset de senha, envie o loginZ "
            "e o Nome do colaborador no formato abaixo:\n"
            "`LoginZ Nome Completo`\n\n"
            "💡 *Exemplo:* `Z12345 Joaozinho da silva`")
        bot.send_message(message.chat.id, texto, parse_mode="Markdown")
        print("bot ligado")

    ### raspa as messangens digitas pelo usuario ###  
    @bot.message_handler(func=lambda message: True)
    def receber_messagem(message):
        try:       
            chat_id = message.chat.id
            texto = message.text
            texto = message.text.strip() 
            resultado = re.match(r'^([A-Za-z]?\d{6})\s+(.+)$', texto)#formataco de texto
            if not resultado:
                bot.send_message(chat_id, "Formato inválido.\nExemplo:\nZ12345 Joaozinho da silva")
                return    
            login_z = resultado.group(1).upper()
            nome_login_z = resultado.group(2).upper()
            
            print("valorZ guardado e valor nome guardado")
            bot.send_message(chat_id,
            "✅*Dados recebidos com sucesso!*\n"
            f"👤 *Nome:* {nome_login_z}\n"
            f"🔑 *LoginZ:* {login_z}\n\n"
            f"⏱️ Sua solicitação entrou na fila de processamento.",parse_mode="Markdown")   
            fila_solicitacao = {
                "chat_id": chat_id,
                "Nome": nome_login_z,
                "LoginZ": login_z}
            fila_trabalho.put(fila_solicitacao)
            bot.send_message(chat_id,"✅ Solicitação adicionada à fila.") 
            
        ### vai rodar com erro ###        
        except Exception as e: 
            print(f"ERRO: {e}")
            bot.send_message(chat_id, "❌Ocorreu um erro ao processar sua solicitação."
                                                       "\nLIGUE PARA O ADMINISTRADOR")
    bot.infinity_polling()

def main():

    bot = telebot.TeleBot(token_telegram)
    fila_trabalho = queue.Queue()

    iniciar_bot_escuta_telegram(
        bot,
        fila_trabalho
    )


if __name__ == "__main__":
    main()