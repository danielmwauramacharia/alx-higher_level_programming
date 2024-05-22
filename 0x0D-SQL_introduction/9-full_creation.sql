#!/bin/bash
-- create a table and insert data
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (1, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (1, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (1, 'George', 8);
