import streamlit as st

#Crear el titulo para la aplicacion web
st.title('Mi primera App con Streamlit')
sidebar = st.sidebar
sidebar.title('Esta es la barra lateral.')
sidebar.write('Aqui van los elementos de entrada.')


st.header('Informacion sobre el conjunto de Datos')

st.header('Descripcion de los datos')

st.write('''
Este es un simple ejemplo de una app para predecir
Esta app predice mis datos
''')

#Radio Buttons o Botones de opciones
selected_class = st.radio("Select Class", titanic_data['class'].unique())
st.write("Selected Class:", selected_class)

#Selectbox
selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")

#Sliders

  #Variable que contiene el expansor
optionals = st.beta_expander("Optional Configurations", True)

  #Variable que contiene el valor seleccionado
fare_select = optionals.slider(

    "Select the Fare",

    min_value=float(titanic_data['fare'].min()),

    max_value=float(titanic_data['fare'].max())

)
 
  #Variable que contiene el conjunto de datos maximos y minimos
subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]

  #Imprime la barra deslizante
st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")

 



