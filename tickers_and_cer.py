import pandas as pd
from datetime import datetime
import os
import glob

# Encuentra el archivo .xlsx más reciente en el directorio
file_list = glob.glob('ACTUALIZACION*.xlsx')
recent_file = max(file_list, key=os.path.getctime)

# Carga el .xlsx con los tickers y precios
df = pd.read_excel(recent_file)

# Carga el indice CER (suponiendo que es un número)
file = open('CER ACTUALIZADO.log', 'r')
indice_cer = file.read()

# Crea una nueva columna con el indice CER
df['CER'] = indice_cer

# Obtiene la fecha y hora actual, y formatea como una cadena
now = datetime.now() 
date_hour_str = now.strftime("%Y-%m-%d %H-%M-%S")

# Crea el nombre del archivo con la fecha y hora
nombre_archivo = f'precios_tickers_con_CER_{date_hour_str}.xlsx'

# Escribe el DataFrame modificado de nuevo a un archivo .xlsx
df.to_excel(nombre_archivo, index=False)

file.close()

