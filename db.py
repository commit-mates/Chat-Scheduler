import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect_db(retries=5, delay=3):
    for attempt in range(retries):
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
            )

            print("Connected to PostgreSQL successfully")
            return connection

        except Exception as error:
            print(f"Attempt {attempt + 1} failed: {error}")

            if attempt < retries - 1:
                time.sleep(delay)

    raise Exception("Database connection failed")