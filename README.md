# Project 5 Working with Databases and SQL

## Overview

""This project will demonstarte practice when working with Python and SQL.
2 Tables named authors and books will be used to show various SQL commands and function statements.""

# Project Setup:
create git hub respoitory : https://github.com/S572396/datafun-05-sql

git clone project into VS code

## create virtual environment using vs code and activate in terminal, add git ignore file
 '''
 phython -m venv.venv
 .\venv\Scripts\activate
 file add ".gitignore"
 '''
 ## Install requirements and freeze requirements
'''
my -m pip install pandas pyarrow
py -m pip freeze > requirements.txt

'''
## Add files to source control, commit and push to orign
'''
git add .
git commit -m "initial commit"
git push -u origin main
'''
## Install pandas and freeze requirements
'''
pip install --upgrade pip
pip install pandas
py -m pip freeze > requirements.txt
'''

# Project Start: Create csv files
authors.csv and books.csv files manaully created with file add.
data provided was copied and pasted.

## commit added to document additon of csv files
'''
git add ,
git commit -m "adding in authors.csv,adding in books.csv"
git push -u origin main
'''
## Create a Python Database
file created book_manager.py

## Import Dependencies for Python File
'''
import dependencies:
import sqlite3,
import pandas as pd,
import pathlib,
import csv,
import logging,

'''
# SQl files created
  project.db, projectdb.sql, insert_records.sql, insert_additonal_authors.sql, create_tables.sql

# Python File book_manager.py to create database, tables, files, logging and SQL Practice
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
# Create SQL tables:
'''
create_tables.sql

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    rating (REAL)
);

-- Create the authors table 
-- Note that the author table has no foreign keys, so it is a standalone table

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    genre (TEXT)

);
After adding your content in VS Code, use git to add / commit / and push your content to GitHub. 
'''
# Logging Implemented
configure logging to write a file named log.txt

log the start of the program usging logging.info().

log the end of the program using logging.info ().

log exceptions using logging.exception().

results print to log.txt

# SQL command practice-see code in book_manager.py
1.create_tables.sql - create your database schema using sql- Created projectdb.sql for schema map

2.insert_records.sql - insert at least 10 additional records into each table-Example of Insert 10 
records into the 'authors' table example with 10 authors and horror genre added

3.update_records.sql - update 1 or more records in a table.-Example John Lagam update to John Langan

4.delete_records.sql - delete 1 or more records from a table.-Example title "1984" deleted from books table

5.query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.

  -COUNT example for count of horror authors and science fictions authors

  -AVG example for AVG for rating column of books table

  -SUM example for SUM of rating column of books table

6.query_filter.sql - use WHERE to filter data based on conditions- Example of SELECT from authors WHERE genre= horror

7.query_sorting.sql - use ORDER BY to sort data.-Example of SELECT title FROM books ORDER BY title ASC

8.query_group_by.sql - use GROUP BY clause (and optionally with aggregation)-Example GROUP By year_published where year >1950

9.query_join.sql - use INNER JOIN operation-Example of INNER JOIN author_id from authors and books table

 #  Define Main Function for SQL Operations Script
I
    db_filepath = 'project.db'
    def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    logging.info("All SQL operations completed successfully, results to log.txt")   

# Project wrap up
   Last git add, git commit and push origin main completed
 