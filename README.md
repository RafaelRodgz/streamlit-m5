# Activate virtual env
source streamlit-env/bin/activate

# Run hello_world.py
streamlit run employees.py --server.enableCORS false --server.enableXsrfProtection false

# subir nueva version a produccion
  # guardar los cambios en tu repo
  git add .
  git commit -m "se agrego tarea del reto (employees.py)"
  git push origin main

  # ir a streamlit y generar app nueva
   https://share.streamlit.io/ 

