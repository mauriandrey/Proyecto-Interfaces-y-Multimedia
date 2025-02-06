# db_connection.py
# Este archivo se utilizará en el futuro para manejar la conexión a la base de datos.

def connect_db():
    """
    Ejemplo de conexión utilizando sqlite3.
    """
    import sqlite3
    conn = sqlite3.connect('usuarios.db')
    return conn

def create_table():
    """
    Crea la tabla de usuarios si no existe.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            password TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Se podrán agregar más funciones para insertar, actualizar y consultar datos.
