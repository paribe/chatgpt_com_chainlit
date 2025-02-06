# Chatbot com Chainlit

Este projeto é um chatbot simples usando a biblioteca [Chainlit](https://github.com/Chainlit/chainlit). O bot responde a mensagens verificando se a palavra "python" está presente no texto enviado pelo usuário.

## 📌 Requisitos

Antes de executar o código, certifique-se de ter o Python instalado e o Chainlit configurado.

### Instalação das Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

2. Instale o Chainlit:
   ```sh
   pip install chainlit
   ```

## 🚀 Como Executar o Projeto

1. Salve o código no arquivo `main.py`.
2. Execute o chatbot com o seguinte comando:
   ```sh
   chainlit run main.py
   ```
3. Uma interface será aberta no navegador para interagir com o bot.

## 📜 Explicação do Código

- O decorador `@cl.on_message` define a função `main()` que será chamada sempre que o usuário enviar uma mensagem.
- O bot verifica se a palavra "python" está presente na mensagem:
  - Se estiver, responde com: **"Parabéns, tá aprendendo uma boa linguagem"**.
  - Caso contrário, responde com: **"Já pensou em aprender Python?"**.

## 🔗 Links Úteis
- [Documentação do Chainlit](https://docs.chainlit.io/)
- [Repositório oficial no GitHub](https://github.com/Chainlit/chainlit)

---

🚀 **Agora é só rodar o chatbot e começar a interagir!**

