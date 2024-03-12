-- Selects score and name from second_table where score is greater than or equal to 10, ordered by score in descending order
-- 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
