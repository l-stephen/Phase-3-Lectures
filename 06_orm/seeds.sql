-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database

-- Drop tables
DROP TABLE students;
DROP TABLE courses;
DROP TABLE major;
-- create some tables

-- CREATE TABLE IF NOT EXISTS <tablename>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER
-- );
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
);


CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    topic TEXT
);

-- CREATE TABLE IF NOT EXISTS <tablename2>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER,
--     <tablename_id> INTEGER,
--     FOREIGN KEY (tablename_id) REFERENCES tablename(id)
-- );

CREATE TABLE IF NOT EXISTS major(
    id INTEGER PRIMARY KEY,
    course_id INTEGER,
    student_id INTEGER,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
-- insert some values into the database
INSERT INTO students(name , grade)
VALUES("Dylan",  3);

INSERT INTO students(name , grade)
VALUES("Chimey",  3);

INSERT INTO students(name , grade)
VALUES("Lydia",  3);

INSERT INTO students(name , grade)
VALUES("Kaleb",  3);

INSERT INTO courses(topic)
VALUES("Javascript");

INSERT INTO courses(topic)
VALUES("Python");

INSERT INTO courses(topic)
VALUES("Flask");

INSERT INTO courses(topic)
VALUES("HTML");

INSERT INTO courses(topic)
VALUES("CSS");

INSERT INTO courses(topic)
VALUES("React");

INSERT INTO major(course_id, student_id)
VALUES(1,1);

INSERT INTO major(course_id, student_id)
VALUES(1,2);

INSERT INTO major(course_id, student_id)
VALUES(1,3);

INSERT INTO major(course_id, student_id)
VALUES(2,2);

