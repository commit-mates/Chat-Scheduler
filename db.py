import psycopg2

DB_HOST="localhost"
DB_PORT=5432
DB_NAME="chatscheduler_db"
DB_USER="postgres"
DB_PASSWORD="654321"


try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")
    
    
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Employee(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,EMAIL TEXT NOT NULL)""")
conn.commit()
print("Table created successfully")

