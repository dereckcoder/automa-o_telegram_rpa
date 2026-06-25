### AUTOMAÇÃO RPA ###

# FLUXO 

[ENTRADA-TELEGRAM(X)] -> [PROCESSAMENTO_BOT_RPA] -> [SAIDA-TELEGRAM(Y)]

.env - cofre dos tokens 
settings - importa dados do .env para usar no resto do codigo 
bot_telegram - Coleta dados para usar no rpa 
bot_rpa - pega dados do bot_telegram e faz ação 
main - ele liga todas as aplicações 




auth/ - modularicao para chamar para fazer login