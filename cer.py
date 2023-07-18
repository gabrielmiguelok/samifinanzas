from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--headless") # Asegurarse de que Chrome se ejecute en modo sin cabeza
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)


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
