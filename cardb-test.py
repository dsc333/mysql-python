# DSC 333
# Test program for cardb database discussed
# in class.
# Required module: mysql-connector-python

import mysql.connector
import os

# Define environment variable DB_PASSWORD as
# MySQL password (or simply hardcode).  If
# hardcoded, do not post on public repo.
pw = os.environ.get('DB_PASSWORD')

# Connect to DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=pw,
  database="cardb"
)

# Create a cursor object for executing queries
mycursor = mydb.cursor()

car_name = input('Input car name: ')
query = f"SELECT Name, `Retail Price` FROM cars WHERE Name LIKE '{car_name}%'"

# Execute the SQL query
mycursor.execute(query)
results = mycursor.fetchall()

# Output fetched data
if results:
    for row in results:
        print(row)  # Each row is a tuple
else:
    print('No matching records found.')

mycursor.close()
mydb.close()
