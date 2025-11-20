import streamlit as st
from datetime import datetime
import math
import os

# =========================================================================
# 1. CONFIGURAÇÃO E DADOS
# =========================================================================

# Ajuste a data e hora do início do namoro aqui! (Ano, Mês, Dia, Hora, Minuto, Segundo)
START_DATE = datetime(2024, 5, 19, 21, 40, 0) 
TITLE = "Pedro & Hellen ❤️" # Altere o título principal
SUBTITLE = "Juntos desde" # O subtítulo que aparece antes da data

# LISTA DE CAMINHOS LOCAIS PARA AS FOTOS
# CRIE UMA PASTA CHAMADA 'images' no SEU REPOSITÓRIO e coloque suas fotos lá.
# O nome do arquivo aqui DEVE ser o mesmo nome do arquivo na pasta 'images/'.
PHOTOS = [
    'images/foto_01.jpg',
    'images/foto_02.jpg',
    'images/foto_03.jpg',
    'images/foto_04.jpg',
    'images/foto_05.jpg',
    # Adicione mais fotos (seus nomes de arquivo reais) aqui:
    # 'images/meu_arquivo.png',
]

# =========================================================================
# 2. FUNÇÕES DE CÁLCULO
# =========================================================================

def calculate_time_components(start_date, now):
    """Calcula a diferença de tempo em anos, meses, dias, horas, minutos e segundos."""
    
    time_difference = now - start_date
    total_seconds = int(time_difference.total_seconds())

    # Componentes para o contador (contagem total e progressiva)
    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // (60 * 60)) % 24
    total_days = total_seconds // (60 * 60 * 24)
    
    # Cálculo de anos e meses (baseado em data para maior precisão)
    years = now.year - start_date.year
    months = now.month - start_date.month
    days_partial = now.day - start_date.day

    if days_partial < 0:
        months -= 1
        # Aproximação do número de dias no mês anterior para um cálculo simples
        days_partial += 30 
        
    if months < 0:
        years -= 1
        months += 12

    return {
        'years': years,
        'months': months,
        'total_days': total_days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

# =========================================================================
# 3. INTERFACE DO STREAMLIT
# =========================================================================

# Configuração da página e tema escuro
st.set_page_config(
    page_title=TITLE,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeção de CSS para o tema preto/vermelho (Tailwind-like classes)
st.markdown("""
    <style>
    /* Estilo do corpo e fundo */
    .stApp {
        background-color: #1a1a1a; /* Fundo preto escuro */
        background-image: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); 
        color: #FF6347;
    }
    /* Estilo do título principal */
    .title-text {
        font-family: 'Inter', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        color: #ef4444; /* Vermelho forte */
        text-align: center;
        margin-bottom: 0.5rem;
    }
    /* Estilo do subtítulo/data */
    .subtitle-text {
        font-size: 1.5rem;
        color: #fca5a5; /* Vermelho claro */
        font-style: italic;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Estilo dos contadores */
    .counter-box {
        background-color: #262626; /* Cinza escuro */
        border-radius: 1rem;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        border: 2px solid #b91c1c; /* Borda vermelha escura */
        transition: all 0.3s ease;
    }
    .counter-value {
        font-size: 3rem;
        font-weight: 800;
        color: #f87171; /* Vermelho vibrante */
    }
    .counter-label {
        font-size: 0.9rem;
        font-weight: 600;
        color: #fca5a5;
        margin-top: 0.25rem;
    }
    /* Estilo da seção da galeria */
    .gallery-title {
        font-size: 2rem;
        font-weight: 700;
        color: #f87171;
        border-bottom: 2px solid #b91c1c;
        padding-bottom: 0.5rem;
        margin-top: 4rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .stImage > img {
        border-radius: 1rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        object-fit: cover;
        width: 100%;
        min-height: 200px;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    # 1. Título e Subtítulo
    st.markdown(f'<div class="title-text">{TITLE}</div>', unsafe_allow_html=True)
    start_date_formatted = START_DATE.strftime("%d/%m/%Y às %H:%M")
    st.markdown(f'<div class="subtitle-text">{SUBTITLE} {start_date_formatted}!</div>', unsafe_allow_html=True)
    
    # 2. Título do Contador
    st.markdown('<h2 style="text-align: center; color: #f87171;">Tempo de Namoro</h2>', unsafe_allow_html=True)

    # Cálculo do tempo atual
    now = datetime.now()
    time_data = calculate_time_components(START_DATE, now)

    # Função auxiliar para exibir o componente
    def display_counter(column, value, label):
        # Adiciona zero à esquerda para Horas, Minutos e Segundos
        formatted_value = str(value).zfill(2) if label in ['Horas', 'Minutos', 'Segundos'] else str(value)
        with column:
            st.markdown(f"""
                <div class="counter-box">
                    <div class="counter-value">{formatted_value}</div>
                    <div class="counter-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

    # Exibição do Contador em Colunas
    # Usa 6 colunas para exibir Anos, Mes