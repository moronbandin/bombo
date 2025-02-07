import streamlit as st
import scipy.stats as stats

# Función para calcular la probabilidad de que al menos un tema estudiado salga en el examen
def calcular_probabilidad(total_temas, temas_estudiados, bolas_extraidas):
    """
    Calcula la probabilidad de que al menos uno de los temas estudiados salga en el examen.

    :param total_temas: Número total de temas en el temario.
    :param temas_estudiados: Número de temas estudiados.
    :param bolas_extraidas: Número de bolas extraídas en el examen.
    :return: Probabilidad en porcentaje.
    """
    if temas_estudiados > total_temas or bolas_extraidas > total_temas:
        return "Error: Los valores ingresados no son válidos."
    
    # Probabilidad de que ninguno de los temas estudiados salga en el examen
    prob_ninguno = stats.hypergeom.pmf(0, total_temas, temas_estudiados, bolas_extraidas)
    # Probabilidad de que al menos uno sí salga
    prob_al_menos_uno = 1 - prob_ninguno
    # Convertir a porcentaje
    return round(prob_al_menos_uno * 100, 2)

# Configuración de la app en Streamlit
st.title("Calculadora de Probabilidad para Exámenes de Oposición")
st.write("Esta aplicación calcula la probabilidad de que al menos uno de los temas que has estudiado salga en el examen.")

# Inputs del usuario
total_temas = st.number_input("Número total de temas en el temario:", min_value=1, value=68)
temas_estudiados = st.number_input("Número de temas que has estudiado:", min_value=1, max_value=total_temas, value=10)
bolas_extraidas = st.number_input("Número de bolas extraídas en el examen:", min_value=1, max_value=total_temas, value=4)

# Botón para calcular la probabilidad
if st.button("Calcular Probabilidad"):
    resultado = calcular_probabilidad(total_temas, temas_estudiados, bolas_extraidas)
    
    if isinstance(resultado, str):
        st.error(resultado)
    else:
        st.success(f"La probabilidad de que salga al menos un tema estudiado es de {resultado}%.")

# Información adicional
st.info("🔹 Usa esta herramienta para planificar tu estudio y aumentar tus posibilidades de éxito en el examen.")
