import streamlit as st
from datetime import datetime
import math
import os
import time # Importação necessária para o st.rerun

# =========================================================================
# 1. CONFIGURAÇÃO E DADOS
# =========================================================================

# Ajuste a data e hora do início do namoro aqui! (Ano, Mês, Dia, Hora, Minuto, Segundo)
# Exemplo: 19 de Maio de 2024 às 21:40:00
START_DATE = datetime(2024, 5, 19, 21, 40, 0) 
TITLE = "Pedro & Hellen ❤️" # Altere o título principal
SUBTITLE = "Juntos desde" # O subtítulo que aparece antes da data

# LISTA DE CAMINHOS LOCAIS PARA AS FOTOS
# ATENÇÃO: O Streamlit irá procurar estas fotos na pasta 'imagens/'
# Esta lista foi ajustada para corresponder à sua pasta no GitHub.
PHOTOS = [
    'imagens/3be387d0-0561-413f-8126-3c8119782ed1.jpg',
    'imagens/6df69606-e508-4a81-9b3d-abc491b099a0.jpg',
    'imagens/4f26d6e8-f6d8-4213-88ac-495b2e9b3175.jpg',
    'imagens/1c4a86e4-cbcf-4a86-b6fe-30a5d26e4639.jpg',
    'imagens/2a546536-5b83-4a33-95a5-7bc28309e6d1.jpg',
    'imagens/7a28892e-cb49-453a-9857-c3547231de6b.jpg',
    'imagens/1ebbab1f-7cd0-4128-a55c-a8e05bffbe6e.jpg',
    'imagens/0d427601-384a-449d-b935-069468ef3917.jpg', 
    'imagens/6f906328-f57f-4ea5-8e6d-8f12f74487b7.jpg',
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
    /* O Streamlit utiliza divs específicas que podemos estilizar */
    div[data-testid="stVerticalBlock"] > div:first-child {
        margin-bottom: 0;
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
        # Usa total_days em vez de dias_parciais para o contador principal
        formatted_value = str(value).zfill(2) if label in ['Horas', 'Minutos', 'Segundos'] else str(value)
        with column:
            st.markdown(f"""
                <div class="counter-box">
                    <div class="counter-value">{formatted_value}</div>
                    <div class="counter-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

    # Exibição do Contador em Colunas
    # Usa 6 colunas para exibir Anos, Meses, Dias, Horas, Minutos, Segundos
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    # Nota: No display de dias, usamos 'total_days' para mostrar a contagem total de dias.
    display_counter(col1, time_data['years'], 'Anos')
    display_counter(col2, time_data['months'], 'Meses')
    display_counter(col3, time_data['total_days'], 'Dias Totais')
    display_counter(col4, time_data['hours'], 'Horas')
    display_counter(col5, time_data['minutes'], 'Minutos')
    display_counter(col6, time_data['seconds'], 'Segundos')

    # 3. Galeria de Fotos
    st.markdown('<div class="gallery-title">Nossas Memórias</div>', unsafe_allow_html=True)
    
    # Filtra apenas fotos que realmente existem localmente (importante para o deploy no Streamlit)
    available_photos = [p for p in PHOTOS if os.path.exists(p)]
    
    if available_photos:
        # Define 3 colunas para a galeria
        cols_gallery = st.columns(3)
        
        for i, photo_path in enumerate(available_photos):
            col_index = i % 3 # Alterna entre as 3 colunas (0, 1, 2, 0, 1, 2...)
            with cols_gallery[col_index]:
                try:
                    # Carrega a imagem
                    st.image(photo_path, use_column_width=True)
                except Exception as e:
                    # Mensagem de fallback caso a imagem não seja carregada no deploy
                    # st.warning(f"Não foi possível carregar a imagem: {photo_path}") # Comentei para evitar poluição visual
                    pass 
    else:
        # Mensagem se as fotos não forem encontradas (o que geralmente acontece antes do push para o GitHub)
        st.info("A galeria de fotos estará visível após você enviar a pasta `imagens/` e o arquivo `app.py` corrigido para o GitHub e fazer o deploy no Streamlit Cloud.")


if __name__ == '__main__':
    # Esta linha executa a aplicação
    main()
    
    # Configuração de 'st.rerun' para atualizar o contador a cada 1 segundo.
    time.sleep(1) 
    st.rerun()
