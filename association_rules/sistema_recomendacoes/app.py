# -*- coding: utf-8 -*-
"""
Created on nov. 2024
@Author: esscova

App para recomendação de itens
"""

# bibliotecas
import streamlit as st
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

# configurações
st.set_page_config(page_title="Geração de Regras de Recomendação",
                   layout="wide")

# titulos
st.title("Geração de Regras de Recomendação")

# sidebar
with st.sidebar:
    uploaded_file = st.file_uploader("Escolha o arquivo", type=['csv'])
    suporte_minimo = st.number_input("Suporte Mínimo", 0.0001,1.0,0.01,0.01)
    confianca_minima = st.number_input("Confiança Mínima", 0.0001,1.0,0.2,0.01)
    lift_minimo = st.number_input("Lift Mínimo", 0.0001,10.0,1.0,0.1)
    tamanho_minimo = st.number_input("Tamanho Mínimo", 1,10,2,1)
    processar = st.button("Processar")

# processamento
if processar and uploaded_file is not None:
    try:
        # leitura e transformação
        transactions = [
            line.decode("utf-8").strip().split(',') for line in uploaded_file
        ]
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        df = pd.DataFrame(te_ary, columns=te.columns_)

        # regras de associação
        frequent_itemsets = apriori(df, min_support=suporte_minimo, use_colnames=True)
        rules = association_rules(frequent_itemsets, 
                                  min_threshold=confianca_minima,
                                  num_itemsets=len(frequent_itemsets))
        
        rules['antecedents'] = rules['antecedents'].apply(list)
        rules['consequents'] = rules['consequents'].apply(list)

        rules_filtered = rules[
            (rules['lift'] >= lift_minimo) &
            (rules['antecedents'].apply(lambda x: len(x) >= tamanho_minimo))
        ]

        # criando colunas para visualização
        if not rules_filtered.empty:
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("Transações")
                st.dataframe(df)

            with col2:
                st.header("Regras Encontradas")
                st.dataframe(rules_filtered)

            with col3:
                st.header("Visualização")
                fig,ax = plt.subplots()
                scatter = ax.scatter(rules_filtered['support'], rules_filtered['confidence'],
                                     alpha=0.5,c=rules_filtered['lift'], cmap='viridis')
                plt.colorbar(scatter, label='Lift')
                ax.set_title("Regras de Associação")
                ax.set_xlabel("Suporte")
                ax.set_ylabel("Confiança")
                st.pyplot(fig)

            # resumo das regras
            st.header("Resumo das Regras")
            st.write(f"Total de Regras Geradas: {len(rules_filtered)}")
            st.write(f"Suporte Médio: {rules_filtered['support'].mean():.4f}")
            st.write(f"Confiança Média: {rules_filtered['confidence'].mean():.4f}")
            st.write(f"Lift Médio: {rules_filtered['lift'].mean():.4f}")

            # download das regras
            st.download_button(label="Exportar Regras como CSV",
                               data=rules_filtered.to_csv(index=False),
                               file_name="regras_associacao.csv",
                               mime='text/csv')

        else:
            st.warning("Nenhuma regra encontrada")

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")