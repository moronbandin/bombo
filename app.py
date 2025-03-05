import streamlit as st
import scipy.stats as stats
import random

# Función para calcular a probabilidade de que polo menos un tema estudado saia no exame
def calcular_probabilidade(temas_totais, temas_estudados, bolas_extraidas):
    """
    Calcula a probabilidade de que polo menos un dos temas estudados saia no exame.

    :param temas_totais: Número total de temas no temario.
    :param temas_estudados: Número de temas estudados.
    :param bolas_extraidas: Número de bolas extraídas no exame.
    :return: Probabilidade en porcentaxe.
    """
    if temas_estudados > temas_totais or bolas_extraidas > temas_totais:
        return "Erro: Os valores introducidos non son válidos."

    # Probabilidade de que ningún dos temas estudados saia no exame
    prob_ningun = stats.hypergeom.pmf(0, temas_totais, temas_estudados, bolas_extraidas)
    # Probabilidade de que polo menos un saia
    prob_polo_menos_uno = 1 - prob_ningun
    # Converter a porcentaxe
    return round(prob_polo_menos_uno * 100, 2)

# Configuración da app en Streamlit
st.title("🎯 OpoBombo - Calculadora de probabilidade para oposicións")
st.write("Esta aplicación calcula a probabilidade de que polo menos un dos temas que estudaches saia no exame.")

# Inputs do usuario
temas_totais = st.number_input("Número total de temas no temario:", min_value=1, value=68)
temas_estudados = st.number_input("Número de temas que estudaches:", min_value=1, max_value=temas_totais, value=10)
bolas_extraidas = st.number_input("Número de bolas extraídas no exame:", min_value=1, max_value=temas_totais, value=4)

# Botón para calcular a probabilidade
if st.button("📊 Calcular Probabilidade"):
    resultado = calcular_probabilidade(temas_totais, temas_estudados, bolas_extraidas)

    if isinstance(resultado, str):
        st.error(resultado)
    else:
        # Código cromático segundo a probabilidade
        if resultado < 30:
            color = "red"
            mensaxe = "😟 A probabilidade é baixa, pero non te desanimes! Segue estudando, cada tema conta!"
        elif resultado < 60:
            color = "orange"
            mensaxe = "🙂 Vas por bo camiño! Se aumentas un pouco os temas estudados, terás máis posibilidades!"
        else:
            color = "green"
            mensaxe = "🎉 Estás nunha moi boa posición! Segue así e afronta o exame con confianza!"

        # Mensaxe de resultado
        st.markdown(
            f'<div style="background-color:{color}; padding:10px; border-radius:5px; text-align:center;">'
            f'<h2 style="color:white;">Probabilidade: {resultado}%</h2>'
            f'<p style="color:white;">{mensaxe}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Botón para realizar o sorteo
if st.button("🎲 Sortear temas"):
    if bolas_extraidas > temas_totais:
        st.error("Erro: O número de bolas extraídas non pode ser maior que o número total de temas.")
    else:
        temas = list(range(1, temas_totais + 1))
        temas_sorteados = random.sample(temas, bolas_extraidas)
        st.success(f"📜 Os temas sorteados son: {', '.join(map(str, temas_sorteados))}")
