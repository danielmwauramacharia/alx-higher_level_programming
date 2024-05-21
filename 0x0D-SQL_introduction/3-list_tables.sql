#!/bin/bash
-- list all tables in a database
database_name=$mysql
mysql -e "USE $database_name;  SHOW TABLES;"

