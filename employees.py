import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

employees_link = 'Employees.csv'

#titulo
st.title('Empleados')

#encabezados
st.header('Descripcion de los datos')

#--- LOGO ---#
st.sidebar.image("logo2.png")
st.sidebar.markdown("##")
#--- SIDEBAR FILTERS ---#

#descripcion del proyecto
st.write('''
Este es un app creada para analizar los datos de empleados
''')

@st.cache
def load_data(nrows):
    data = pd.read_csv(employees_link, nrows = nrows)
    return data

#define las funciones para las cajas de texto y botones de comando

@st.cache
def filter_data_by_Employee_ID(employeid):
    filtered_data_Employee = data[data['Employee_ID'].str.upper().str.contains(employeid)]
    return filtered_data_Employee

@st.cache
def filter_data_by_Hometown(home):
    filtered_data_Hometown = data[data['Hometown'].str.upper().str.contains(home)]
    return filtered_data_Hometown

@st.cache
def filter_data_by_Unit(unit1):
    filtered_data_Unit = data[data['Unit'].str.upper().str.contains(unit1)]
    return filtered_data_Unit

@st.cache
def filter_data_by_education(educationl):
    filtered_data_education = data[data['Education_Level'] == educationl]
    return filtered_data_education

@st.cache
def filter_data_by_ciudad(ciudad):
    filtered_data_ciudad = data[data['Hometown'] == ciudad]
    return filtered_data_ciudad

#limita los datos a 500 filas
data = load_data(500)

#permite mostrar u ocultar un dataframe completo
if st.sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los empleados')
    st.write(data)

#crea un buscador con cajas de texto y botones de comando para ID Empleado
id_empleado = st.sidebar.text_input('ID de Empleado :')
btnBuscar = st.sidebar.button('Buscar ID')

if (btnBuscar):
   emp_id = filter_data_by_Employee_ID(id_empleado.upper())
   count_row = emp_id.shape[0]  # Gives number of rows
   st.write(f"Total de empleados : {count_row}")
   st.write(emp_id)

#crea un buscador con cajas de texto y botones de comando para Hometown
hometown = st.sidebar.text_input('Hometown :')
btnBuscar2 = st.sidebar.button('Buscar Hometown')

if (btnBuscar2):
   home_town = filter_data_by_Hometown(hometown.upper())
   count_row1 = home_town.shape[0]  # Gives number of rows
   st.write(f"Total de Ciudades : {count_row1}")
   st.write(home_town)

#crea un buscador con cajas de texto y botones de comando para Unit
Units = st.sidebar.text_input('Unit :')
btnBuscar3 = st.sidebar.button('Buscar Unit')

if (btnBuscar3):
   units_1 = filter_data_by_Unit(Units.upper())
   count_row2 = units_1.shape[0]  # Gives number of rows
   st.write(f"Total de unidades : {count_row2}")
   st.write(units_1)


#crea un control selectbox para filtrar por nivel educativo

selected_education = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbyEducation = st.sidebar.button('Filtrar Nivel Educativo')

if (btnFilterbyEducation):
   filterbyedu = filter_data_by_education(selected_education)
   count_row3 = filterbyedu.shape[0]  # Gives number of rows
   st.write(f"Total Niveles : {count_row3}")

   st.dataframe(filterbyedu)


#crea un control selectbox con las ciudades que participaron en el estudio

selected_ciudad = st.sidebar.selectbox("Seleccionar Ciudad", data['Hometown'].unique())
btnFilterbyCiudad = st.sidebar.button('Filtrar Ciudad')

if (btnFilterbyCiudad):
   filterbyCiudad = filter_data_by_ciudad(selected_ciudad)
   #grouped_data = filtered_data[['Hometown','Employee_ID']].groupby(['Hometown']).count()
   count_row4 = filterbyCiudad.shape[0]  # Gives number of rows
   st.write(f"Total empleados por ciudad : {count_row4}")

   st.dataframe(filterbyCiudad)

#crea un selectbox para filtrar por Unit

selected_unit = st.sidebar.selectbox("Seleccionar Unit", data['Unit'].unique())
btnFilterbyUnit = st.sidebar.button('Filtrar Unit')

if (btnFilterbyUnit):
   filterbyUnit = filter_data_by_Unit(selected_unit)
   count_row5 = filterbyUnit.shape[0]  # Gives number of rows
   st.write(f"Total de Empleados por Unit : {count_row5}")

   st.dataframe(filterbyUnit)

#Histograma

st.header("Histograma")  

fig, ax = plt.subplots()  
sns.histplot(data['Age'])
st.pyplot(fig)
st.markdown("___")   

#manera2 de Histogrma

#fig, ax = plt.subplots()      
#ax.hist(data.Age)  
#st.pyplot(fig)

#Grafico de Frecuencias

st.header("Grafico de Frecuencias")  

fig2, ax2 = plt.subplots() 
sns.countplot(x=data['Unit'])
plt.xticks(rotation=90)
st.pyplot(fig2)
st.markdown("___")  

#Grafico Lineal
st.header("Grafico Lineal") 

fig3, ax3 = plt.subplots() 
sns.lineplot(x = data['Hometown'],y = data['Attrition_rate'])
st.pyplot(fig3)
st.markdown("___")  

#Grafico Lineal 2

st.header("Grafico Lineal 2") 

fig4, ax4 = plt.subplots() 
sns.lineplot(x = data['Age'],y = data['Attrition_rate'])
st.pyplot(fig4)
st.markdown("___")  

#Grafico de dispersion

st.header("Grafico de dispersión") 

fig5, ax5 = plt.subplots() 
sns.scatterplot(x = data['Time_of_service'],y = data['Attrition_rate'])
st.pyplot(fig5)

