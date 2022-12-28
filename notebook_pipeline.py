import subprocess

# Lista de archivos .ipynb a convertir y ejecutar
archivos_ipynb = ["Articulos.ipynb", "precios.ipynb", "Final.ipynb"]

# Iterar sobre cada archivo .ipynb
for archivo in archivos_ipynb:
    # Convertir el archivo .ipynb a un archivo .py
    subprocess.run(["jupyter", "nbconvert", "--to", "python", archivo])

    # Extraer el nombre del archivo .py
    nombre_archivo_py = archivo.replace(".ipynb", ".py")

    # Ejecutar el archivo .py
    subprocess.run(["python", nombre_archivo_py])
