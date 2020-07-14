-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT title, genre_id FROM tv_shows, tv_show_genres
WHERE  tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
