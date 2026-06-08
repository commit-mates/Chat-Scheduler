import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def get_db_connection():
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        print("Database connected successfully")
        return conn

    except Exception as e:
        raise ConnectionError( f"Database connection failed: {e}") from e


def create_tables():
    try:
        conn = get_db_connection()

        cursor = conn.cursor()
        with open("sql/table_ddl.sql", "r") as file:
          create_tables_sql = file.read()

        cursor.execute(create_tables_sql)

        conn.commit()

        print("Tables created successfully")

    except Exception as e:
        raise Exception(f"Table creation failed: {e}") from e

    finally:
    
        cursor.close() if cursor else None
        
        conn.close() if conn else None
        print("Database connection closed")


if __name__ == "__main__":
    create_tables()
    