-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database

-- Drop tables
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

-- create some tables

-- CREATE TABLE IF NOT EXISTS <tablename>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER
-- );

-- CREATE TABLE IF NOT EXISTS <tablename2>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER,
--     <tablename_id> INTEGER,
--     FOREIGN KEY (tablename_id) REFERENCES tablename(id)
-- );
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY,
    comment TEXT,
    post_id INTEGER,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

-- insert some values into the database
INSERT INTO posts(title)
VALUES("Intro to HTML/CSS");

INSERT INTO posts(title)
VALUES("CSS Best Practices");

INSERT INTO comments(comment, post_id)
VALUES("This was helpful~", 1);

INSERT INTO comments(comment, post_id)
VALUES("tailwind is better", 2);


