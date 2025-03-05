import psycopg2

def obtener_conexion():
    """
    Establece una conexión a la base de datos PostgreSQL en Railway.
    """
    conn = psycopg2.connect(
        host="mainline.proxy.rlwy.net",  # Dirección del servidor de Railway
        dbname="railway",  # Nombre de la base de datos (verifícalo en el panel de Railway)
        user="postgres",  # Usuario predeterminado en Railway (o el que hayas creado)
        password="yZKptOSfoKPZkqdJraujkIOTlFmuDCQP",  # Contraseña proporcionada por Railway
        port=57794  # Puerto especificado por Railway
    )
    return conn

def crear_tabla_supertabla():
    """Crea la tabla 'supertabla' en la base de datos Railway."""
    try:
        # Establecemos la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()

        # Comando SQL para crear la tabla
        create_table_query = """
        CREATE TABLE IF NOT EXISTS supertabla (
            ci VARCHAR(20),
            nombre VARCHAR(100),
            tiempo_total_ojos_cerrados FLOAT,
            parpadeos_totales INT,
            porcentaje_ojos_cerrados FLOAT,
            comisiones INT,
            omisiones INT,
            t_promedio FLOAT,
            conclusion TEXT,
            fecha DATE
        );
        """

        # Ejecutar la consulta para crear la tabla
        cursor.execute(create_table_query)

        # Confirmamos la creación de la tabla
        conn.commit()
        print("Tabla 'supertabla' creada correctamente en la base de datos.")

    except Exception as error:
        print(f"Error al crear la tabla en la base de datos: {error}")

    finally:
        # Cerramos la conexión
        if conn:
            cursor.close()
            conn.close()

# Llamar a la función para crear la tabla
if __name__ == "__main__":
    crear_tabla_supertabla()
