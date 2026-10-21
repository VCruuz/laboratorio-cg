import streamlit as st
from src.laboratorio_cg.atv2 import bandeira

st.title("Laboratório de Computação Gráfica")
st.write("Desenvolvido por: Vitor Alves de Oliveira Cruz")

# Exibe a bandeira criada no atv2.py
st.image(bandeira, use_container_width=True)