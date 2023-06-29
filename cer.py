from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Configura el driver de Selenium
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Define la URL de la página web
url = 'https://ikiwi.net.ar/coeficiente-de-estabilizacion-de-referencia-cer/'

# Navega a la página web
driver.get(url)

# Espera a que se cargue la página
time.sleep(3)

# Obtén el HTML de la página
html = driver.page_source

# Usa BeautifulSoup para parsear el HTML
soup = BeautifulSoup(html, 'html.parser')

# Guarda el HTML en un archivo
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# Cierra el navegador al terminar
driver.quit()
