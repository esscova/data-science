import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Classificação de Veículos",
    page_icon="🚗",
    layout="wide",
)

@st.cache_data
def load_data_and_model():

    df = pd.read_csv("car.csv", sep=',', encoding='iso 8859-1')
    encoder = OrdinalEncoder()

    for col in df.columns.drop('class'):
        df[col] = df[col].astype('category')
    
    X_enconded = encoder.fit_transform(df.drop('class', axis=1))
    y = df['class'].astype('category').cat.codes

    X_train, X_test, y_train, y_test = train_test_split(X_enconded, y, test_size=0.3, random_state=42)

    model = CategoricalNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return encoder, model, accuracy, df

encoder, model, accuracy, df = load_data_and_model()

st.title("Classificação de Veículos")
st.write(f"Acurácia do Modelo: {accuracy*100.0:.2f}%")

input_features = [
    st.selectbox(f"{feature}", df[feature].unique()) for feature in df.columns.drop('class')
]

if st.button("Classificar"):
    input_df = pd.DataFrame([input_features], columns=df.columns.drop('class'))
    input_encoded = encoder.transform(input_df)
    prediction_encoded = model.predict(input_encoded)
    prediction = df['class'].astype('category').cat.categories[prediction_encoded[0]]

    st.header(f"Classe prevista: {prediction}")