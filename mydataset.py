import pandas as pd
import streamlit as st

name_link = 'dataset.csv'

names_data = pd.read_csv(name_link)

st.title('streamlit con pandas')
st.dataframe(names_data)