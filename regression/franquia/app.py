import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Previsão de Custo para Franquia")

dados = pd.read_csv("data.csv", sep=';', encoding='iso 8859-1')

X = dados[['FrqAnual']]
y = dados['CusInic']

model = LinearRegression().fit(X, y)

col1, col2 = st.columns(2)

with col1:
    st.header("Dados")
    st.table(dados.head(10))

with col2:
    st.header("Modelo")
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(X, model.predict(X), color='red', linewidth=3)
    st.pyplot(fig)

st.header('Valor Anual da Franquia')
novo_valor = st.number_input('Insira o valor da Franquia', 
                             min_value=1.0, 
                             max_value=1000000.0,
                             step=0.01)
processar = st.button('Processar')

if processar:
    dados_novo_valor = pd.DataFrame({'FrqAnual': [novo_valor]})
    valor_previsto = model.predict(dados_novo_valor)
    st.write(f'Valor inicial previsto para a Franquia é de: R$ {valor_previsto[0]:.2f}')