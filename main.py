# import pandas as pd
# import numpy as np
import streamlit as st
import pickle
import base64
# import requests

imdb = pickle.load(open('imdb.pkl','rb'))
similarity_matrix = pickle.load(open('similarity_matrix.pkl','rb'))

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('mrs.jpg')

recommended_movies=[]

def recommend(movie):
    movie_index = imdb[imdb['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(imdb.iloc[i[0]].title)
    return recommended_movies

st.title('Movies Recommendation System')
name = st.selectbox("Enter a movie name", imdb['title'].values)

if st.button('Recommend'):
    names = recommend(name)
    for i in names:
        st.subheader(i)