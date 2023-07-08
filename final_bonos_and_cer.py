import subprocess
import time

# La lista de tus scripts
scripts = ["main.py", "mainbonos.py", "tickers_and_cer.py"]

for script in scripts:
    # subprocess.call ejecuta el script y espera a que termine
    subprocess.call(["python", script])