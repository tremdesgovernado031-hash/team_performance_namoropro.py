import streamlit as st
from datetime import datetime, timedelta
import time

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Pedro e Hellen",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Configuração de Data e Hora ---
# A data de início do relacionamento
START_DATETIME = datetime(2024, 5, 19, 21, 30)

# --- Funções de Cálculo ---
def calculate_time_together(start_dt, end_dt):
    """Calcula o tempo decorrido em anos, meses, dias, horas, minutos, segundos e total de segundos."""
    delta = end_dt - start_dt
    
    # Se a data de término for anterior à data de início (caso improvável, mas para segurança)
    if delta.total_seconds() < 0:
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    total_seconds = int(delta.total_seconds())
    total_days = delta.days
    
    # 1. Cálculo de Anos, Meses, Dias (Aproximado para exibição)
    years = total_days // 365
    remaining_days = total_days % 365
    months = remaining_days // 30
    days = remaining_days % 30 

    # 2. Cálculo de Horas, Minutos, Segundos (Exato no dia atual)
    # Recalcula a diferença exata de tempo (horas, minutos, segundos) após os dias completos
    remaining_seconds_in_day = total_seconds % 86400 
    
    hours = remaining_seconds_in_day // 3600
    minutes = (remaining_seconds_in_day % 3600) // 60
    seconds = remaining_seconds_in_day % 60
    
    total_hours = total_seconds // 3600
    total_minutes = total_seconds // 60
    
    # Retorna todos os valores necessários
    return total_days, total_hours, total_minutes, total_seconds, years, months, days, hours, minutes, seconds

# --- Lista de Imagens ---
# IMPORTANTE: Por favor, substitua a imagem de placeholder abaixo 
# por todos os caminhos das suas fotos.
caminhos_imagens = [
    # Adicione aqui os caminhos das suas fotos!
    "https://placehold.co/800x600/7F1D1D/FFFFFF?text=ADICIONE+AS+SUAS+FOTOS+AQUI", 
    "https://placehold.co/800x600/FF4500/FFFFFF?text=SEGUNDA+FOTO+DE+MEM%C3%93RIA", 
    "https://placehold.co/800x600/DC2626/FFFFFF?text=TERCEIRA+FOTO+ESPECIAL", 
]

# --- Inicialização de Estado para o Carrossel ---
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    
def next_image():
    if len(caminhos_imagens) > 0:
        st.session_state.current_index = (st.session_state.current_index + 1) % len(caminhos_imagens)

def prev_image():
    if len(caminhos_imagens) > 0:
        st.session_state.current_index = (st.session_state.current_index - 1 + len(caminhos_imagens)) % len(caminhos_imagens)

if len(caminhos_imagens) == 0:
    st.error("Nenhuma imagem encontrada. Por favor, adicione caminhos de fotos na lista 'caminhos_imagens'.")
    st.stop()
    
current_image_path = caminhos_imagens[st.session_state.current_index]

