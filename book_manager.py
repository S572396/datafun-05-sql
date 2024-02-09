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
logging.info("All SQL operations completed successfully")

## SQL Operations Practice

# Connect to the SQLite database
connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Insert 10 records into the 'authors' table
import sqlite3
connection = sqlite3.connect('project.db')
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
connection = sqlite3.connect('project.db')
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

# Insert 10 records into the 'authors' table example
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

import sqlite3
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query with placeholders for values
query = "INSERT INTO authors (first, last, genre) VALUES (?, ?, ?)"
cursor.executemany(query, authors_data)
conn.commit()


# Log successful addition to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write('Authors and genres added successfully.\n')


## Update Records example  
import sqlite3
# Update the 'authors' table
with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE authors SET last='Langan' WHERE last='Langam' AND first='John'")
        connection.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

### Delete Records example
import sqlite3

with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM 'books' WHERE title = '1984'")
        rows_deleted = cursor.rowcount
        if rows_deleted > 0:
            print(f"Rows deleted: {rows_deleted}")
            # Log to log.txt
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Rows deleted: {rows_deleted}\n")
        else:
            print("No matching rows found for deletion.")
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # Log to log.txt
        with open('log.txt', 'a') as log_file:
            log_file.write(f"SQLite error: {e}\n")

## Using Query Statement WHERE

