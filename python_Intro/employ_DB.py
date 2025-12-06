import _sqlite3

connection = _sqlite3.connect("Employee_DB.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
        First_Name TEXT,
        Last_Name  TEXT,
        Age        INTEGER,
        Income     REAL
               )


""")

connection.commit()

print("database and table created successfully")

connection.close()