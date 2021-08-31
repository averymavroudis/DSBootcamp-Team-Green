import streamlit as st
import pandas as pd
import numpy as np
import os


CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))

print(CONFIG_PATH)

movies_df = pd.read_csv(
        os.path.join(CONFIG_PATH, 'movies.csv'),
        encoding='latin-1',  
        skiprows=1, 
        index_col=0, 
        sep='\t', 
        names=['movie_id', 'title', 'genres']
    )
movie_list = movies_df['title'].to_list()
 
movie_list.sort()

st.title('Movie Recommendations')

form = st.form(key='my-form')
form.markdown('Please choose three movies from the list below')

hint_text = 'Select or type to search'
movie1 = form.selectbox(
        'Movie 1', 
        [ hint_text, *movie_list ]
    )
movie2 = form.selectbox(
        'Movie 2', 
        [ hint_text, *movie_list ]
    )
movie3 = form.selectbox(
        'Movie 3', 
        [ hint_text, *movie_list ]
    )
recommender_list = st.empty()
submit = form.form_submit_button('Submit')

def load_recommendations(list_of_movies):
    # for movie in list_of_movies:
    movie_list = "\n".join(list_of_movies)
        # movie_list.append(movie + "  \n")
    recommender_list.text(movie_list)

if submit:
    if hint_text in [movie1, movie2, movie3]:
        st.write('Please choose three movies')
    else:
        load_recommendations([movie1, movie2, movie3])

