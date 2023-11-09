import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simples previsor do tipo da flor Iris

Este site consegue prever o tipo da **flor Iris** com base em suas características
""")

st.sidebar.header('Parâmetros do usuário')

def user_input():
    sepal_length = st.sidebar.slider('Comprimento da sétala', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Largura da sétala', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Comprimento da pétala', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Largura da pétala', 0.1, 2.5, 0.2)
    dados = {'Comprimento da sétala': sepal_length,
             'Largura da sétala': sepal_width,
             'Comprimento da pétala': petal_length,
             'Largura da pétala': petal_width}
    features = pd.DataFrame(dados, index=[0])
    return features

df = user_input()

st.subheader('Parâmetros do usuário')
st.write(df)

iris = datasets.load_iris()
x = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(x, y)

pred = clf.predict(df)
pred_prob = clf.predict_proba(df)

st.subheader('Classes e seus correspondentes índices')
st.write(iris.target_names)

st.subheader('Previsões')
st.write(iris.target_names[pred])

st.subheader('Probabilidade da previsão')
st.write(pred_prob)
