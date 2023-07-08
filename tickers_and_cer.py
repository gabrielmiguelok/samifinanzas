import pandas as pd
import os
import glob
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

def load_emails():
    """Carga los correos del archivo emails.txt"""
    if os.path.exists('emails.txt'):
        with open('emails.txt', 'r') as file:
            return file.read().splitlines()
    else:
        return []

def save_emails(emails):
    """Guarda los correos en el archivo emails.txt"""
    with open('emails.txt', 'w') as file:
        for email in emails:
            file.write(f'{email}\n')

def manage_sharing(email, action, emails):
    """Gestiona la compartición del archivo basándose en la acción proporcionada"""
    if action.lower() == 'a':
        if email not in emails:
            spreadsheet.share(email, perm_type='user', role='reader', notify=False)
            emails.append(email)
            save_emails(emails)
    elif action.lower() == 'q':
        if email in emails:
            spreadsheet.remove_permissions(email, role='reader')
            emails.remove(email)
            save_emails(emails)
    else:
        print("Entrada no válida. Por favor, elige 'a' para agregar o 'q' para quitar.")

# Carga la lista de correos
shared_emails = load_emails()

# Encuentra el archivo .xlsx más reciente en el directorio y lo carga
df = pd.read_excel(max(glob.glob('ACTUALIZACION*.xlsx'), key=os.path.getctime))

# Carga el indice CER, lo convierte a un float y lo agrega al DataFrame
with open('CER ACTUALIZADO.log', 'r') as file:
    df['CER'] = float(file.read().replace(',', '.'))

# Autentica con las credenciales
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(os.getcwd(), 'finanzassami.json'),
    ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
)

gc = gspread.authorize(credentials)

# Intenta abrir el archivo existente, sino lo crea
try:
    spreadsheet = gc.open('precios_tickers_con_CER')
except gspread.SpreadsheetNotFound:
    spreadsheet = gc.create('precios_tickers_con_CER')

# Solicita al usuario que ingrese un correo electrónico y una acción
email = input("Ingresa el correo electrónico con el que deseas compartir el archivo (presiona enter para omitir): ")
if email:
    manage_sharing(
        email,
        input("¿Quieres agregar (a) o quitar (q) este correo? "),
        shared_emails
    )

# Comparte el archivo con los correos de la lista con permisos de solo lectura
for email in shared_emails:
    spreadsheet.share(email, perm_type='user', role='reader', notify=False)

# Escribe el DataFrame modificado de nuevo a la hoja de Google
set_with_dataframe(spreadsheet.get_worksheet(0), df)
