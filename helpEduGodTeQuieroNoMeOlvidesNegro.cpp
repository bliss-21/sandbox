/*
Aquí tienes un ejemplo de cómo podrías construir una estructura de orden 3 en C++ que cumple con los requisitos mencionados,
utilizando una celda compuesta por una matriz de orden 3 y una matriz de orden 2. El programa generará números aleatorios en
el rango de 8 a 50 para llenar las celdas y calculará el valor promedio por cada fila de cada celda:
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

const int SIZE1 = 3; // Tamaño de la estructura de orden 3
const int SIZE2 = 3; // Tamaño de la matriz de orden 3 en cada celda
const int SIZE3 = 2; // Tamaño de la matriz de orden 2 en cada celda

// Estructura de orden 3
struct Orden3 {
    int matriz3x3[SIZE2][SIZE2];
    int matriz2x2[SIZE3][SIZE3];
};

// Función para generar números aleatorios en el rango [min, max]
int generarNumeroAleatorio(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Función para calcular el valor promedio de una fila en la matriz de orden 3
double calcularPromedioFila(int fila, int matriz[SIZE2][SIZE2]) {
    double suma = 0.0;
    for (int j = 0; j < SIZE2; j++) {
        suma += matriz[fila][j];
    }
    return suma / SIZE2;
}

int main() {
    srand(time(0)); // Inicializar la semilla del generador de números aleatorios

    Orden3 estructura[SIZE1];

    // Llenar las celdas con números aleatorios
    for (int i = 0; i < SIZE1; i++) {
        for (int j = 0; j < SIZE2; j++) {
            for (int k = 0; k < SIZE2; k++) {
                estructura[i].matriz3x3[j][k] = generarNumeroAleatorio(8, 50);
            }
        }
        for (int j = 0; j < SIZE3; j++) {
            for (int k = 0; k < SIZE3; k++) {
                estructura[i].matriz2x2[j][k] = generarNumeroAleatorio(8, 50);
            }
        }
    }

    // Mostrar la matriz generada y calcular el promedio por fila
    for (int i = 0; i < SIZE1; i++) {
        std::cout << "Celda " << i + 1 << ":" << std::endl;

        std::cout << "Matriz de orden 3:" << std::endl;
        for (int j = 0; j < SIZE2; j++) {
            for (int k = 0; k < SIZE2; k++) {
                std::cout << estructura[i].matriz3x3[j][k] << " ";
            }
            std::cout << std::endl;
        }

        std::cout << "Matriz de orden 2:" << std::endl;
        for (int j = 0; j < SIZE3; j++) {
            for (int k = 0; k < SIZE3; k++) {
                std::cout << estructura[i].matriz2x2[j][k] << " ";
            }
            std::cout << std::endl;
        }

        std::cout << "Promedio por fila en la matriz de orden 3:" << std::endl;
        for (int j = 0; j < SIZE2; j++) {
            double promedio = calcularPromedioFila(j, estructura[i].matriz3x3);
            std::cout << "Fila " << j + 1 << ": " << promedio << std::endl;
        }

        std::cout << std::endl;
    }

    return 0;
}

/*
En este programa, se define la estructura de orden 3 llamada Orden3, que tiene dos matrices: matriz3x3 de orden 3 y matriz2x2 de orden 2. Luego, se crea un arreglo de Orden3 llamado estructura con tamaño 3.
La función generarNumeroAleatorio se utiliza para generar números aleatorios en el rango especificado.
El bucle for anidado se utiliza para llenar las celdas con números aleatorios utilizando la función generarNumeroAleatorio.
Después, se muestra la matriz generada y se calcula el promedio por fila en la matriz de orden 3 utilizando la función calcularPromedioFila. Se imprime el resultado en la consola.
Recuerda que al compilar y ejecutar el programa, los resultados pueden variar debido a la generación aleatoria de los números.
*/
