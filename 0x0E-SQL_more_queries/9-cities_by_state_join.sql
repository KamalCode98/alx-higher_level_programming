-- Script that lists all cities contained in the database hbtn_0d_usa.
-- Execution cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