# >>> CSS PERSONALIZADO (TEMA PRETO E VERMELHO - Foco no HUD) <<<
# O seletor h1.st-emotion-cache-10qzyku foi alterado para o seletor mais genérico h1
st.markdown("""
    <style>
    /* Estilo do corpo e fundo */
    .stApp {
        background-color: #121212; /* Fundo preto ainda mais escuro */
        background-image: radial-gradient(circle at center, #1a1a1a 0%, #0d0d0d 100%);
        color: #F8F8F8; /* Cor do texto padrão (branco suave) */
    }
    /* Estilo do título principal */
    h1 { 
        font-family: 'Inter', sans-serif;
        font-size: 5rem; /* Título GIGANTE */
        font-weight: 900;
        color: #FF0000; /* Vermelho puro */
        text-align: center;
        text-shadow: 0 0 15px rgba(255, 0, 0, 0.7); /* Efeito de brilho */
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    /* Estilo do subtítulo de início */
    .start-date-text {
        text-align: center;
        color: #FCA5A5; /* Vermelho claro */
        font-style: italic;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 500;
    }
    /* Estilo do st.header (Contadores) */
    h2 {
        color: #EF4444; /* Vermelho forte */
        text-align: center;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
        border-bottom: 1px solid rgba(255, 0, 0, 0.2);
        padding-bottom: 0.5rem;
    }
    /* Estilo dos contadores (st.metric) - o novo HUD */
    .st-emotion-cache-1nj6q9b { /* Seletor do container do st.metric */
        background-color: #1e1e1e; /* Cinza bem escuro para o bloco */
        border-radius: 1.5rem;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.2); /* Sombra suave vermelha */
        border: 3px solid #7F1D1D; /* Borda vermelha escura */
        transition: all 0.4s ease;
        margin: 1rem 0;
    }
    .st-emotion-cache-1nj6q9b:hover {
        transform: scale(1.05); /* Pequeno zoom ao passar o mouse */
        box-shadow: 0 0 30px rgba(255, 0, 0, 0.5);
    }
    .st-emotion-cache-q18a8y { /* Label do st.metric (Anos, Meses, Dias...) */
        font-size: 1rem;
        font-weight: 700;
        color: #FFCDD2; /* Vermelho clarinho */
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .st-emotion-cache-110u8u9 { /* Value do st.metric (O número grande) */
        font-size: 4.5rem; /* O MAIOR TAMANHO */
        font-weight: 900;
        color: #FF4500; /* Laranja avermelhado vibrante */
        line-height: 1;
        margin-top: 0.5rem;
    }
    /* Estilo para a métrica Total de Dias (destaque) */
    /* Uso de !important e seletores mais específicos para sobrescrever */
    .metric-total .st-emotion-cache-1nj6q9b {
        padding: 2.5rem; 
        background-color: #2c0808; /* Um pouco mais escuro para o bloco central */
        border: 3px solid #FF0000; /* Borda Vermelha Pura */
    }
    .metric-total .st-emotion-cache-110u8u9 { 
        font-size: 4.5rem; /* Mantém o tamanho grande */
        color: #FF0000; /* Vermelho puro no valor */
    }
    /* Estilo do rodapé */
    .footer-text { 
        color: #A3A3A3;
        text-align: center;
        width: 100%;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid rgba(255, 0, 0, 0.1);
    }
    /* Estilo da imagem no carrossel */
    .stImage > img {
        border-radius: 1rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        object-fit: cover;
        width: 100%;
        min-height: 200px;
        margin-top: 2rem; /* Espaçamento da foto do contador */
        border: 2px solid #ef4444; /* Borda vermelha na foto */
    }
    /* Botões do carrossel */
    .stButton > button {
        background-color: #ef4444;
        color: white;
        border-radius: 0.75rem; /* Mais arredondado */
        padding: 0.75rem 1.5rem; /* Maior */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        border: none; /* Remove borda padrão */
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #dc2626;
        transform: translateY(-2px); /* Efeito de "pular" */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Layout da Interface ---

# Recalcula o tempo para garantir que a interface sempre use a hora mais recente
NOW = datetime.now()
total_days, total_hours, total_minutes, total_seconds, years, months, days, hours, minutes, seconds = calculate_time_together(START_DATETIME, NOW)

st.title("Pedro & Hellen")
st.markdown(
    f'<p class="start-date-text">Juntos desde: {START_DATETIME.strftime("%d de %B de %Y, %H:%M:%S")}</p>', 
    unsafe_allow_html=True
)

# 1. Contadores Primários (Anos, Meses, Dias)
st.header("Tempo de Namoro")

col_y, col_m, col_d = st.columns(3)
with col_y:
    st.metric(label="Anos", value=years)
with col_m:
    st.metric(label="Meses", value=months)
with col_d:
    st.metric(label="Dias (Aprox.)", value=days)

# 2. Total de Dias (Destaque Central)
# Usando um markdown container para aplicar a classe 'metric-total'
st.markdown('<div class="metric-total">', unsafe_allow_html=True)
st.metric(label="Total de Dias", value=total_days)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Contadores Secundários (Horas, Minutos, Segundos - Exatos)
st.header("Detalhes Milissegundos")

# Criamos um placeholder para o tempo exato para que possamos atualizá-lo
# Mesmo que o loop de rerun esteja no final, usamos o placeholder para manter o layout
time_placeholder = st.empty()

with time_placeholder.container():
    col_h, col_min, col_sec = st.columns(3)

    with col_h:
        st.metric(label="Horas", value=hours)
    with col_min:
        st.metric(label="Minutos", value=minutes)
    with col_sec:
        st.metric(label="Segundos", value=seconds)
    
    # 4. Total Geral (abaixo do tempo exato)
    st.markdown('<br>', unsafe_allow_html=True) # Espaçamento
    # Formata com ponto como separador de milhares para melhor leitura (1.234.567)
    st.metric(label="Total de Segundos Vivos", value=f"{total_seconds:,}".replace(",", "."))


# 5. Carrossel de Fotos
st.header("Nossas Memórias")

# Cria colunas para centralizar a imagem e os botões
col_space_l, col_img_center, col_space_r = st.columns([1, 4, 1])

with col_img_center:
    st.image(current_image_path, use_column_width=True, caption=f"Foto {st.session_state.current_index + 1} de {len(caminhos_imagens)}")
    
# Cria colunas para os botões Anterior/Próximo
col_btn1, col_btn_space, col_btn2 = st.columns([1, 3, 1])

with col_btn1:
    st.button("❮ Anterior", on_click=prev_image, use_container_width=True)

with col_btn2:
    st.button("Próximo ❯", on_click=next_image, use_container_width=True)

# 6. Rodapé
st.markdown('<p class="footer-text">Feito com ♥ por Pedro e Hellen</p>', unsafe_allow_html=True)

# 7. Loop de Atualização em Tempo Real
# Faz o script ser executado a cada 1 segundo para atualizar o contador
time.sleep(1) 
st.rerun()
