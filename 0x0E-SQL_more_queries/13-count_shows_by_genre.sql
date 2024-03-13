-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Execute :  13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
