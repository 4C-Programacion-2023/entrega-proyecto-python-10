import sqlite3

conexion = sqlite3.connect('Usuarios.db')

conexion.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        correo TEXT
    )
''')
conexion.execute('INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)', ('Juan', 30, 'juan@example.com'))
conexion.execute('INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)', ('María', 25, 'maria@example.com'))
conexion.commit()
cursor = conexion.execute('SELECT * FROM usuarios')
for fila in cursor:
    print(fila)
conexion.close()
