import psycopg2

def obtener_conexion():
    conn = psycopg2.connect(
        host="localhost",  # o la dirección de tu servidor
        dbname="Interfaces",  # Nombre de la base de datos
        user="postgres",  # Usuario
        password="1234"  # Contraseña Version Stalin: 1234
    )
    return conn

def crear_tabla_rtest():
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rtest (
            CI VARCHAR(20) PRIMARY KEY,
            Comisiones INT,
            Omisiones INT,
            T_promedio FLOAT
        );
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla Rtest creada exitosamente.")

if __name__ == "__main__":
    crear_tabla_rtest()
