import time
import os

# Definir la representación ASCII art de la mascota en diferentes estados
estados_mascota = [
    r'''
   /\_/\  
  ( o.o )
   > ^ <
    ''',
    r'''
   /\_/\  
  ( o.o )
   U ^ U
    ''',
    r'''
   /\_/\  
  ( o.o )
   - ^ -
    ''',
    r'''
   /\_/\  
  ( o.o )
   * ^ *
    '''
]

# Variables de estado de la mascota
energia = 100
felicidad = 100

# Función para mostrar la animación
def mostrar_animacion():
    global energia, felicidad

    while True:
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostrar la mascota en cada estado
        for estado in estados_mascota:
            print(estado)
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Actualizar niveles de energía y felicidad
            energia -= 10
            felicidad -= 5

            if energia <= 0 or felicidad <= 0:
                print("Tu mascota se ha agotado o está triste. ¡Game Over!")
                return

# Función para alimentar a la mascota
def alimentar_mascota():
    global energia
    energia += 20
    print("Has alimentado a tu mascota. ¡Energía incrementada!")

# Función para jugar con la mascota
def jugar_con_mascota():
    global felicidad
    felicidad += 10
    print("Has jugado con tu mascota. ¡Felicidad incrementada!")

# Función principal
def main():
    while True:
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostrar opciones de interacción
        print("Bienvenido a tu mascota virtual")
        print("1. Alimentar a la mascota")
        print("2. Jugar con la mascota")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            alimentar_mascota()
        elif opcion == "2":
            jugar_con_mascota()
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

        # Hacer una pausa antes de mostrar la animación
        input("Presiona Enter para continuar...")
        mostrar_animacion()

# Llamar a la función principal
main()
