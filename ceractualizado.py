import os
import glob

# Itera sobre todos los archivos .txt en el directorio actual
for filename in glob.glob('*.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Itera sobre las líneas del archivo actual
    for i in range(len(lines)):
        # Si encuentra una línea que contiene "Hoy", entonces guarda la línea siguiente
        # en un archivo .log y rompe el bucle
        if "Hoy" in lines[i]:
            with open('CER ACTUALIZADO.log', 'w', encoding='utf-8') as log_file:
                if i+1 < len(lines):  # Verifica que no esté al final del archivo
                    log_file.write(lines[i+1])
            break

    # Elimina el archivo .txt fuente
    os.remove(filename)

    # Elimina un archivo .html con el mismo nombre si existe
    html_filename = filename.replace('.txt', '.html')
    if os.path.isfile(html_filename):
        os.remove(html_filename)
