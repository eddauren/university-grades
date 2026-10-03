import os
import psycopg 
from dotenv import load_dotenv
load_dotenv()
conn_string = (
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"host={os.getenv('DB_HOST')}"
)
with psycopg.connect(conn_string) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT version()')
        result=cur.fetchone()[0]
        print(result)
