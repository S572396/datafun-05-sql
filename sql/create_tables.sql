
-- create_tables.sql

-- Create Authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL
);

-- Create Books table
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    publication_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Import data from CSV into Authors table
.mode csv
.import 'C:\Users\19564\Documents\datafun-05-sql\data\authors.csv' authors

-- Import data from CSV into Books table
.mode csv
.import 'C:\Users\19564\Documents\datafun-05-sql\data\books.csv' books


