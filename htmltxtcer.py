import os
from bs4 import BeautifulSoup, Comment

# Obtener todos los archivos en el directorio actual
archivos = os.listdir()

# Filtrar solo los archivos html
archivos_html = [archivo for archivo in archivos if archivo.endswith('.html')]

for archivo_html in archivos_html:
    with open(archivo_html, 'r', encoding='utf-8') as f:
        contenido = f.read()
        
    # Parsear el contenido HTML
    soup = BeautifulSoup(contenido, 'html.parser')
    
    # Eliminar scripts y estilos
    for script in soup(["script", "style", "head"]):
        script.decompose()    # eliminar estos elementos del árbol DOM de BeautifulSoup

    # Eliminar todos los comentarios
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    # Obtener el texto
    texto = soup.get_text()
    
    # Eliminar líneas en blanco
    lineas = (linea.strip() for linea in texto.splitlines())
    
    # Romper líneas con varias partes en varias líneas
    partes = (frase.strip() for linea in lineas for frase in linea.split("  "))
    
    # Eliminar líneas en blanco
    texto = '\n'.join(parte for parte in partes if parte)
    
    # Crear el nombre del archivo de texto
    nombre_archivo_txt = archivo_html.replace('.html', '.txt')
    
    # Escribir el texto extraído en un archivo de texto
    with open(nombre_archivo_txt, 'w', encoding='utf-8') as f:
        f.write(texto)
