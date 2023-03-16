import sqlite3
import csv
import time

# Connect to the database
conn = sqlite3.connect('citizens.db')
c = conn.cursor()

# Define the name of the CSV file
csv_file = 'citizens.csv'

while True:
    # Fetch all rows from the citizens table
    c.execute('SELECT * FROM citizens')
    rows = c.fetchall()
    
    # Append the rows to the CSV file
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    # Wait for 10 seconds before fetching and appending the next set of rows
    time.sleep(10)
