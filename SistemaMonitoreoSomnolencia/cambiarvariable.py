import psycopg2

def cambiar_tipo_columna():
    try:
        # Establecemos la conexión a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host="mainline.proxy.rlwy.net",  # Dirección del servidor de Railway
            dbname="railway",  # Nombre de la base de datos (verifícalo en el panel de Railway)
            user="postgres",  # Usuario predeterminado en Railway (o el que hayas creado)
            password="yZKptOSfoKPZkqdJraujkIOTlFmuDCQP",  # Contraseña proporcionada por Railway
            port=57794  # Puerto especificado por Railway
        )
        cursor = connection.cursor()

        # Ejecutamos la consulta ALTER TABLE para cambiar el tipo de columna
        alter_query = """
        ALTER TABLE supertabla 
        ALTER COLUMN t_promedio TYPE DECIMAL;
        """
        cursor.execute(alter_query)

        # Confirmamos la operación
        connection.commit()
        print("El tipo de la columna t_promedio ha sido cambiado a DECIMAL.")

    except Exception as error:
        print(f"Error al cambiar el tipo de la columna: {error}")

    finally:
        # Cerramos la conexión
        if connection:
            cursor.close()
            connection.close()

# Llamamos a la función para cambiar el tipo de la columna
cambiar_tipo_columna()
