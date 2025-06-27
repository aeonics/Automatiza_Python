###Ordena los ficheros de un directorio###
import os
import shutil

#Ruta Origen
ruta_origen = "/home/aeonics/Descargas"
#Crear carpetas si no existen
folders = ["Imagenes","PDFs","Comprimidos","Txt"]
for tipos in folders:
    ruta_folder=os.path.join(ruta_origen, tipos)
    if not os.path.exists(ruta_folder):
        os.makedirs(ruta_folder)

