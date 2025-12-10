import streamlit as st
import random

st.title("🎮 Jogo de Adivinhação") # Para rodar no terminal digite: "streamlit run jogos.na.web.py" dentro da pasta
st.subheader("SE ACERTAR GANHA UM PIX DE R$ 49,99")  # texto menor logo
# Gera número secreto (pode ser fixo ou aleatório)
numero_secreto = random.randint(1, 50)

# Entrada do usuário
palpite = st.number_input("Vamos ver se você tem sorte mesmo, escolhe ai um número de 1 a 50:")

# Botão para verificar
if st.button("Pode enviar"):
    if palpite == 20.25:
        st.success("Ótima resposta, você acertou!!")
    elif palpite > 20.25:
        st.info("Bom chute! Mas, o número certo é menor.")
    else:
        st.warning("Putsss, quase! Mas, o número certo é maior.")



#Site do Jogo
#https://jogo-de-adivinha-cmkjyqinpozzejwkvx4ff8.streamlit.app/
