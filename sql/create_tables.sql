
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


### SQL command practice
create_tables.sql - create your database schema using sql
insert_records.sql - insert at least 10 additional records into each table.
update_records.sql - update 1 or more records in a table.
delete_records.sql - delete 1 or more records from a table.
query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
query_filter.sql - use WHERE to filter data based on conditions.
query_sorting.sql - use ORDER BY to sort data.
query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.