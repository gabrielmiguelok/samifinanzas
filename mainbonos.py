import subprocess
import time
import os
import glob

# Lista de scripts a ejecutar en orden
scripts = ['bonos.py', 'htmltxtbonos.py', 'pasarexcelbonos.py']

for script in scripts:
    print(f"Ejecutando {script}...")

    # Eliminar archivos viejos en el directorio 'output/'
    files = glob.glob('ACTUALIZACION*.xlsx')
    for f in files:
        os.remove(f)

    # Crear el comando para ejecutar el script de Python
    command = ["python", script]

    # Iniciar el proceso
    process = subprocess.Popen(command, stdout=subprocess.PIPE)

    # Esperar a que termine el proceso
    while process.poll() is None:
        time.sleep(0.5)

    # Capturar la salida estándar
    output, error = process.communicate()

    # Decodificar la salida del script
    output = output.decode("utf-8")

    # Imprimir la salida del script
    print(output)

    if process.returncode != 0:
        print(f"Error al ejecutar {script}. El proceso devolvió el código {process.returncode}")
        break

    print(f"{script} terminó correctamente.")
