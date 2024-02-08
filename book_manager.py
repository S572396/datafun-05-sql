## """This project will focus on practice with Python and SQL, creating a database,creating tables,and using various SQL functions and logging will be used."""


import sqlite3
import pandas as pd
import pathlib
import csv
import logging

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

##4.Logging
# Configure logging to write to a file named log.txt
log_file_path = pathlib.Path("log.txt")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
db_file = pathlib.Path("project.db")
logging.info(f"Log file created successfully in {log_file_path}")
print(f"Log file created successfully in {log_file_path}")

# Configure logging to write to a file named log.txt
log_file_path = pathlib.Path("log.txt")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
db_file = pathlib.Path("project.db")

# Log the start of the program
logging.info("Program started.")
# Log the end of the program
logging.info("Program  is near end.")

## SQL Operations Practice

# Connect to the SQLite database
connection = sqlite3.connect('project.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Insert 10 records into the 'authors' table
import sqlite3

import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('project.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the 'authors' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        first TEXT,
        last TEXT,
        genre TEXT
    )
''')

# Insert 10 records into the 'authors' table
import sqlite3
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('project.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the 'authors' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        first TEXT,
        last TEXT,
        genre TEXT
    )
''')

# Insert 10 records into the 'authors' table
authors_data = [
    ('Edgar', 'Allan Poe', 'horror'),
    ('Shirley', 'Jackson', 'horror'),
    ('John', 'Langam', 'horror'),
    ('Bram', 'Stoker', 'horror'),
    ('Stephen', 'King', 'horror'),
    ('Dean', 'Koontz', 'horror'),
    ('Mary', 'Shelley', 'horror'),
    ('Kayla', 'Chenault', 'horror'),
    ('Elizabeth', 'Gaskell', 'horror'),
    ('Linda', 'Addison', 'horror')
]

# Inserting records into the 'authors' table
cursor.executemany("INSERT INTO authors (first, last, genre) VALUES (?, ?, ?)", authors_data)

# Commit the changes
connection.commit()

# Log successful addition to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write('Authors and genres added successfully.\n')

## Update Statement    
import sqlite3
# Update the 'authors' table
with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE authors SET last='Langan' WHERE last='Langam' AND first='John'")
        connection.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

# Delete a Record from the 'books' table
import sqlite3

# Delete a Record from the 'books' table based on specific column values
with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM books WHERE title = '1984'")
        connection.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Execute the SQL query
cursor.execute("SELECT * FROM authors WHERE genre = 'horror'")
result = cursor.fetchall()

# Print the result
print(result)

# Print the result to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(str(result) + '\n')






























   







def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
