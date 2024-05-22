#!/bin/bash
-- list all rows where name is not null or empty
-- order by a column values in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

