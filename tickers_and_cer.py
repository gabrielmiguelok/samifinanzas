import pandas as pd
from datetime import datetime
import os
import glob
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

# Elimina archivos viejos que comienzan con 'precios_tickers_con_CER'
# for f in glob.glob('precios_tickers_con_CER_*.xlsx'):
#     os.remove(f)
    
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

# Define las credenciales de la API de Google Cloud
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

# Pon aquí el nombre de tu archivo de credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Marti/Programs/samifinanzas/finanzassami.json', scope)

# Autentica con las credenciales
gc = gspread.authorize(credentials)

# Crea el nombre del archivo
nombre_archivo = f'precios_tickers_con_CER'

# Intenta abrir el archivo existente
try:
    spreadsheet = gc.open(nombre_archivo)
except gspread.SpreadsheetNotFound:
    # Si el archivo no existe, crea un nuevo archivo
    spreadsheet = gc.create(nombre_archivo)
    # Comparte el archivo con el correo electrónico que desees
    spreadsheet.share('pablou90@gmail.com', perm_type='user', role='writer')

# Obtiene la primera hoja del archivo
worksheet = spreadsheet.get_worksheet(0)

# Escribe el DataFrame modificado de nuevo a la hoja de Google
set_with_dataframe(worksheet, df)

file.close()
