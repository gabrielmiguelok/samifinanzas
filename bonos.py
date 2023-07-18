from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Configura las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")

# Configura el driver de Selenium
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)

# Define la URL de la página web
url = 'https://www.rava.com/cotizaciones/bonos'

# Navega a la página web
driver.get(url)

# Espera a que se cargue la página
time.sleep(7)

# Obtén el HTML de la página
html = driver.page_source

# Usa BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html, 'html.parser')

# Guarda el HTML en un archivo
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# Cierra el navegador al terminar
driver.quit()
