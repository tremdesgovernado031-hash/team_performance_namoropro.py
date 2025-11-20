import streamlit as st
from datetime import datetime
import time
import math
import os
# Linha que causa o erro: A biblioteca 'streamlit-carousel' PRECISA estar no requirements.txt
from streamlit_carousel import carousel 

# --- CONFIGURAÇÃO INICIAL (O USUÁRIO DEVE ALTERAR ESTA DATA) ---
# Altere o ano, mês, dia, hora e minuto para a data exata do início do namoro.
# Exemplo: datetime(Ano, Mês, Dia, Hora, Minuto, Segundo)
DATE_OF_START = datetime(2023, 10, 27, 18, 30, 0)
# ----------------------------------------------------------------

# --- CARREGANDO IMAGENS DA PASTA LOCAL 'imagens' ---
IMAGE_FOLDER = "imagens"
image_paths = []

if os.path.exists(IMAGE_FOLDER) and os.path.isdir(IMAGE_FOLDER):
    for filename in sorted(os.listdir(IMAGE_FOLDER)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            image_paths.append(os.path.join(IMAGE_FOLDER, filename))
else:
    st.warning(f"A pasta '{IMAGE_FOLDER}' não foi encontrada. Certifique-se de que ela está no seu repositório GitHub.")

carousel_items = []
if image_paths:
    for i, path in enumerate(image_paths):
        carousel_items.append({
            "image": path,
            "title": f"Nossa Memória {i+1}",
            "text": f"Momento especial {i+1} do nosso namoro",
            "interval": 3000 # 3 segundos para cada slide
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

    # Aproximação para anos e meses
    DAYS_IN_YEAR = 365.2425
    DAYS_IN_MONTH = 30.4375

    years = math.floor(total_days / DAYS_IN_YEAR)
    days_after_years = total_days - math.floor(years * DAYS_IN_YEAR)
    months = math.floor(days_after_years / DAYS_IN_MONTH)
    days_only = math.floor(days_after_years - (months * DAYS_IN_MONTH))

    return years, months, days_only, h, m, s, total_seconds

# Configuração da página Streamlit
st.set_page_config(
    page_title="Contador de Namoro",
    page_icon="💖",
    layout="centered",
)

st.title("💖 Contador do Nosso Amor 💖")
st.subheader("O Tempo Voa Quando Estamos Juntos!")

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    /* Estilos para o Contador (mantidos do design anterior) */
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #FF69B4;
        text-align: center;
        margin: 15px 0 25px 0;
        padding: 10px;
        border: 2px solid #D81B60;
        border-radius: 10px;
        background-color: #fff0f5;
        box-shadow: 0 4px 10px rgba(255, 105, 180, 0.4);
    }
    .metric-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 30px;
        gap: 20px;
    }
    .metric-box {
        background-color: #ffe4e1;
        border-radius: 12px;
        padding: 15px 25px;
        min-width: 120px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s;
    }
    .metric-box:hover {
        transform: translateY(-5px);
    }
    .metric-value {
        font-size: 3.0em;
        font-weight: 900;
        color: #D81B60;
    }
    .metric-label {
        font-size: 0.9em;
        color: #555;
        margin-top: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    /* Estilos para o carrossel */
    .stCarousel {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        margin-top: 40px;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"Início do Nosso Amor: **{DATE_OF_START.strftime('%d/%m/%Y às %H:%M:%S')}**")
st.markdown("---")

# Exibindo o carrossel de fotos (se houver imagens)
if carousel_items:
    try:
        carousel(items=carousel_items,
                width=1, # Usa a largura máxima do contêiner centralizado
                height=400,
                autoplay=True,
                loop=True) # O intervalo é definido dentro de cada item
    except Exception as e:
        # Se o carrossel falhar (provavelmente a biblioteca não foi instalada), exibe um erro amigável.
        st.error(f"Erro ao exibir carrossel (A biblioteca 'streamlit-carousel' pode não estar instalada. Verifique seu requirements.txt): {e}")
    st.markdown("---")
else:
    st.error("Nenhuma imagem encontrada na pasta 'imagens' ou a pasta não existe. Adicione suas fotos lá!")


# Inicializa um container vazio que será atualizado a cada segundo
placeholder = st.empty()

# O loop 'while True' permite a atualização em tempo real do contador.
# (Em Streamlit Cloud, o loop pode ter pausas devido à política de recursos)
while True:
    years, months, days_only, h, m, s, total_seconds = calculate_duration(DATE_OF_START)

    with placeholder.container():
        # Métrica principal: Anos, Meses e Dias
        st.markdown(
            f'<div class="big-font">Estamos juntos há: <br> {years} anos, {months} meses e {days_only} dias!</div>',
            unsafe_allow_html=True
        )

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

        st.markdown("---")
        st.info(f"O total de segundos do nosso amor é de aproximadamente: **{total_seconds:,}**")

    # Espera 1 segundo antes de recalcular e atualizar a tela
    time.sleep(1)
