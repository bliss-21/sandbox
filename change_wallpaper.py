import subprocess
import os
import time

def change_wallpaper(image_path):
    try:
        # Ejecuta el comando 'gsettings' para cambiar el fondo de pantalla
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{image_path}'])
        print(f"Fondo de pantalla cambiado a: {image_path}")
    except Exception as e:
        print(f"Ocurrió un error al cambiar el fondo de pantalla: {e}")

if __name__ == "__main__":
    image_folder = "/ruta/a/tu/carpeta/de/imagenes"  # Ruta a la carpeta con las imágenes
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

    while True:
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            change_wallpaper(image_path)
            time.sleep(3600)  # Espera 1 hora (3600 segundos) antes de cambiar a la siguiente imagen
