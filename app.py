import streamlit as st
import scipy.stats as stats
import random

# Lista de nomes dos temas (debe ter exactamente tantos elementos como temas totais)
nomes_dos_temas = [
    "El Griego en el contexto de las lenguas indoeuropeas",
    "Los sistemas alfabéticos griegos: su origen, estructura, valores grafemáticos",
    "Su adopción por Roma: el alfabeto latino",
    "Signos ortográficos y de puntuación en griego",
    "El acento griego",
    "La transcripción y transliteración de términos griegos",
    "El sistema vocálico griego. Origen y evolución. Las laringales y su pervivencia en griego",
    "El sistema consonántico griego. Origen y evolución",
    "La métrica griega. Nociones generales de prosodia y métrica latina",
    "Composición y derivación en palabras de raíz grecolatina. Prefijos y sufijos. Etimología de las terminologías científica y técnica",
    "Concepto de flexión nominal en una lengua flexiva. La flexiva nominal indoeuropea y su evolución en las lenguas clásicas",
    "Flexión de los temas en –α y flexión temática",
    "Flexión de los temas en oclusiva. Líquida y nasal",
    "Flexión de los temas en silbante, semivocal y diptongo",
    "Influjo de la lengua griega en la evolución de la lengua latina. La adaptación de la flexión griega a la flexión latina. Conceptos generales sobre la flexión nominal latina",
    "Nociones generales sobre el adjetivo en las lenguas clásicas. Clasificación, grados y sintaxis del adjetivo en griego. Numerales",
    "Características de la flexión pronominal en las lenguas clásicas. Morfosintaxis de los pronombres personales, demostrativos y anafóricos en griego",
    "Morfosintaxis de los pronombres relativos, interrogativos e indefinidos en griego. Estudio especial de las oraciones de relativo",
    "Morfosintaxis de adverbios y preposiciones en las lenguas clásicas",
    "La sintaxis: concepto. Función de los casos en las lenguas clásicas. Corrientes actuales sobre el estudio de los casos. Nominativo y vocativo en griego: origen indoeuropeo, evolución y funciones sintácticas",
    "Acusativo en griego: origen indoeuropeo, evolución y funciones sintácticas",
    "Genitivo y dativo en griego: origen indoeuropeo, evolución y funciones sintácticas",
    "Fundamentos indoeuropeos, estructura y evolución de la flexión verbal en las lenguas clásicas...",
    "Morfosintaxis de los temas de futuro y de perfecto en griego",
    "Morfosintaxis de los modos personales en griego. Morfosintaxis del infinitivo, participio y adjetivo verbal en griego",
    "El orden de palabras en la frase. La concordancia...",
    "Proposiciones sustantivas en griego",
    "Proposiciones adverbiales en griego: temporales, causales y comparativas",
    "Proposiciones adverbiales en griego: consecutivas, finales, condicionales y concesivas",
    "Origen de la poesía épica. Homero. Evolución de la épica grecolatina...",
    "Poesía didáctica en el mundo griego. Hesíodo...",
    "Orígenes de la poesía lírica en Grecia. Elegía y yambo...",
    "Lírica monódica y coral en Grecia...",
    "Origen y evolución de la poesía dramática en el mundo clásico...",
    "Esquilo y Sofocles...",
    "Eurípides y la evolución de la tragedia...",
    "Aristófanes y Menandro...",
    "Literatura griega en época helenística...",
    "La historiografía griega: orígenes y primeros cultivadores. Heródoto",
    "Tucídides y Jenofonte. Influjo en la literatura occidental",
    "La historiografía grecolatina posterior a Jenofonte",
    "La novela y la fábula en Grecia...",
    "Oratoria en Grecia: origen y tipos...",
    "Oratoria judicial y oratoria política en Grecia...",
    "Orígenes de la filosofía griega y su evolución hasta el siglo V a. C.",
    "Las teorías filosóficas de los Sofistas, Sócrates y Platón",
    "Aristóteles. Evolución de la filosofía griega...",
    "Los principales autores de la literatura cristiana en lengua griega...",
    "Ciencia y técnica en el mundo griego...",
    "Rasgos generales de la religión griega, su evolución y su pervivencia...",
    "Cosmología, teogonía y antropogonía en el mundo clásico...",
    "Fiestas y juegos en el mundo grecorromano...",
    "Cómputo del tiempo en Grecia. Pesas, medidas y monedas",
    "Los mitos griegos. Principales teorías sobre su función...",
    "Geografía del mundo grecorromano. La economía...",
    "Grecia desde la llegada de los indoeuropeos hasta el siglo XII a. C.; mito e historia",
    "Evolución de Grecia desde el siglo XII hasta el VIII a.C.",
    "Grecia desde el siglo VIII hasta el siglo V a. C. La institución de la polis...",
    "Grecia y Persia en el mundo antiguo",
    "Atenas y Esparta en el siglo V a. C.",
    "El siglo IV a. C. en Grecia hasta Alejandro Magno",
    "Panthelenismo y Alejandro Magno...",
    "Griegos y romanos en Hispania...",
    "Organización político-social de Atenas y Esparta...",
    "Instituciones jurídicas en Grecia...",
    "La vida privada en el mundo grecorromano...",
    "La situación de la mujer en la Grecia antigua...",
    "Arquitectura en el mundo grecorromano...",
    "Urbanismo y vías de comunicación en el mundo grecorromano...",
    "Escultura. Pintura. Cerámica. Mosaico...",
    "Estudio de las fuentes: arqueología, epigrafía, paleografía...",
    "Pervivencia del mundo grecorromano en la historia cultural das Comunidades Autónomas"
]

