import os
import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row
load_dotenv()

def get_connection():
    string = (
        f"dbname={os.getenv('DB_NAME')} "
        f"user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')} "
        f"host={os.getenv('DB_HOST')}"
    )
    return psycopg.connect(string, row_factory=dict_row)