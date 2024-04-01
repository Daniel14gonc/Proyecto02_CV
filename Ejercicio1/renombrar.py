import os

# Ruta del directorio donde se encuentran las imágenes seleccionadas
ruta_carpeta_nueva = r'C:\Users\pablo\OneDrive\Documentos\GitHub\Proyecto02_CV\Ejercicio1\Dataset'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(ruta_carpeta_nueva)

# Ordenar la lista de archivos para asegurar un orden consistente
archivos.sort()

# Iterar sobre los archivos y renombrarlos del 1 al 50
for i, archivo in enumerate(archivos, start=1):
    # Obtener la ruta completa del archivo original
    ruta_original = os.path.join(ruta_carpeta_nueva, archivo)
    # Obtener la extensión del archivo
    nombre, extension = os.path.splitext(archivo)
    # Construir el nuevo nombre de archivo con el formato "nuevo_nombre_numero.extension"
    nuevo_nombre = f"{i}{extension}"
    # Construir la ruta completa para el nuevo archivo
    nueva_ruta = os.path.join(ruta_carpeta_nueva, nuevo_nombre)
    # Renombrar el archivo
    os.rename(ruta_original, nueva_ruta)

print("Imágenes renombradas correctamente.")
