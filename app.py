import streamlit as st
from datetime import datetime

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Pedro e Hellen",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Configuração de Data e Hora ---
START_DATETIME = datetime(2024, 5, 19, 21, 30)
NOW = datetime.now()

# --- Funções de Cálculo ---
def calculate_time_together(start_dt, end_dt):
    """Calcula o tempo decorrido em anos, meses, dias, horas, minutos, segundos e total de segundos."""
    delta = end_dt - start_dt
    
    total_seconds = int(delta.total_seconds())
    total_minutes = int(total_seconds / 60)
    total_hours = int(total_seconds / 3600)
    total_days = delta.days
    
    years = total_days // 365
    remaining_days = total_days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    
    remaining_seconds = total_seconds - (total_days * 86400)
    hours = int(remaining_seconds // 3600)
    minutes = int((remaining_seconds % 3600) // 60)
    seconds = int(remaining_seconds % 60) # Segundos
    
    # Retorna todos os valores necessários
    return total_days, total_hours, total_minutes, total_seconds, years, months, days, hours, minutes, seconds

# Atualiza a atribuição para incluir 'seconds'
total_days, total_hours, total_minutes, total_seconds, years, months, days, hours, minutes, seconds = calculate_time_together(START_DATETIME, NOW)

# --- Lista de Imagens ---
# Se o carrossel ainda falhar, verifique se alguma dessas imagens abaixo foi renomeada ou apagada na pasta "imagens/".
caminhos_imagens = [
    "imagens/7a28892e-cb49-453a-9857-c3547231de6b.jpg",
    "imagens/0d427601-384a-449d-b935-069468ef3917.jpg",
    "imagens/1c4a86e4-cbcf-4a86-b6fe-30a5d26e4639.jpg",
    "imagens/1ebbab1f-7cd0-4128-a55c-a8e05bffbe6e.jpg",
    "imagens/2a546536-5b83-4a33-95a5-7bc28309e6d1.jpg",
    "imagens/3be387d0-0561-413f-8126-3c8119782ed1.jpg",
    "imagens/4f26d6e8-f6d8-4213-88ac-495b2e9b3175.jpg",
    "imagens/6df69606-e508-4a81-9b3d-abc491b099a0.jpg",
    "imagens/6f906328-f57f-4ea5-8e6d-8f12f74487b7.jpg",
    "imagens/9e264297-7acd-40ac-a8ae-8a2f0cbd339e.jpg",
    "imagens/21d25895-1288-4db2-857d-ed1400973387.jpg",
    "imagens/31b3bf5f-d68a-45fb-9722-2d5e2a3286c7.jpg",
    "imagens/060d5638-8666-45c3-9fc8-c23b642fbed5.jpg",
    "imagens/78b878b6-14a9-4df2-8060-499c939358bf.jpg",
    "imagens/91db3b05-5341-4b97-999d-f685110dc150.jpg",
    "imagens/254edec2-50eb-4e6b-ac36-bce2b88dfaa4.jpg",
    "imagens/a7e2ea93-2876-40e2-98a2-c581bbc93779.jpg",
    "imagens/aa483bbe-4fdf-4c88-bbc0-ec4d07fd4414.jpg",
    "imagens/ae03878a-f795-4a8a-9277-7c52fed6623b.jpg",
    "imagens/b067b0c5-06df-4cb8-bbd3-9e2752e9a809.jpg",
    "imagens/b786514b-5813-430b-a0b2-5322fddb52da.jpg",
    "imagens/b8511401-d3a4-4633-a374-ec9553f291fe.jpg",
    "imagens/image_02c7fd.jpg",
    "imagens/c9653015-c93d-4225-a3b0-db230961ae4c.jpg",
    "imagens/d2284db7-4052-4275-be26-b268fbe9907d.jpg",
    "imagens/ea6ff7bf-8106-4d43-a975-3065bbc3e87d.jpg",
    "imagens/eb8ec612-f16e-4814-85f3-a6a62b78d6a1.jpg",
    "imagens/fb07b5b1-ef6f-4139-9699-c6ea4d7e4131.jpg",
    "imagens/fb514067-0fec-4f7f-9a5b-15541c05f28d.jpg"
]

# --- Inicialização de Estado para o Carrossel ---
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    
def next_image():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(caminhos_imagens)

def prev_image():
    st.session_state.current_index = (st.session_state.current_index - 1 + len(caminhos_imagens)) % len(caminhos_imagens)

if len(caminhos_imagens) == 0:
    st.error("Nenhuma imagem encontrada. Por favor, adicione fotos na pasta 'imagens/'.")
    st.stop()
    
current_image_path = caminhos_imagens[st.session_state.current_index]

# >>> CSS PERSONALIZADO (TEMA PRETO E VERMELHO - Foco no HUD) <<<
st.markdown("""
    <style>
    /* Estilo do corpo e fundo */
    .stApp {
        background-color: #121212; /* Fundo preto ainda mais escuro */
        background-image: radial-gradient(circle at center, #1a1a1a 0%, #0d0d0d 100%);
        color: #F8F8F8; /* Cor do texto padrão (branco suave) */
    }
    /* Estilo do título principal */
    h1.st-emotion-cache-10qzyku { 
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
    .st-emotion-cache-1nj6q9b { 
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
    .metric-total .st-emotion-cache-1nj6q9b {
        /* Garante que o bloco central (Total de Dias) seja grande e não apenas o texto */
        padding: 2.5rem; 
        background-color: #2c0808; /* Um pouco mais escuro para o bloco central */
        border: 3px solid #FF0000; /* Borda Vermelha Pura */
    }
    .metric-total .st-emotion-cache-110u8u9 { 
        font-size: 4.5rem; /* Mantém o tamanho grande */
        color: #FF0000; /* Vermelho puro no valor */
    }
    /* Estilo do rodapé */
    .st-emotion-cache-h4xj1k { 
        color: #A3A3A3;
        text-align: center;
        width: 100%;
        margin-top: 2rem;
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
    .st-emotion-cache-z5rdx0 { /* Botões */
        background-color: #ef4444;
        color: white;
        border-radius: 0.75rem; /* Mais arredondado */
        padding: 0.75rem 1.5rem; /* Maior */
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        border: none; /* Remove borda padrão */
        margin-top: 1rem;
    }
    .st-emotion-cache-z5rdx0:hover {
        background-color: #dc2626;
        transform: translateY(-2px); /* Efeito de "pular" */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Layout da Interface ---

st.title("💖 Pedro e Hellen 💖")
st.markdown(f'<p class="start-date-text">Nossa jornada começou em **{START_DATETIME.strftime("%d/%m/%Y às %H:%M")}**</p>', unsafe_allow_html=True)


# 1. VISÃO GERAL (TODAS AS MÉTRICAS DE TEMPO RELATIVAS - SEM "RESTANTES")
st.header("Tempo Juntos (Visão Geral)")

# Linha 1: Anos, Meses, Dias
col_y, col_m, col_d = st.columns(3)
with col_y: st.metric(label="Anos", value=years)
with col_m: st.metric(label="Meses", value=months)
with col_d: st.metric(label="Dias", value=days) 

# Linha 2: Horas, Minutos, Segundos
col_h, col_min, col_s = st.columns(3)

with col_h: 
    st.metric(label="Horas", value=hours) 

with col_min:
    st.metric(label="Minutos", value=minutes)

with col_s:
    st.metric(label="Segundos", value=seconds)

# BLOCO PARA O TOTAL DE DIAS - DESTAQUE
col_spacer1, col_total, col_spacer2 = st.columns([1, 2, 1])

with col_total:
    # Métrica do total de dias com estilo de destaque
    st.markdown('<div class="metric-total">', unsafe_allow_html=True)
    st.metric(label="Total de Dias (inteiros)", value=f"{total_days:,}".replace(",", "."))
    st.markdown('</div>', unsafe_allow_html=True)

# Adicionando um divisor
st.markdown("""
    <div style="height: 30px;"></div>
    <div style="width: 50%; margin: 0 auto; border-bottom: 2px dashed #7F1D1D;"></div>
    <div style="height: 30px;"></div>
""", unsafe_allow_html=True)

# 2. Carrossel de Fotos
st.subheader("Nossas Memórias Especiais")

# Colunas para os botões (mantendo a proporção original)
col_prev, col_center_buttons, col_next = st.columns([1, 4, 1])
with col_prev: st.button("⬅️ Anterior", on_click=prev_image, use_container_width=True)
with col_next: st.button("Próxima ➡️", on_click=next_image, use_container_width=True)

# Nova estrutura para centralizar e reduzir a imagem (aproximadamente 50% da largura da tela)
# A imagem será colocada na coluna do meio, que é 3/6 (50%) da largura.
col_spacer_l, col_image_narrow, col_spacer_r = st.columns([1.5, 3, 1.5]) 

with col_image_narrow:
    st.image(
        current_image_path, 
        caption=f"Foto {st.session_state.current_index + 1} de {len(caminhos_imagens)}", 
        use_column_width=True # A imagem preenche 100% da sua coluna (que é 50% da tela)
    )

# 3. Rodapé
st.markdown(f"---")
st.caption(f"Data e Hora de Início: **{START_DATETIME.strftime('%d/%m/%Y às %H:%M')}**")
st.caption(f"Total de fotos únicas no carrossel: **{len(caminhos_imagens)}**")
st.caption("Desenvolvido com carinho para o casal.")
