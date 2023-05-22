import os
import glob
import shutil

ruta_destino = os.path.join(os.path.expanduser('~'), 'MisDescargas')
ruta_origen =os.path.join(os.path.expanduser('~'), 'Downloads')

img = ['JPEG','JPG','PNG','GIF','BMP','TIFF','SVG','WebP']
docs = ['DOC','DOCX','PDF','TXT','XLS','XLSX','PPT','PPTX','CSV','RTF','ODT']
audio = ['MP3','WAV','FLAC','AAC','OGG','M4A','AIFF']
video = ['MP4','AVI','MOV','MKV','WMV','FLV','MPEG','webm']
programs = ['exe','msi']
compressed = ['zip', 'rar','7z']

delete = ['crdownload',]

folder_tree = {
    "programs": programs,
    "video":    video,
    "audio":    audio,
    "docs":     docs,
    "img":      img,
    "compressed":compressed,
    "folders": [],
    "others": []
}


folders = list(folder_tree.keys())

# Verificar si la carpeta no existe previamente
if not os.path.exists(ruta_destino):
    # Crear la carpeta
    os.makedirs(ruta_destino)
    # creamos los directorios
    for f in folders:
        os.makedirs(f"{ruta_destino}/{f}")
else:
    # validamos si existen las carpetas organizadoras dentro de la carpeta de destino, de no existir se crea
    for f in folders:
        folder = f"{ruta_destino}/{f}"
        if not os.path.exists(folder):
            os.makedirs(folder)


if not os.path.exists(ruta_origen):
    raise ValueError("No se encontro la carpeta de origen")

"""----------------------Listo--------------------------"""

for f in folders:
    #obtenemos la lista de extenciones  para la carpeta organizadora
    for extension in folder_tree[f]:
        # Especifica el patrón de archivos
        patron_archivos = f'{ruta_origen}/*.{extension.lower()}'

        # Obtiene la lista de archivos que coinciden con el patrón
        archivos_to_moved = glob.glob(patron_archivos)

        for file in archivos_to_moved:
            shutil.move(file, f"{ruta_destino}/{f}")


#movemos las carpetas 
# Obtiene la lista de elementos dentro de la carpeta principal
elementos = os.listdir(ruta_origen)

# Filtra los elementos que son carpetas
carpetas = [elemento for elemento in elementos if os.path.isdir(os.path.join(ruta_origen, elemento))]

# Imprime los nombres de las carpetas
for carpeta in carpetas:
    shutil.move(f"{ruta_origen}/{carpeta}", f"{ruta_destino}/folders")

#Eliminamos los archios que no queremos
for extension in delete:
    patron_archivos = f'{ruta_origen}/*.{extension.lower()}'
    archivos_to_deleted = glob.glob(patron_archivos)
    for file_delete in archivos_to_deleted:
        os.remove(file_delete)

#movemos los que no calzan

# Lista los archivos de la carpeta
archivos = os.listdir(ruta_origen)

# Imprime los nombres de los archivos
for archivo in archivos:
    if os.path.isfile(os.path.join(ruta_origen, archivo)):
        shutil.move(f"{ruta_origen}/{archivo}", f"{ruta_destino}/others")