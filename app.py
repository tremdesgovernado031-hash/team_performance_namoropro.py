import streamlit as st
import os

# --- Configurações Iniciais ---
st.set_page_config(layout="centered")
st.title("Meu Contador de Fotos do Casal")
st.markdown("---")


# --- LISTA DE IMAGENS ---
# Esta lista contém os caminhos de TODAS as 29 fotos que você fez upload até agora.
# O método list(dict.fromkeys(...)) garante que não haverá duplicatas na lista final,
# mantendo a ordem original.
raw_image_paths = [
    # 10 Fotos Iniciais
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
    # 6 Fotos do Segundo Upload
    "imagens/21d25895-1288-4db2-857d-ed1400973387.jpg",
    "imagens/31b3bf5f-d68a-45fb-9722-2d5e2a3286c7.jpg",
    "imagens/060d5638-8666-45c3-9fc8-c23b642fbed5.jpg",
    "imagens/78b878b6-14a9-4df2-8060-499c939358bf.jpg",
    "imagens/91db3b05-5341-4b97-999d-f685110dc150.jpg",
    "imagens/254edec2-50eb-4e6b-ac36-bce2b88dfaa4.jpg",
    # 6 Fotos do Terceiro Upload
    "imagens/503d6d53-a55e-4c74-8c85-35c8e27c0067.jpg",
    "imagens/17ce6785-3c46-4a49-a292-6284f69747c0.jpg",
    "imagens/873f8730-7988-468b-ac21-b4f0e737140e.jpg",
    "imagens/b5204445-6617-4560-a249-1667b2d2948c.jpg",
    "imagens/c571dd63-e522-4467-8854-934c98f8fc51.jpg",
    "imagens/d5a9d690-d4ec-406c-829d-ee1780f27464.jpg",
    # 6 Fotos do Quarto Upload
    "imagens/a7e2ea93-2876-40e2-98a2-c581bbc93779.jpg",
    "imagens/aa483bbe-4fdf-4c88-bbc0-ec4d07fd4414.jpg",
    "imagens/ae03878a-f795-4a8a-9277-7c52fed6623b.jpg",
    "imagens/b067b0c5-06df-4cb8-bbd3-9e2752e9a809.jpg",
    "imagens/b786514b-5813-430b-a0b2-5322fddb52da.jpg",
    "imagens/b8511401-d3a4-4633-a374-ec9553f291fe.jpg",
    # 1 Foto Nova
    "imagens/image_02c7fd.jpg",
]

# Remove duplicatas mantendo a ordem (list(dict.fromkeys(list)) é a maneira Pythonica)
image_paths = list(dict.fromkeys(raw_image_paths))
# O total de imagens carregadas é agora 29.

# --- Inicialização de Estado ---
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'count' not in st.session_state:
    st.session_state.count = 0

# Garante que o índice não exceda a lista
if len(image_paths) == 0:
    st.error("Nenhuma imagem encontrada. Certifique-se de que os arquivos estão na pasta 'imagens/'.")
    st.stop()
elif st.session_state.current_index >= len(image_paths):
    st.session_state.current_index = 0
    
current_image_path = image_paths[st.session_state.current_index]
current_image_filename = os.path.basename(current_image_path)


# --- Função de Callback para Próxima Imagem ---
def next_image_callback():
    """Avança para a próxima imagem e incrementa o contador."""
    st.session_state.count += 1
    # Cálculo do próximo índice (volta para 0 se chegar ao final da lista)
    st.session_state.current_index = (st.session_state.current_index + 1) % len(image_paths)
    
    # Notificação ao completar um ciclo
    if st.session_state.current_index == 0:
        st.toast(f"Contagem do ciclo completa! Reiniciando na primeira foto. Total marcado: {st.session_state.count}")

# --- Layout da Interface ---

# 1. Colunas para a Imagem e o Contador
col_img, col_count = st.columns([3, 1])

with col_img:
    st.image(current_image_path, caption=f"Foto {st.session_state.current_index + 1} de {len(image_paths)}", use_column_width=True)

with col_count:
    # Mostra o contador de fotos marcadas
    st.metric(label="Contagem Total de Marcações", value=st.session_state.count)
    
# 2. Botão de Ação
st.button(
    "Marcar e Próxima Foto",
    on_click=next_image_callback,
    type="primary"
)

# 3. Mostrar o nome do arquivo atual (para verificação)
st.markdown(f"---")
st.info(f"Total de fotos únicas no carrossel: **{len(image_paths)}**")
st.caption(f"Arquivo atual: `{current_image_filename}`")

# --- Limpar Contagem (Opcional) ---
if st.button("Zerar Contagem e Reiniciar"):
    st.session_state.count = 0
    st.session_state.current_index = 0
    st.rerun() # Recarrega a página para aplicar a mudança
