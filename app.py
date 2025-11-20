import streamlit as st
from datetime import datetime
import time
import math
import os
from streamlit_carousel import carousel 

# --- CONFIGURAÇÃO INICIAL (DATA E HORA DO NAMORO) ---
# Namoro começou em 19/05/2024 às 21:30:00
DATE_OF_START = datetime(2024, 5, 19, 21, 30, 0)
# ----------------------------------------------------------------

# --- CARREGANDO IMAGENS DA PASTA LOCAL 'imagens' ---
IMAGE_FOLDER = "imagens"
image_paths = []

# O Streamlit Cloud executa este código. Ele PRECISA encontrar a pasta 'imagens' no repositório.
if os.path.exists(IMAGE_FOLDER) and os.path.isdir(IMAGE_FOLDER):
    # Lista os arquivos, ordenados por nome para ter uma ordem consistente
    for filename in sorted(os.listdir(IMAGE_FOLDER)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            # Adiciona o caminho completo da imagem (ex: imagens/foto1.jpg)
            image_paths.append(os.path.join(IMAGE_FOLDER, filename))
else:
    # Aviso caso a pasta não seja encontrada
    st.warning(f"A pasta '{IMAGE_FOLDER}' não foi encontrada. O carrossel não será exibido. Certifique-se de que ela está no seu repositório GitHub.")

carousel_items = []
if image_paths:
    for i, path in enumerate(image_paths):
        carousel_items.append({
            "image": path,
            "title": f"Nossa Memória {i+1}",
            "text": f"Momento especial {i+1} de Pedro e Hellen",
            "interval": 3000
        })
# ------------------------------------------------------------------------------

def calculate_duration(start_date):
    """Calcula a duração e a decompõe em anos, meses, dias, horas, minutos e segundos."""
    now = datetime.now()
    duration = now - start_date

    total_seconds = int(duration.total_seconds())

    s = total_seconds % 60
    m = (total_seconds // 60) % 60
    h = (total_seconds // 3600) % 24
    total_days = total_seconds // 86400

    # Aproximação para anos e meses (abordagem comum em contadores)
    DAYS_IN_YEAR = 365.2425
    DAYS_IN_MONTH = 30.4375

    years = math.floor(total_days / DAYS_IN_YEAR)
    days_after_years = total_days - math.floor(years * DAYS_IN_YEAR)
    months = math.floor(days_after_years / DAYS_IN_MONTH)
    days_only = math.floor(days_after_years - (months * DAYS_IN_MONTH))

    return years, months, days_only, h, m, s, total_seconds

# Configuração da página Streamlit
st.set_page_config(
    page_title="Pedro e Hellen",
    page_icon="❤️",
    layout="centered",
)

st.title("❤️ Pedro e Hellen ❤️")
st.subheader("O Nosso Amor em Números!")

# NOVIDADE: Descrição sobre os números e fotos
st.markdown(
    """
    <p style="text-align: center; color: #aaaaaa; font-size: 1.1em; margin-top: -10px;">
        Contamos cada segundo do nosso relacionamento. Veja a linha do tempo abaixo e, em seguida,
        reviva nossas melhores lembranças na galeria de fotos!
    </p>
    """,
    unsafe_allow_html=True
)


# Estilos CSS personalizados (Preto e Vermelho)
st.markdown(
    """
    <style>
    /* Fundo escuro sutil e texto principal claro */
    .stApp {
        background-color: #111111; /* Fundo do app */
    }
    h1, h2, h3, h4, .stMarkdown {
        color: #ffffff;
    }
    
    /* Contador Principal (Fundo Preto com Borda Vermelha) */
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #D81B60; /* Vermelho Principal */
        text-align: center;
        margin: 15px 0 25px 0;
        padding: 15px;
        border: 3px solid #D81B60; /* Borda Vermelha */
        border-radius: 10px;
        background-color: #222222; /* Fundo levemente cinza/preto */
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.4); /* Sombra Vermelha */
    }
    
    /* Contêiner de Métricas (Responsável por colocar os boxes lado a lado) */
    .metric
