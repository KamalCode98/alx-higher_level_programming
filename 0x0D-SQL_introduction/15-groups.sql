-- Lists the number of records for each score in second_table, ordered by the number of records in descending order
-- Execution 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
