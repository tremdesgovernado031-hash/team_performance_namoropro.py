import streamlit as st
from datetime import datetime
import os
import time

# =========================================================================
# 1. CONFIGURAÇÃO E DADOS
# =========================================================================

# Ajuste a data e hora do início do namoro aqui! (Ano, Mês, Dia, Hora, Minuto, Segundo)
# Esta data é usada tanto pelo Python quanto pelo JavaScript
# Exemplo: 19 de Maio de 2024 às 21:40:00
START_DATE = datetime(2024, 5, 19, 21, 40, 0) 
TITLE = "Pedro & Hellen ❤️" # Altere o título principal
SUBTITLE = "Juntos desde" # O subtítulo que aparece antes da data

# Lista de caminhos locais para as fotos
PHOTOS = [
    'imagens/3be387d0-0561-413f-8126-3c8119782ed1.jpg',
    'imagens/6df69606-e508-4a81-9b3d-abc491b099a0.jpg',
    'imagens/4f26d6e8-f6d8-4213-88ac-495b2e9b3175.jpg',
    'imagens/1c4a86e4-cbcf-4a86-b6fe-30a5d26e4639.jpg',
    'imagens/2a546536-5b83-4a33-95a5-7bc28309e6d1.jpg',
    'imagens/7a28892e-cb49-453a-9857-c3547231de6b.jpg',
    'imagens/1ebbab1f-7cd0-4128-a55c-a8e05bffbe6e.jpg',
    'imagens/0d427601-384a-449d-b935-069468ef3917.jpg', 
    'imagens/0d427601-384a-449d-b935-069468ef3917 - Copia.jpg',
    'imagens/6f906328-f57f-4ea5-8e6d-8f12f74487b7.jpg',
]

# =========================================================================
# 2. FUNÇÕES DE CÁLCULO (Apenas cálculos de data estáticos)
# =========================================================================

def calculate_static_time_components(start_date, now):
    """Calcula a diferença de tempo em anos, meses, dias, horas e minutos (valores estáticos)."""
    
    time_difference = now - start_date
    total_seconds = int(time_difference.total_seconds())

    # Componentes progressivos de HORAS e MINUTOS (para o ciclo de 24h e 60min)
    minutes_progressive = (total_seconds // 60) % 60
    hours_progressive = (total_seconds // (60 * 60)) % 24
    
    # Total de dias (sempre útil)
    total_days = total_seconds // (60 * 60 * 24)
    
    # Cálculo de anos e meses (baseado em data para maior precisão)
    years = now.year - start_date.year
    months = now.month - start_date.month
    days_partial = now.day - start_date.day

    if days_partial < 0:
        months -= 1
        days_partial += 30 # Aproximação
        
    if months < 0:
        years -= 1
        months += 12

    return {
        'years': years,
        'months': months,
        'total_days': total_days,
        'hours': hours_progressive,
        'minutes': minutes_progressive,
        'total_seconds_raw': total_seconds # Passamos o total de segundos para o JS
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
        height: 100%; /* Garante altura uniforme */
        display: flex;
        flex-direction: column;
        justify-content: center;
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

    # Cálculo do tempo estático (anos, meses, dias, horas, minutos)
    now = datetime.now()
    time_data = calculate_static_time_components(START_DATE, now)
    
    # Define a função auxiliar para display
    def display_counter_html(column, value, label, element_id=None):
        formatted_value = str(value).zfill(2) if label in ['Horas', 'Minutos'] else str(value)
        
        # Se tiver um ID (somente para Segundos), adiciona-o ao <span>
        value_tag = f'<span class="counter-value" id="{element_id}">{formatted_value}</span>' if element_id else f'<div class="counter-value">{formatted_value}</div>'
        
        with column:
            st.markdown(f"""
                <div class="counter-box">
                    {value_tag}
                    <div class="counter-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)

    # Exibição do Contador em Colunas
    # Note que a coluna de segundos agora usará um ID HTML
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    display_counter_html(col1, time_data['years'], 'Anos')
    display_counter_html(col2, time_data['months'], 'Meses')
    display_counter_html(col3, time_data['total_days'], 'Dias Totais')
    display_counter_html(col4, time_data['hours'], 'Horas')
    display_counter_html(col5, time_data['minutes'], 'Minutos')
    
    # A coluna de segundos é a que será atualizada pelo JavaScript
    display_counter_html(col6, 0, 'Segundos', element_id='seconds-counter') 
    # O valor inicial é 0, o JS irá corrigi-lo imediatamente

    # 3. GALERIA DE FOTOS
    st.markdown('<div class="gallery-title">Nossas Memórias</div>', unsafe_allow_html=True)
    
    # Filtra apenas fotos que realmente existem localmente (importante para evitar falhas)
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
                except Exception:
                    # Se uma imagem falhar, ignora e continua
                    pass 
    else:
        st.warning("Não foi possível carregar as fotos. Confirme se a pasta `imagens/` e os arquivos estão no GitHub.")

    # 4. INJEÇÃO DE JAVASCRIPT PARA ATUALIZAÇÃO DO SEGUNDOS (Solução Anti-Erro)
    # A data de início do Streamlit Cloud está em UTC. O START_DATE é convertido
    # para um timestamp UNIX que o JS entende para garantir a precisão.
    
    # Converta a data de início para timestamp UNIX (em milissegundos)
    start_timestamp_ms = int(START_DATE.timestamp() * 1000)
    
    js_code = f"""
    <script>
        // Carrega o timestamp de início da sessão do Python
        const START_TIME_MS = {start_timestamp_ms};

        function updateSecondsCounter() {{
            const now = new Date().getTime();
            const elapsed_ms = now - START_TIME_MS;
            
            // Calcula o total de segundos, horas, minutos e segundos restantes
            const total_seconds = Math.floor(elapsed_ms / 1000);
            const seconds = total_seconds % 60;

            const secondsElement = document.getElementById('seconds-counter');
            
            if (secondsElement) {{
                // Atualiza o valor com zero à esquerda (ex: 05)
                secondsElement.innerText = seconds.toString().padStart(2, '0');
            }} else {{
                // Se o elemento não for encontrado, para o loop para economizar recursos.
                // Isso deve evitar a maioria dos erros de DOM do Streamlit.
                clearInterval(window.secondsInterval); 
            }}
        }}

        // Limpa qualquer intervalo anterior para evitar duplicação (importante no Streamlit)
        if (window.secondsInterval) {{
            clearInterval(window.secondsInterval);
        }}
        
        // Inicia a atualização imediata e depois a cada 1 segundo
        updateSecondsCounter(); 
        window.secondsInterval = setInterval(updateSecondsCounter, 1000);

    </script>
    """
    # Injeta o script de JavaScript no Streamlit
    st.markdown(js_code, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
    
    # REMOVIDO: O st.rerun() e time.sleep(1) foram removidos para garantir a estabilidade!
