import psycopg2

def obtener_conexion():
    """
    Establece una conexión a la base de datos PostgreSQL.
    """
    conn = psycopg2.connect(
        host="localhost",  # Dirección del servidor de la base de datos
        dbname="Interfaces",  # Nombre de la base de datos
        user="postgres",  # Usuario de la base de datos
        password="1234"  # Contraseña del usuario
    )
    return conn

def crear_tabla_ractividades():
    """
    Crea la tabla Ractividades si no existe.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Ractividades (
            CI VARCHAR(20) PRIMARY KEY,
            Tiempo_total_ojos_cerrados INT,
            Parpadeos_totales INT,
            Porcentaje_ojos_cerrados FLOAT
        );
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla Ractividades creada exitosamente.")

def guardar_datos_actividad(ci, tiempo_ojos, parpadeos, porcentaje):
    """
    Guarda los datos de la actividad (somnolencia) en la base de datos.
    
    :param ci: El CI del usuario
    :param tiempo_ojos: El tiempo total en que los ojos estuvieron cerrados
    :param parpadeos: La cantidad total de parpadeos
    :param porcentaje: El porcentaje de ojos cerrados durante el análisis
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    # Insertar los datos en la tabla Ractividades (siempre se insertan, sin importar si ya existen)
    cursor.execute('''
        INSERT INTO Ractividades (CI, Tiempo_total_ojos_cerrados, Parpadeos_totales, Porcentaje_ojos_cerrados)
        VALUES (%s, %s, %s, %s);
    ''', (ci, tiempo_ojos, parpadeos, porcentaje))
    
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Datos de actividad guardados correctamente para CI: {ci}.")

if __name__ == "__main__":
    # Crear la tabla si no existe
    crear_tabla_ractividades()
