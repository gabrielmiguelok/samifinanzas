import subprocess
import time

# Lista de scripts a ejecutar en orden
scripts = ['cer.py', 'htmltxtcer.py', 'ceractualizado.py']

for script in scripts:
    print(f"Ejecutando {script}...")

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
