-- Create some test data
-- use .read to run this file!
DROP TABLE test;
DROP TABLE test2;

CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS test2(
    id INTEGER PRIMARY KEY,
    test_id INTEGER,
    FOREIGN KEY (test_id) REFERENCES test(id)
);

INSERT INTO test(name)
VALUES ("TEST");

INSERT INTO test2(test_id)
VALUES (1);