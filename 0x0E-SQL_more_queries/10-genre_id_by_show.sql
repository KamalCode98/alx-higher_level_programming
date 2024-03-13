-- Lists all shows with at least one genre linked, displaying the show title and genre ID.
-- Results are sorted by show title and genre ID.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
