import subprocess
import time

# La lista de tus scripts
scripts = ["main.py", "mainbonos.py", "tickers_and_cer.py"]

while True:

    for script in scripts:
        # subprocess.call ejecuta el script y espera a que termine
        subprocess.call(["python", script])

    # Dormir durante 600 segundos (10 minutos)
    time.sleep(600)
