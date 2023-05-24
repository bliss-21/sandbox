import os
import glob
import shutil

DESTINATION_FOLDER_NAME ="Oraganizador"
DESTINATION_PATH = os.path.join(os.path.expanduser('~'), DESTINATION_FOLDER_NAME)
SOURCE_PATH =os.path.join(os.path.expanduser('~'), 'Downloads')

TO_REMOVE_EXTENSIONS = ['crdownload',]

ORGANIZER_FOLDERS = {
    "programs": ['EXE','MSI',],
    "video":    ['MP4','AVI','MOV','MKV','WMV','FLV','MPEG','WEBM',],
    "audio":    ['MP3','WAV','FLAC','AAC','OGG','M4A','AIFF',],
    "docs":     ['DOC','DOCX','PDF','TXT','XLS','XLSX','PPT','PPTX','CSV','RTF','ODT',],
    "img":      ['JPEG','JPG','PNG','GIF','BMP','TIFF','SVG','WEBP',],
    "compressed":['zip', 'rar','7z',],
    "FOLDER_NAMES": [],
    "others": []
}

FOLDER_NAMES = list(ORGANIZER_FOLDERS.keys())

"""
Creamos las carpetas en los que organizaremos los archivos de la carpeta de origen,
si no existen las creamos basándonos en el diccionario, siendo el nombre de la carpeta,
cada llave y la lista que contiene será la extensión de cada archivo que tiene que guardar.
"""    
if not os.path.exists(SOURCE_PATH):
    raise ValueError("No se encontro la carpeta de origen")

for folder in FOLDER_NAMES:
    create_folder_path = f"{DESTINATION_PATH}/{folder}"
    os.makedirs(create_folder_path, exist_ok=True)

    
"""
Eliminamos archivos con la extensión que no interesan almacenados en la variable TO_REMOVE_EXTENSIONS,
en mi caso elimino las descargas incompletas.
"""

for extension in TO_REMOVE_EXTENSIONS:
    pattern = f'{SOURCE_PATH}/*.{extension.lower()}'
    files = glob.glob(pattern)
    for file in files:
        os.remove(file)


"""
Movemos las carpetas que puedan están dentro de mi carpeta de origen.
"""
folder_list = os.listdir(SOURCE_PATH)

# Filtra los elementos que son carpetas
folders_to_move = [folder for folder in folder_list if os.path.isdir(os.path.join(SOURCE_PATH, folder))]

# movemos las carpetas a la carpeta de destino
for folder in folders_to_move:
    shutil.move(f"{SOURCE_PATH}/{folder}", f"{DESTINATION_PATH}/FOLDER_NAMES")


"""
Movemos los archivos a las carpetas correspondientes dependiendo su extensión.
"""
for folder in FOLDER_NAMES:
    for extension in ORGANIZER_FOLDERS[folder]:
        pattern = f'{SOURCE_PATH}/*.{extension.lower()}'

        files_with_pattern = glob.glob(pattern)

        for file in files_with_pattern:
            file_destination = os.path.join(DESTINATION_PATH, folder, os.path.basename(file))
            
            if not os.path.exists(file_destination):
                shutil.move(file, file_destination)
            else:
                # Generar un nuevo nombre de archivo único
                base_name, extension = os.path.splitext(os.path.basename(file))
                count = 1
                rename_name = f"{base_name}_{count}{extension}"
                file_destination = os.path.join(DESTINATION_PATH, folder, rename_name)
                
                # Incrementar el contador hasta encontrar un nombre único
                while os.path.exists(file_destination):
                    count += 1
                    rename_name = f"{base_name}_{count}{extension}"
                    file_destination = os.path.join(DESTINATION_PATH, folder, rename_name)
                
                # Mover el archivo con el nuevo nombre
                shutil.move(file, file_destination)
