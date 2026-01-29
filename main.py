import psycopg
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

try:
    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    ) as conn:

        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            print("Conexión exitosa. Resultado:", cur.fetchone())

except Exception as e:
    print("Error al conectar a la base de datos:")
    print(e)
