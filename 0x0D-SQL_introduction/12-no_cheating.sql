-- Updates the score of the row in second_table where name is 'Bob' to 10
-- cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

UPDATE second_table SET score = 10 WHERE name = 'Bob';
