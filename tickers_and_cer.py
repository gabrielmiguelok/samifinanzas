import os
import time
import glob
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

# Encuentra el archivo .xlsx más reciente en el directorio y lo carga
df = pd.read_excel(max(glob.glob('ACTUALIZACION*.xlsx'), key=os.path.getctime))

# Carga el indice CER, lo convierte a un float y lo agrega al DataFrame
with open('CER ACTUALIZADO.log', 'r') as file:
    df['CER'] = float(file.read().replace(',', '.'))

# Autentica con las credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(os.getcwd(), 'finanzassami.json'),
    ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
)

gc = gspread.authorize(credentials)

# Intenta abrir el archivo existente, sino lo crea
try:
    spreadsheet = gc.open('precios_tickers_con_CER')
except gspread.SpreadsheetNotFound:
    spreadsheet = gc.create('precios_tickers_con_CER')

# Escribe el DataFrame modificado de nuevo a la hoja de Google
set_with_dataframe(spreadsheet.get_worksheet(0), df)
