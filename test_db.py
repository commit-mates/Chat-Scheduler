"""from db import connect_db

conn = connect_db()

cursor = conn.cursor()

cursor.execute("SELECT version();")

print(cursor.fetchone())

cursor.close()
conn.close()
"""


from db import connect_db



conn =  connect_db()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS test_connection (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
""")

conn.commit()

print("Table created successfully!")

cursor.close()
conn.close()