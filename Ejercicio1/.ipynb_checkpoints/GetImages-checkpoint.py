import os
import random
import shutil

# Ruta del directorio donde se encuentran las imágenes
ruta_carpeta = r'C:\Users\pablo\OneDrive\Desktop\frames'

# Ruta del directorio donde se guardarán las imágenes seleccionadas
ruta_carpeta_nueva = r'C:\Users\pablo\OneDrive\Desktop\nuevas_imagenes'

# Verificamos si el directorio de destino existe, si no, lo creamos
if not os.path.exists(ruta_carpeta_nueva):
    os.makedirs(ruta_carpeta_nueva)

# Lista de nombres de archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Seleccionamos aleatoriamente 50 imágenes (o menos si hay menos de 50 en total)
imagenes_seleccionadas = random.sample(archivos, min(50, len(archivos)))

# Copiamos las imágenes seleccionadas al directorio de destino
for imagen in imagenes_seleccionadas:
    ruta_imagen_original = os.path.join(ruta_carpeta, imagen)
    ruta_imagen_nueva = os.path.join(ruta_carpeta_nueva, imagen)
    shutil.copyfile(ruta_imagen_original, ruta_imagen_nueva)

print("Imágenes seleccionadas y guardadas correctamente.")
