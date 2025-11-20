import streamlit as st
import os
from datetime import datetime, timedelta

# --- Configurações Iniciais ---
st.set_page_config(
    page_title="Pedro e Hellen",
    layout="wide", # Layout wide para melhor aproveitamento do espaço
    initial_sidebar_state="collapsed" # Esconde a sidebar padrão do streamlit
)

# >>> CSS PERSONALIZADO (TEMA PRETO E VERMELHO) <<<
st.markdown("""
    <style>
    /* Estilo do corpo e fundo */
    .stApp {
        background-color: #1a1a1a; /* Fundo preto escuro */
        background-image: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%); 
        color: #FF6347; /* Cor do texto padrão */
    }
    /* Estilo do título principal */
    .st-emotion-cache-10qzyku { /* Classe do st.title */
        font-family: 'Inter', sans-serif;
        font-size: 4rem; /* Tamanho maior */
        font-weight: 800;
        color: #ef4444; /* Vermelho forte */
        text-align: center;
        margin-bottom: 0.5rem;
    }
    /* Estilo do st.header e st.subheader */
    h1, h2, h3 {
        color: #f87171; /* Vermelho mais suave */
        text-align: center;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    /* Estilo dos contadores (st.metric) */
    .st-emotion-cache-1nj6q9b { /* Contêiner do st.metric */
        background-color: #262626; /* Cinza escuro */
        border-radius: 1rem;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        border: 2px solid #b91c1c; /* Borda vermelha escura */
        transition: all 0.3s ease;
    }
    .st-emotion-cache-1nj6q9b:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }
    .st-emotion-cache-q18a8y { /* Label do st.metric */
        font-size: 0.9rem;
        font-weight: 600;
        color: #fca5a5; /* Vermelho claro */
        margin-top: 0.25rem;
    }
    .st-emotion-cache-110u8u9 { /* Value do st.metric */
        font-size: 3rem; /* Tamanho maior */
        font-weight: 800;
        color: #f87171; /* Vermelho vibrante */
    }
    /* Estilo do rodapé */
    .st-emotion-cache-h4xj1k { /* st.caption */
        color: #fca5a5;
        text-align: center;
        width: 100%;
    }
    /* Estilo da imagem no carrossel */
    .stImage > img {
        border-radius: 1rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        object-fit: cover;
        width: 100%;
        min-height: 200px;
    }
    /* Botões do carrossel */
    .st-emotion-cache-z5rdx0 { /* Botões */
        background-color: #ef4444;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .st-emotion-cache-z5rdx0:hover {
        background-color: #dc2626;
        color: white;
    }
    /* Centralizar o subtítulo e o total de dias */
    .centered-text {
        text-align: center;
        color: #fca5a5;
        font-style: italic;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Configuração de Data e Hora ---
START_DATETIME = datetime(2024, 5, 19, 21, 30)
NOW = datetime.now()

# --- Funções de Cálculo ---
def calculate_time_together(start_dt, end_dt):
    """Calcula o tempo decorrido em anos, meses, dias, horas e minutos."""
    delta = end_dt - start_dt
    
    total_seconds = delta.total_seconds()
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
    
    return total_days, total_hours, total_minutes, years, months, days, hours, minutes

total_days, total_hours, total_minutes, years, months, days, hours, minutes = calculate_time_together(START_DATETIME, NOW)

# --- Lista de Imagens ---
# (Lista com 30 fotos únicas, incluindo a nova)
raw_image_paths = [
    "imagens/7a28892e-cb49-453a-9857-c3547231de6b.jpg", "imagens/0d427601-384a-449d-b935-069468ef3917.jpg",
    "imagens/1c4a86e4-cbcf-4a86-b6fe-30a5d26e4639.jpg", "imagens/1ebbab1f-7cd0-4128-a55c-a8e05bffbe6e.jpg",
    "imagens/2a546536-5b83-4a33-95a5-7bc28309e6d1.jpg", "imagens/3be387d0-0561-413f-8126-3c8119782ed1.jpg",
    "imagens/4f26d6e8-f6d8-4213-88ac-495b2e9b3175.jpg", "imagens/6df69606-e508-4a81-9b3d-abc491b099a0.jpg",
    "imagens/6f906328-f57f-4ea5-8e6d-8f12f74487b7.jpg", "imagens/9e264297-7acd-40ac-a8ae-8a2f0cbd339e.jpg",
    "imagens/21d25895-1288-4db2-857d-ed1400973387.jpg", "imagens/31b3bf5f-d68a-45fb-9722-2d5e2a3286c7.jpg",
    "imagens/060d5638-8666-45c3-9fc8-c23b642fbed5.jpg", "imagens/78b878b6-14a9-4df2-8060-499c939358bf.jpg",
    "imagens/91db3b05-5341-4b97-999d-f685110dc150.jpg", "imagens/254edec2-50eb-4e6b-ac36-bce2b88dfaa4.jpg",
    "imagens/503d6d53-a55e-4c74-8c85-35c8e27c0067.jpg", "imagens/17ce6785-3c46-4a49-a292-6284f69747c0.jpg",
    "imagens/873f8730-7988-468b-ac21-b4f0e737140e.jpg", "imagens/b5204445-6617-4560-a249-1667b2d2948c.jpg",
    "imagens/c571dd63-e522-4467-8854-934c98f8fc51.jpg", "imagens/d5a9d690-d4ec-406c-829d-ee1780f27464.jpg",
    "imagens/a7e2ea93-2876-40e2-98a2-c581bbc93779.jpg", "imagens/aa483bbe-4fdf-4c88-bbc0-ec4d07fd4414.jpg",
    "imagens/ae03878a-f795-4a8a-9277-7c52fed6623b.jpg", "imagens/b067b0c5-06df-4cb8-bbd3-9e2752e9a809.jpg",
    "imagens/b786514b-5813-430b-a0b2-5322fddb52da.jpg", "imagens/b8511401-d3a4-4633-a374-ec9553f291fe.jpg",
    "imagens/image_02c7fd.jpg", "imagens/Captura de tela 2025-11-19 233621.png",
]
image_paths = list(dict.fromkeys(raw_image_paths))

# --- Inicialização de Estado para o Carrossel ---
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    
def next_image():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(image_paths)

def prev_image():
    st.session_state.current_index = (st.session_state.current_index - 1 + len(image_paths)) % len(image_paths)

if len(image_paths) == 0:
    st.error("Nenhuma imagem encontrada.")
    st.stop()
    
current_image_path = image_paths[st.session_state.current_index]

# --- Layout da Interface ---

st.title("💖 Pedro e Hellen 💖")
st.markdown(f'<p class="centered-text">Juntos desde {START_DATETIME.strftime("%d/%m/%Y às %H:%M")}!</p>', unsafe_allow_html=True)
st.markdown("---")

# 2. Exibição do Contador de Tempo
st.header("Estamos Juntos Há:")

# Primeiro bloco: Anos, Meses, Dias
col_y, col_m, col_d = st.columns(3)
with col_y: st.metric(label="Anos", value=years)
with col_m: st.metric(label="Meses", value=months)
with col_d: st.metric(label="Dias", value=days)
    
# Segundo bloco: Horas e Minutos
st.subheader(f"E também há:")
col_h, col_min = st.columns(2)
with col_h: st.metric(label="Horas", value=hours)
with col_min: st.metric(label="Minutos", value=minutes)

# Total
st.markdown(f"<h3 style='text-align: center; color: #f87171; margin-top: 15px;'>Total: {total_days} dias, {total_hours} horas, ou {total_minutes} minutos de amor!</h3>", unsafe_allow_html=True)
st.markdown("---")

# 3. Carrossel de Fotos
st.subheader("Nossas Memórias Especiais")

col_prev, col_center, col_next = st.columns([1, 4, 1])
with col_prev: st.button("⬅️ Anterior", on_click=prev_image)
with col_next: st.button("Próxima ➡️", on_click=next_image)

st.image(
    current_image_path, 
    caption=f"Foto {st.session_state.current_index + 1} de {len(image_paths)} (Total: {len(image_paths)})", 
    use_column_width=True
)

# 4. Rodapé
st.markdown(f"---")
st.caption(f"Data e Hora de Início: **{START_DATETIME.strftime('%d/%m/%Y às %H:%M')}**")
st.caption(f"Total de fotos únicas no carrossel: **{len(image_paths)}**")
