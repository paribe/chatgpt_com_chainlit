import streamlit as st

# Configuração da Página (DEVE SER A PRIMEIRA INSTRUÇÃO)
st.set_page_config(page_title="Chatbot com Streamlit", layout="centered")

st.title("🤖 Chatbot Simples com Streamlit")

def obter_resposta(mensagem):
    conteudo = mensagem.lower()
    
    if "bom dia" in conteudo:
        return "Bom dia! Espero que tenha um ótimo dia! ☀️"
    elif "boa tarde" in conteudo:
        return "Boa tarde! Como está indo o seu dia? 🌞"
    elif "boa noite" in conteudo:
        return "Boa noite! Tenha um ótimo descanso! 🌙"
    elif "python" in conteudo:
        return "Parabéns, tá aprendendo uma ótima linguagem! 🐍"
    elif "como você está" in conteudo or "tudo bem" in conteudo:
        return "Estou bem, obrigado por perguntar! E você? 😊"
    elif "obrigado" in conteudo or "valeu" in conteudo:
        return "De nada! Sempre que precisar, estou aqui. 👍"
    elif "clima" in conteudo or "tempo" in conteudo:
        return "Infelizmente, não posso verificar o clima agora, mas você pode conferir em um aplicativo de meteorologia! ☁️"
    elif "notícias" in conteudo:
        return "Para se manter atualizado, recomendo acessar um portal de notícias como BBC, CNN ou G1. 📰"
    elif "piada" in conteudo:
        return "Por que o desenvolvedor foi ao terapeuta? Porque ele tinha muitos bugs! 😂"
    elif "motivação" in conteudo or "inspirar" in conteudo:
        return "Nunca desista! Cada erro é um passo em direção ao sucesso. 💪"
    elif "angola" in conteudo:
        return "Sei que vai viajar para Angola, parabéns! ✈️🌍"
    elif "feio" in conteudo:
        return "Você precisa faer uma operação plastica, parabéns! ✈️🌍"
    

    else:
        return "Não entendi muito bem. Já pensou em aprender Python? 🤔"

# Caixa de entrada do usuário
mensagem = st.text_input("Digite sua mensagem:")

if st.button("Enviar"):
    if mensagem:
        resposta = obter_resposta(mensagem)
        st.write(f"**Bot:** {resposta}")
