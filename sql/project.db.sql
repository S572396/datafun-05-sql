Schema Design:

Table 1: authors
Columns:
author_id (Primary Key, Integer)
author_name (Text)
genre(Text)


Table 2: books
Columns:
book_id (Primary Key, Integer)
title (Text)
publication_date (Date)
author_id (Foreign Key referencing authors)
rating (Text)

-- Insert authors data
INSERT INTO authors (author_name, genre) VALUES
    ('Edgar Allen, Poe', 'horror'),
    ('Shirley, Jackson', 'horror'),
    ('John Langam', 'horror'),
    ('Bram, Stoker', 'horror'),
    ('Stephen, King', 'horror'),
    ('Dean,Koontz','horror'),
    ('Marry, Shelley','horror'),
    ('Kayla, Chenault', 'horror')
    ('Elizabeth, Gaskell','horror')
    ('Linda, Addison', 'horror')

    UPDATE authors SET last= 'Langan'
    WHERE last= 'Langam' AND first = 'John'


-- Import data from CSV into Authors table
.mode csv
.import 'C:\Users\19564\Documents\datafun-05-sql\data\authors.csv' authors

-- Import data from CSV into Books table
.mode csv
.import 'C:\Users\19564\Documents\datafun-05-sql\data\books.csv' books
