import os

# Ejecutar el comando de actualización de paquetes usando el gestor de paquetes de Ubuntu (apt)
def update_packages():
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')

if __name__ == "__main__":
    update_packages()
