 -- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
CREATE TABLE second_table(id INT,name VARCHAR(256),score INT,)
SELECT * FROM (VALUES ROW(1, “John”,10), ROW(2,“Alex”,3), ROW(3,“Bob”,14), ROW(4, “George”,8)) AS v(id, name,score);

