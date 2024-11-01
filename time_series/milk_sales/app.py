import streamlit as st
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from datetime import date
from io import StringIO

st.set_page_config(
    page_title="Milk Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("Milk Sales Forecasting")

with st.sidebar:
    upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if upload_file is not None:
        stringio = StringIO(upload_file.getvalue().decode("utf-8"))
        df = pd.read_csv(stringio, header=None)
        
        data_inicio = date(2000, 1, 1)
        periodo = st.date_input('Periodo de previsão', data_inicio)
        periodo_previsao = st.number_input('Informe quantos meses quer prever', min_value=1, max_value=48, value=12)

        processar = st.button("Processar")

if upload_file is not None and processar:
    try:
        ts_data = pd.Series(df.iloc[:,0].values, index=pd.date_range(start=periodo, periods=len(df), freq='M'))
        seasonal_data = seasonal_decompose(ts_data, model='additive')

        fig_decompose = seasonal_data.plot()
        fig_decompose.set_size_inches(12, 6)

        modelo = SARIMAX(ts_data, order=(2, 0, 0), seasonal_order=(0, 1, 1, 12))
        modelo_fit = modelo.fit()
        previsao = modelo_fit.forecast(steps=periodo_previsao)

        fig_previsao, ax = plt.subplots(figsize=(12, 6))
        ax = ts_data.plot(ax=ax)
        previsao.plot(ax=ax, style='r--')

        col1, col2, col3 = st.columns([3,3,2])

        with col1:
            st.write("Decomposição")
            st.pyplot(fig_decompose)

        with col2:
            st.write("Previsão")
            st.pyplot(fig_previsao)

        with col3:
            st.write("Previsão")
            st.dataframe(previsao)
            
    except Exception as e:
        st.error(f"Algo deu errado. Verifique o arquivo e tente novamente. Erro: {e}")
