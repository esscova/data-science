# -*- coding: utf-8 -*-
"""
Created on nov. 2024
@Author: wellington moreira

App para previsão de falhas em equipamentos
"""

# bibliotecas
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.set_page_config(page_title="Probabilidade de Falhas em Equipamentos")
st.title("Probabilidade de Falhas em Equipamentos")

with st.sidebar:
    st.header("Configurações")
    tipo = st.radio("Selecione o Cálculo", options=["Prob. Exata","Menos que","Mais que"])
    ocorrencia = st.number_input("Ocorrência Atual",min_value=1,max_value=99, value=2, step=1)
    processar = st.button("Processar")

if processar:
    lamb = ocorrencia
    inic = lamb -2
    fim = lamb + 2
    x_vals = np.arange(inic,fim+1)

    if tipo =="Prob. Exata":
        probs = poisson.pmf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência"
    elif tipo == "Menos que":
        probs = poisson.cdf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência Igual ou Menor que:"
    else:
        probs = poisson.sf(x_vals, lamb)
        tit = "Probabilidades de Ocorrência Maior que:"

    z_vals = np.round(probs,4)
    labels = [
        f'{x_vals[i]:.0f}: {z_vals[i]:.4f}' for i in range(len(x_vals))
    ]


    fig, ax = plt.subplots()
    ax.bar(x_vals, probs, tick_label=labels)
    ax.set_title(tit)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig)