import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    conteudo = message.content.lower()
    
    if "bom dia" in conteudo:
        resposta = "Bom dia! Espero que tenha um ótimo dia! ☀️"
    elif "boa tarde" in conteudo:
        resposta = "Boa tarde! Como está indo o seu dia? 🌞"
    elif "boa noite" in conteudo:
        resposta = "Boa noite! Tenha um ótimo descanso! 🌙"
    elif "python" in conteudo:
        resposta = "Parabéns, tá aprendendo uma ótima linguagem! 🐍"
    elif "como você está" in conteudo or "tudo bem" in conteudo:
        resposta = "Estou bem, obrigado por perguntar! E você? 😊"
    elif "obrigado" in conteudo or "valeu" in conteudo:
        resposta = "De nada! Sempre que precisar, estou aqui. 👍"
    elif "clima" in conteudo or "tempo" in conteudo:
        resposta = "Infelizmente, não posso verificar o clima agora, mas você pode conferir em um aplicativo de meteorologia! ☁️"
    elif "notícias" in conteudo:
        resposta = "Para se manter atualizado, recomendo acessar um portal de notícias como BBC, CNN ou G1. 📰"
    elif "piada" in conteudo:
        resposta = "Por que o desenvolvedor foi ao terapeuta? Porque ele tinha muitos bugs! 😂"
    elif "motivação" in conteudo or "inspirar" in conteudo:
        resposta = "Nunca desista! Cada erro é um passo em direção ao sucesso. 💪"
    elif "angola" in conteudo.lower():
        resposta = "Sei que vai viajar para Angola, parabéns! ✈️🌍"
    else:
        resposta = "Não entendi muito bem. Já pensou em aprender Python? 🤔"
    
    # Enviar a resposta ao usuário
    await cl.Message(content=resposta).send()
