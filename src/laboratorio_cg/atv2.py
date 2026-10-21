import numpy as np
import streamlit as st

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:, :6] = (0, 35, 149)
bandeira[:, 6:12] = (255, 255, 255)
bandeira[:, 12:] = (237, 41, 57)

# O st.image fica AQUI:
st.image(bandeira, use_container_width=True)