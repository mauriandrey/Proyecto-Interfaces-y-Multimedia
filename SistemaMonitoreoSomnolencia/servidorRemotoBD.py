import psycopg2

DATABASE_URL = "postgresql://postgres:yZKptOSfoKPZkqdJraujkIOTlFmuDCQP@mainline.proxy.rlwy.net:57794/railway"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Conexión exitosa a PostgreSQL en Railway")
except Exception as e:
    print("Error de conexión:", e)