# Función para calcular a probabilidade
def calcular_probabilidade(temas_totais, temas_estudados, bolas_extraidas):
    if temas_estudados > temas_totais or bolas_extraidas > temas_totais:
        return "Erro: Os valores introducidos non son válidos."
    prob_ningun = stats.hypergeom.pmf(0, temas_totais, temas_estudados, bolas_extraidas)
    prob_polo_menos_uno = 1 - prob_ningun
    return round(prob_polo_menos_uno * 100, 2)

# Configuración da app
st.title("🎯 OpoBombo - Calculadora de probabilidade para oposicións")
st.write("Esta aplicación calcula a probabilidade de que polo menos un dos temas que estudaches saia no exame.")

temas_totais = st.number_input("Número total de temas no temario:", min_value=1, value=68)
temas_estudados = st.number_input("Número de temas que estudaches:", min_value=1, max_value=temas_totais, value=10)
bolas_extraidas = st.number_input("Número de bolas extraídas no exame:", min_value=1, max_value=temas_totais, value=4)

if st.button("📊 Calcular Probabilidade"):
    resultado = calcular_probabilidade(temas_totais, temas_estudados, bolas_extraidas)
    if isinstance(resultado, str):
        st.error(resultado)
    else:
        if resultado < 30:
            color = "red"
            mensaxe = "😟 A probabilidade é baixa, pero non te desanimes! Segue estudando, cada tema conta!"
        elif resultado < 60:
            color = "orange"
            mensaxe = "🙂 Vas por bo camiño! Se aumentas un pouco os temas estudados, terás máis posibilidades!"
        else:
            color = "green"
            mensaxe = "🎉 Estás nunha moi boa posición! Segue así e afronta o exame con confianza!"
        st.markdown(
            f'<div style="background-color:{color}; padding:10px; border-radius:5px; text-align:center;">'
            f'<h2 style="color:white;">Probabilidade: {resultado}%</h2>'
            f'<p style="color:white;">{mensaxe}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

if st.button("🎲 Sortear temas"):
    if bolas_extraidas > temas_totais:
        st.error("Erro: O número de bolas extraídas non pode ser maior que o número total de temas.")
    else:
        temas = list(range(1, temas_totais + 1))
        temas_sorteados = random.sample(temas, bolas_extraidas)
        nomes_sorteados = [f"{n}. {nomes_dos_temas[n-1]}" for n in temas_sorteados]
        st.success("📜 Os temas sorteados son:")
        for nome in nomes_sorteados:
            st.markdown(f"- {nome}")