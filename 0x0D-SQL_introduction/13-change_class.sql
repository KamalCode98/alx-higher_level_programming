-- Deletes rows from second_table where the score is less than or equal to 5
-- Execute cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

DELETE FROM seconde_table WHERE score <= 5;
