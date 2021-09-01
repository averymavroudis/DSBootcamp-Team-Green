import streamlit as st
import pandas as pd
import numpy as np
import os


CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))

print(CONFIG_PATH)

users_df = pd.read_csv(
        os.path.join(CONFIG_PATH, 'users.csv'),
        encoding='latin-1',  
        skiprows=1, 
        index_col=0, 
        sep='\t', 
        names=['user_id', 'gender', 'age', 'occupation', 'zipcode', 'age_desc', 'occ_desc']
    )
users_list = users_df['user_id'].to_list()
 
users_list.sort()

st.title('Movie Recommender App')

form = st.form(key='my-form')
form.markdown('Select user from list below.')

hint_text = 'Select or type to search'
user1 = form.selectbox(
        'User:', 
        [ hint_text, *users_list ]
    )

recommender_list = st.empty()
submit = form.form_submit_button('Submit')

