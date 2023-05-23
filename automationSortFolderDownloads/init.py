import os
import glob
import shutil

"""
init variables
"""

DESTINATION_FOLDER_NAME ="MisDescargas2sss"
DESTINATION_PATH = os.path.join(os.path.expanduser('~'), DESTINATION_FOLDER_NAME)
SOURCE_PATH =os.path.join(os.path.expanduser('~'), 'Downloads')

TO_REMOVE_EXTENSIONS = ['crdownload',]

FOLDER_NAMES = {
    "programs": ['exe','msi',],
    "video":    ['MP4','AVI','MOV','MKV','WMV','FLV','MPEG','webm',],
    "audio":    ['MP3','WAV','FLAC','AAC','OGG','M4A','AIFF',],
    "docs":     ['DOC','DOCX','PDF','TXT','XLS','XLSX','PPT','PPTX','CSV','RTF','ODT',],
    "img":      ['JPEG','JPG','PNG','GIF','BMP','TIFF','SVG','WebP',],
    "compressed":['zip', 'rar','7z',],
    "folders": [],
    "others": []
}

folders = list(FOLDER_NAMES.keys())

"""
crear carpetas si no existen
"""    
for f in folders:
    new_folder = f"{DESTINATION_PATH}/{f}"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

if not os.path.exists(SOURCE_PATH):
    raise ValueError("No se encontro la carpeta de origen")


"""
eliminarmos archivos que no interezan
"""
for extension in TO_REMOVE_EXTENSIONS:
    patron_archivos = f'{SOURCE_PATH}/*.{extension.lower()}'
    archivos_to_TO_REMOVE_EXTENSIONSd = glob.glob(patron_archivos)
    for file in archivos_to_TO_REMOVE_EXTENSIONSd:
        os.remove(file)

"""
movemos las carpetas
"""
elementos = os.listdir(SOURCE_PATH)

# Filtra los elementos que son carpetas
folders_to_moved = [elemento for elemento in elementos if os.path.isdir(os.path.join(SOURCE_PATH, elemento))]

# Imprime los nombres de las carpetas
for folder in folders_to_moved:
    shutil.move(f"{SOURCE_PATH}/{folder}", f"{DESTINATION_PATH}/folders")

"""
mover los archivosa sus carpetas correspondientes
"""
for f in folders:
    for extension in FOLDER_NAMES[f]:
        patron_archivos = f'{SOURCE_PATH}/*.{extension.lower()}'

        archivos_to_moved = glob.glob(patron_archivos)

        for file in archivos_to_moved:
            archivo_destino = os.path.join(DESTINATION_PATH, f, os.path.basename(file))
            
            if not os.path.exists(archivo_destino):
                shutil.move(file, archivo_destino)
            else:
                # Generar un nuevo nombre de archivo único
                nombre_base, extension = os.path.splitext(os.path.basename(file))
                contador = 1
                nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                nuevo_archivo_destino = os.path.join(DESTINATION_PATH, f, nuevo_nombre)
                
                # Incrementar el contador hasta encontrar un nombre único
                while os.path.exists(nuevo_archivo_destino):
                    contador += 1
                    nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                    nuevo_archivo_destino = os.path.join(DESTINATION_PATH, f, nuevo_nombre)
                
                # Mover el archivo con el nuevo nombre
                shutil.move(file, nuevo_archivo_destino)
