import subprocess
import os

# Lista de archivos .ipynb a convertir y ejecutar
archivos_ipynb = ["./archivos_ipynb/Articulos.ipynb",
                  "./archivos_ipynb/precios.ipynb",
                  "./archivos_ipynb/Final.ipynb"]



for archivo in archivos_ipynb:
    nombre_archivo_py = os.path.basename(archivo).replace(".ipynb", ".py")
    output_path = os.path.abspath(os.path.join("archivos_py", nombre_archivo_py))

    # Convertir el archivo .ipynb a un archivo .py
    subprocess.run(["jupyter", "nbconvert", "--to", "python", archivo, "--output", output_path])

    # Ejecutar el archivo .py
    subprocess.run(["python", output_path])