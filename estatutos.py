import pandas as pd

import streamlit as st
streamlit run estatutos.py --server.enableCORS false --server.enableXsrfProtection false
 

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

 

titanic_data = pd.read_csv(titanic_link)

 

# Create the title for the web app

st.title("My First Streamlit App")

sidebar = st.sidebar

sidebar.title("This is the sidebar.")

sidebar.write("You can add any elements to the sidebar.")

 

 

st.header("Dataset Overview")

st.dataframe(titanic_data)

 

st.header("Data Description")

 

selected_class = st.radio("Select Class", titanic_data['class'].unique())

st.write("Selected Class:", selected_class)

st.markdown("___")

 

selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())

st.write(f"Selected Option: {selected_sex!r}")

 

st.markdown("___")

 

optionals = st.beta_expander("Optional Configurations", True)

fare_select = optionals.slider(

    "Select the Fare",

    min_value=float(titanic_data['fare'].min()),

    max_value=float(titanic_data['fare'].max())

)

subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]

st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")

 
st.markdown("___")