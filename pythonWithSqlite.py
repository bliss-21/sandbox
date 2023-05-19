import sqlite3

# Establecer conexión con la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')

# Crear una tabla en la base de datos
conexion.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
''')

# Insertar datos en la tabla
conexion.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('John Doe', 25))
conexion.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Jane Smith', 30))

# Guardar los cambios
conexion.commit()

# Consultar todos los registros de la tabla
resultado = conexion.execute('SELECT * FROM usuarios').fetchall()

# Imprimir los registros
for fila in resultado:
    print(f'ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}')

# Cerrar la conexión
conexion.close()
