import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except Exception as e:
    raise ConnectionError(f"Database connection failed: {e}") from e
  


def create_tables():
    
    cursor = None

    try:
        cursor = conn.cursor()

        with open("backend/sql/table_ddl.sql", "r") as file:
            create_tables_sql = file.read()

        cursor.execute(create_tables_sql)

        conn.commit()

        print(" Tables created successfully")

    except Exception as e:

        conn.rollback()

        raise Exception(f"Table creation failed: {e}")

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

        print("Database connection closed")


if __name__ == "__main__":
    create_tables()
