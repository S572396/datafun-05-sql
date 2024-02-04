# Project 5 Working with Databases and SQL
##Project Start:
create git hub respoitory : https://github.com/S572396/datafun-05-sql
git clone into VS 
 ##create virtual environment
 '''
 phython -m venv.venv
 '''
 ## activate virtual environment
 '''
 .\venv\Scripts\activate
 '''
 ## add git ignore file
 '''
 file add ".gitignore"
 '''
 ## Install requirements:
'''
my -m pip install pandas pyarrow
'''
## freeze requirments
'''
py -m pip freeze > requirements.txt

requirements.txt created
'''
## add files to source control
'''
git add .
'''
## commit changes to repository
'''
git commit -m "initial commit"
'''
## git push to repository
'''
git push -u origin main
'''
## install pandas
upgrade pip 
'''
pip install --upgrade pip
pip install pandas
'''
## freeze requirments
'''
py -m pip freeze > requirements.txt

requirements.txt updated
'''
## 2nd commit added to document 
use process of git add . 
git commit -m "commit for additon of pandas"
git push -u origin main

## Create csv files
authors.csv and books.csv files manaully created with file add.
data provided was copied and pasted.

## commit added to document additon of csv files
'''
git add ,
git commit -m "adding in authors.csv,aadding in books.csv"
git push -u origin main
'''
## Create a Database
file create book_manager.py
'''
import dependencies:
import sqlite3
import pandas as pd
import pathlib
'''
## create new python file
book_manager.py
import dependencies:
import sqlite3
import pandas as pd
import pathlib
import csv

## add coding
'''
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

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
    
    '''
## create sq tables:
'''
create_tables.sql

-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create the books table
-- Note that the books table has a foreign key to the authors table
-- This means that the books table is dependent on the authors table
-- Be sure to create the standalone authors table BEFORE creating the books table.

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create the authors table 
-- Note that the author table has no foreign keys, so it is a standalone table

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER
);
After adding your content in VS Code, use git to add / commit / and push your content to GitHub. 
'''

 