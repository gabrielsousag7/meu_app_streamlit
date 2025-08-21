import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analisador de Jogos - Beta", layout="centered")

st.title("⚽ Analisador de Jogos - Beta")

st.subheader("📥 Insira suas estatísticas aqui:")

# -------------------------------
# Campos de entrada
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    g1 = st.number_input("Média de gols do Time 1", min_value=0.0, step=0.1)
    e1 = st.number_input("Escanteios médios do Time 1", min_value=0.0, step=0.1)
    f1 = st.number_input("Finalizações do Time 1", min_value=0.0, step=0.1)
    ca1 = st.number_input("Cartões Amarelos - Time 1", min_value=0.0, step=0.1)
    cv1 = st.number_input("Cartões Vermelhos - Time 1", min_value=0.0, step=0.1)

with col2:
    g2 = st.number_input("Média de gols do Time 2", min_value=0.0, step=0.1)
    e2 = st.number_input("Escanteios médios do Time 2", min_value=0.0, step=0.1)
    f2 = st.number_input("Finalizações do Time 2", min_value=0.0, step=0.1)
    ca2 = st.number_input("Cartões Amarelos - Time 2", min_value=0.0, step=0.1)
    cv2 = st.number_input("Cartões Vermelhos - Time 2", min_value=0.0, step=0.1)

# -------------------------------
# Análise simples (Beta)
# -------------------------------
if st.button("🔎 Analisar Jogo"):
    st.subheader("📊 Resultado da Análise")

    # Probabilidade de gols (bem simplificada)
    media_gols = (g1 + g2) / 2
    if media_gols >= 2.5:
        st.write("👉 Tendência para **Over 2.5 gols**")
    elif media_gols >= 1.5:
        st.write("👉 Tendência para **Over 1.5 gols**")
    else:
        st.write("👉 Jogo com poucos gols (Under)")

    # Ambas marcam
    if g1 >= 1 and g2 >= 1:
        st.write("👉 Alta chance de **Ambas Marcam (BTTS)**")
    else:
        st.write("👉 Risco de apenas 1 marcar")

    # Escanteios
    media_esc = (e1 + e2) / 2
    if media_esc >= 9:
        st.write("👉 Tendência de **muitos escanteios (+9.5)**")
    else:
        st.write("👉 Escanteios medianos")

    # Finalizações
    if f1 >= 10 or f2 >= 10:
        st.write("👉 Pelo menos um time finaliza bastante, chance de gols")

    # Cartões
    if (ca1 + ca2) >= 4 or (cv1 + cv2) > 0:
        st.write("👉 Jogo **quente**, tendência de cartões")

    # Resumão
    st.success("✅ Análise gerada! Use com cautela (versão Beta)")
