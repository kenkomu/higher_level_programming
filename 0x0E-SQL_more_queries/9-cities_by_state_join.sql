-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities, states INNER JOIN states s ON c.state_id = s.id ORDER BY c.id ASC;