import sqlite3
connection = sqlite3.connect('project.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM authors WHERE genre = 'horror'")
result = cursor.fetchall()

# Print the result
print(result)

# Print the result to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(str(result) + '\n')

import sqlite3

connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Execute the SELECT query with ORDER BY
cursor.execute('SELECT title FROM books ORDER BY title ASC')

# Fetch the result
result = cursor.fetchall()

# Print the result
print(result)

# Print the result to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(str(result) + '\n')


## Using Aggreation Functions
    
import sqlite3

connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Query for horror genre count
cursor.execute("SELECT COUNT(*) FROM authors WHERE genre = 'horror'")
result_horror = cursor.fetchone()[0]
print(f"Count of authors in horror genre: {result_horror}")

# Query for science fiction genre count
cursor.execute("SELECT COUNT(*) FROM authors WHERE genre = 'science fiction'")
result_science_fiction = cursor.fetchone()[0]
print(f"Count of authors in science fiction genre: {result_science_fiction}")

# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Count of authors in horror genre: {result_horror}\n")
    log_file.write(f"Count of authors in science fiction genre: {result_science_fiction}\n")

#Using SUM
import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT SUM(rating) AS total_rating
FROM books;

"""

cursor.execute(query)
result = cursor.fetchone()

total_rating = result[0]
print(f"Total Rating: {total_rating}")
# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Total Rating: {total_rating}\n")

## Using AVG
    import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT AVG(rating) AS total_AVG
FROM books;
"""

cursor.execute(query)
result = cursor.fetchone()

total_AVG = result[0]
print(f"Total AVG: {total_AVG}")

# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Total AVG: {total_AVG}\n")


#Using ORDER BY
import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT year_published, COUNT(*) as book_count
    FROM books
    WHERE year_published > 1950
    GROUP BY year_published
    ORDER BY year_published;
"""

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Display or process the results and write to log.txt
with open('log.txt', 'a') as log_file:
    for row in results:
        print(f"Year Published: {row[0]}, Book Count: {row[1]}")
        log_file.write(f"Year Published: {row[0]}, Book Count: {row[1]}\n")

## Using INNER JOIN

import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT authors.first, authors.last, books.title, books.year_published, books.rating
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Author: {row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}")
    # Display or process the results and write to log.txt
with open('log.txt', 'a') as log_file:
    for row in results:
        print(f"Author: {row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}") 
        log_file.write(f"Author:{row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}")


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
logging.info("All SQL operations completed successfully")

## SQL Operations Practice

# Connect to the SQLite database
connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Insert 10 records into the 'authors' table
import sqlite3
connection = sqlite3.connect('project.db')
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
connection = sqlite3.connect('project.db')
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

# Insert 10 records into the 'authors' table example
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

import sqlite3
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query with placeholders for values
query = "INSERT INTO authors (first, last, genre) VALUES (?, ?, ?)"
cursor.executemany(query, authors_data)
conn.commit()


# Log successful addition to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write('Authors and genres added successfully.\n')


## Update Records example  
import sqlite3
# Update the 'authors' table
with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE authors SET last='Langan' WHERE last='Langam' AND first='John'")
        connection.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)

### Delete Records example
import sqlite3

with sqlite3.connect('project.db') as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM 'books' WHERE title = '1984'")
        rows_deleted = cursor.rowcount
        if rows_deleted > 0:
            print(f"Rows deleted: {rows_deleted}")
            # Log to log.txt
            with open('log.txt', 'a') as log_file:
                log_file.write(f"Rows deleted: {rows_deleted}\n")
        else:
            print("No matching rows found for deletion.")
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # Log to log.txt
        with open('log.txt', 'a') as log_file:
            log_file.write(f"SQLite error: {e}\n")

## Using Query Statement WHERE

import sqlite3
connection = sqlite3.connect('project.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM authors WHERE genre = 'horror'")
result = cursor.fetchall()

# Print the result
print(result)

# Print the result to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(str(result) + '\n')

import sqlite3

connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Execute the SELECT query with ORDER BY
cursor.execute('SELECT title FROM books ORDER BY title ASC')

# Fetch the result
result = cursor.fetchall()

# Print the result
print(result)

# Print the result to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(str(result) + '\n')


## Using Aggreation Functions
    
import sqlite3

connection = sqlite3.connect('project.db')
cursor = connection.cursor()

# Query for horror genre count
cursor.execute("SELECT COUNT(*) FROM authors WHERE genre = 'horror'")
result_horror = cursor.fetchone()[0]
print(f"Count of authors in horror genre: {result_horror}")

# Query for science fiction genre count
cursor.execute("SELECT COUNT(*) FROM authors WHERE genre = 'science fiction'")
result_science_fiction = cursor.fetchone()[0]
print(f"Count of authors in science fiction genre: {result_science_fiction}")

# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Count of authors in horror genre: {result_horror}\n")
    log_file.write(f"Count of authors in science fiction genre: {result_science_fiction}\n")

#Using SUM
import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT SUM(rating) AS total_rating
FROM books;

"""

cursor.execute(query)
result = cursor.fetchone()

total_rating = result[0]
print(f"Total Rating: {total_rating}")
# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Total Rating: {total_rating}\n")

## Using AVG
    import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT AVG(rating) AS total_AVG
FROM books;
"""

cursor.execute(query)
result = cursor.fetchone()

total_AVG = result[0]
print(f"Total AVG: {total_AVG}")

# Print the results to log.txt
with open('log.txt', 'a') as log_file:
    log_file.write(f"Total AVG: {total_AVG}\n")


#Using ORDER BY
import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT year_published, COUNT(*) as book_count
    FROM books
    WHERE year_published > 1950
    GROUP BY year_published
    ORDER BY year_published;
"""

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Display or process the results and write to log.txt
with open('log.txt', 'a') as log_file:
    for row in results:
        print(f"Year Published: {row[0]}, Book Count: {row[1]}")
        log_file.write(f"Year Published: {row[0]}, Book Count: {row[1]}\n")

## Using INNER JOIN

import sqlite3

# Establish a connection to your database
conn = sqlite3.connect("project.db")
cursor = conn.cursor()

# Your SQL query
query = """
    SELECT authors.first, authors.last, books.title, books.year_published, books.rating
    FROM authors
    INNER JOIN books ON authors.author_id = books.author_id;
"""

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Author: {row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}")
    # Display or process the results and write to log.txt
with open('log.txt', 'a') as log_file:
    for row in results:
        print(f"Author: {row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}") 
        log_file.write(f"Author:{row[0]} {row[1]}, Title: {row[2]}, Year Published: {row[3]}, Rating: {row[4]}")

# Log Completed Progress
logging.info("All SQL operations completed successfully")

def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    

if __name__ == "__main__":
    main()

  
    
   




































   









    















































   







def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
