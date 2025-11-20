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

# --- LISTA DE ARQUIVOS ENVIADOS PELO USUÁRIO (DEVE ESTAR NA PASTA 'imagens') ---
IMAGE_FOLDER = "imagens"

# Lista explícita de nomes de arquivos que o usuário enviou.
# É CRUCIAL que o usuário mova/faça o push DESSES arquivos para a pasta 'imagens' no repositório.
UPLOADED_FILENAMES = [
    "21d25895-1288-4db2-857d-ed1400973387.jpg",
    "46473c97-9f73-4f0d-9ef3-0132ea25008e.jpg",
    "3be387d0-0561-413f-8126-3c8119782ed1.jpg",
    "91db3b05-5341-4b97-999d-f685110dc150.jpg",
    "eb8ec612-f16e-4814-85f3-a6a62b78d6a1.jpg",
    "7a28892e-cb49-453a-9857-c3547231de6b.jpg",
    "9e264297-7acd-40ac-a8ae-8a2f0cbd339e.jpg",
    "c9653015-c93d-4225-a3b0-db230961ae4c.jpg",
    "477a557e-3faa-4deb-936f-03483b8a654d.jpg",
    "578ab3ea-698d-4404-9ab1-93cb9180805e.jpg",
    "fb07b5b1-ef6f-4139-9699-c6ea4d7e4131.jpg",
    "254edec2-50eb-4e6b-ac36-bce2b88dfaa4.jpg",
    "ea6ff7bf-8106-4d43-a975-3065bbc3e87d.jpg",
    "fb514067-0fec-4f7f-9a5b-15541c05f28d.jpg",
    "0d427601-384a-449d-b935-069468ef3917.jpg",
    "6df69606-e508-4a81-9b3d-abc491b099a0.jpg",
    "1691e020-b323-43d4-8e49-555a9324f612.jpg",
    "d2284db7-4052-4275-be26-b268fbe9907d.jpg",
    "1ebbab1f-7cd0-4128-a55c-a8e05bffbe6e.jpg",
    "78b878b6-14a9-4df2-8060-499c939358bf.jpg",
    "31b3bf5f-d68a-45fb-9722-2d5e2a3286c7.jpg",
    "060d5638-8666-45c3-9fc8-c23b642fbed5.jpg",
    "WhatsApp Image 2025-11-19 at 20.43.14.jpeg",
]

# Tenta carregar os arquivos da pasta 'imagens' ou usa a lista estática se a pasta for inacessível
image_paths = []
if os.path.exists(IMAGE_FOLDER) and os.path.isdir(IMAGE_FOLDER):
    # Lista os arquivos da pasta local (Streamlit Cloud usará isto se as fotos estiverem lá)
    for filename in sorted(os.listdir(IMAGE_FOLDER)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            image_paths.append(os.path.join(IMAGE_FOLDER, filename))
else:
    # Caso a pasta não seja encontrada, usamos a lista de arquivos enviados como referência de caminho
    # Isso é feito para funcionar no ambiente de desenvolvimento simulado
    image_paths = [os.path.join(IMAGE_FOLDER, filename) for filename in UPLOADED_FILENAMES]

carousel_items = []
if image_paths:
    for i, path in enumerate(image_paths):
        # Usamos o caminho da imagem e um texto simples
        carousel_items.append({
            "image": path,
            "title": f"Nossa Memória {i+1}",
            "text": "Um momento especial",
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
st.subheader("Contagem Detalhada do Nosso Amor!") 

# NOVIDADE: Descrição sobre os números e fotos
st.markdown(
    """
    <p style="text-align: center; color: #aaaaaa; font-size: 1.1em; margin-top: -10px;">
        Contamos cada segundo do nosso relacionamento! Reviva nossas melhores lembranças na galeria de fotos.
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
    
    /* Contêiner de Métricas (Responsável por colocar os boxes lado a lado e agora com destaque) */
    .metric-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap; /* Permite que os boxes quebrem para a próxima linha em telas pequenas */
        margin-top: 30px;
        gap: 20px;
        /* Estilos para destacar o único contador */
        border: 3px solid #D81B60; /* Borda Vermelha */
        border-radius: 10px;
        padding: 20px;
        background-color: #222222;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.4); 
    }
    
    /* Caixa de Cada Métrica */
    .metric-box {
        background-color: #333333; /* Fundo da caixa cinza escuro */
        border-radius: 12px;
        padding: 15px 25px;
        min-width: 120px;
        text-align: center;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        border-bottom: 4px solid #D81B60; /* Linha de destaque vermelha */
        transition: transform 0.2s;
    }
    .metric-box:hover {
        transform: scale(1.05); /* Efeito sutil ao passar o mouse */
        background-color: #444444;
    }
    .metric-value {
        font-size: 3.0em;
        font-weight: 900;
        color: #FF4444; /* Vermelho para os números */
    }
    .metric-label {
        font-size: 0.9em;
        color: #aaaaaa; /* Cinza claro para os rótulos */
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Estilos para o carrossel */
    .stCarousel {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(216, 27, 96, 0.6); /* Sombra vermelha forte para destaque */
        margin-top: 40px;
        margin-bottom: 40px;
    }
    
    /* Cor do texto de informação abaixo do contador */
    .stAlert p {
        color: #dddddd; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"Início do Nosso Amor: **{DATE_OF_START.strftime('%d/%m/%Y às %H:%M:%S')}**")
st.markdown("---")

# --- CARROSSEL ---
# Fix: Removemos o argumento 'height' que estava causando o erro no Streamlit-carousel.
if carousel_items:
    try:
        carousel(items=carousel_items,
                width=1,
                autoplay=True,
                loop=True) 
        st.markdown("---") # Separador após o carrossel
    except Exception as e:
        # Mostra o erro, mas o app continua rodando
        st.error(f"Erro ao exibir carrossel. Verifique seu requirements.txt para garantir que 'streamlit-carousel' esteja instalado e que TODAS as fotos estejam na pasta 'imagens'. Erro: {e}")
        st.markdown("---") 
else:
    st.info("Adicione suas fotos na pasta 'imagens' do seu repositório para exibir o carrossel!")
    st.markdown("---") 


# Inicializa um container vazio que será atualizado a cada segundo
placeholder = st.empty()

# O loop 'while True' permite a atualização em tempo real do contador.
while True:
    years, months, days_only, h, m, s, total_seconds = calculate_duration(DATE_OF_START)

    with placeholder.container():
        
        # Métrica detalhada em uma grade responsiva
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)

        # Anos
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{years}</div>
            <div class="metric-label">Anos</div>
        </div>
        """, unsafe_allow_html=True)

        # Meses
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{months}</div>
            <div class="metric-label">Meses</div>
        </div>
        """, unsafe_allow_html=True)

        # Dias
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{days_only}</div>
            <div class="metric-label">Dias Restantes</div>
        </div>
        """, unsafe_allow_html=True)

        # Horas
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{h:02}</div>
            <div class="metric-label">Horas</div>
        </div>
        """, unsafe_allow_html=True)

        # Minutos
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{m:02}</div>
            <div class="metric-label">Minutos</div>
        </div>
        """, unsafe_allow_html=True)

        # Segundos
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{s:02}</div>
            <div class="metric-label">Segundos</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Espera 1 segundo antes de recalcular e atualizar a tela
    time.sleep(1)
