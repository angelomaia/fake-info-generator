import sqlite3
from faker import Faker
import time

# create a Faker instance
fake = Faker()

# create a connection to the database
conn = sqlite3.connect('citizens.db')
c = conn.cursor()

# create a table to store the citizen information
c.execute('''CREATE TABLE IF NOT EXISTS citizens
             (id INTEGER PRIMARY KEY,
             name TEXT,
             birth_date TEXT,
             nationality TEXT,
             gender TEXT,
             phone_number TEXT,
             address TEXT)''')

while True:
    # generate 10 sets of fake citizen information and insert them into the table
    for i in range(10):
        name = fake.name()
        birth_date = fake.date_of_birth()
        nationality = fake.country()
        gender = fake.random_element(elements=('Male', 'Female'))
        phone_number = fake.phone_number()
        address = fake.address()
        c.execute('''INSERT INTO citizens (name, birth_date, nationality, gender, phone_number, address)
                     VALUES (?, ?, ?, ?, ?, ?)''', (name, birth_date, nationality, gender, phone_number, address))

    # commit the changes and wait for 30 seconds before inserting the next 10 entries
    conn.commit()
    time.sleep(30)

# close the connection
conn.close()
