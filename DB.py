import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('Govee')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE Devices(
Number VARCHAR(255),
 Location VARCHAR(255),
Code VARCHAR(255),
Model VARCHAR(255),
Min_T VARCHAR(255),
Max_T VARCHAR(255),
Min_H VARCHAR(255),
Max_H VARCHAR(255));
"""
cursor.execute(table)
# Queries to INSERT records.
cursor.execute('''INSERT INTO Devices VALUES ('1', 'test', 'A','ddd',10,20,50,60)''');


# Display data inserted
print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM Devices''')
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()