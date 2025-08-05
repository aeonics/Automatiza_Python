###Ordena los ficheros de un directorio###
import os
import shutil

#Ruta Origen
ruta_origen = "/home/aeonics/Descargas"
#Crear carpetas si no existen
folders = ["Imagenes","PDFs","ZIPs","Txt"]
for tipos in folders:
    ruta_folder=os.path.join(ruta_origen, tipos)
    if not os.path.exists(ruta_folder):
        os.makedirs(ruta_folder)

for archivo in os.listdir(ruta_origen):
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        shutil.move(os.path.join(ruta_origen,archivo), os.path.join(ruta_origen,"Imagenes",archivo))
    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta_origen,archivo), os.path.join(ruta_origen,"PDFs",archivo))
    elif archivo.endswith(".gz") or archivo.endswith(".zip"):
        shutil.move(os.path.join(ruta_origen,archivo), os.path.join(ruta_origen,"ZIPs",archivo))
    elif archivo.endswith(".txt"):
        shutil.move(os.path.join(ruta_origen,archivo), os.path.join(ruta_origen,"Txt",archivo))