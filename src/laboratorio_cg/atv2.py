import numpy as np
import streamlit as st

# Matriz 12x18 pixels com 3 canais de cor RGB
bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

# 1. Faixa Azul (esquerda) - colunas de 0 a 5
bandeira[:, :6] = (0, 35, 149)

# 2. Faixa Branca (meio) - colunas de 6 a 11
bandeira[:, 6:12] = (255, 255, 255)

# 3. Faixa Vermelha (direita) - colunas de 12 a 18
bandeira[:, 12:] = (237, 41, 57)

# Exibe a bandeira no Streamlit
st.image(bandeira, use_container_width=True)