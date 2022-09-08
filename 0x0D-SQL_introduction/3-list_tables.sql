-- lists all the tables of a database in your MySQL server.
SELECT Table_name as TablesName from information_schema.tables where table_schema = 'mysql';
