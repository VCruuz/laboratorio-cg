import numpy as np
import streamlit as st

st.title("Atividade 3 - Padrão Matemático")

# Controle k
k = st.slider("Ajuste o controle k:", min_value=1, max_value=50, value=10)

altura, largura = 200, 200

# Cria as matrizes de coordenadas X e Y vetorizadas
y, x = np.ogrid[:altura, :largura]

# Aplica a fórmula matemática de forma ultra rápida
r = (x * k + y) % 256
g = (y * k - x) % 256
b = np.bitwise_xor(x, y * k) % 256

# Junta os 3 canais em uma imagem RGB (uint8)
imagem = np.stack([r, g, b], axis=-1).astype(np.uint8)

st.image(imagem, caption=f"Padrão com k = {k}", use_container_width=True)