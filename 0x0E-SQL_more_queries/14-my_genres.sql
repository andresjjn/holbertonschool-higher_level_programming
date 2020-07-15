-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name FROM tv_genres, tv_show_genres, tv_shows WHERE tv_genres.id = tv_show_genres.genre_id 
AND tv_show_genres.show_id = tv_shows.id AND tv_shows.title = "Dexter" 
ORDER BY tv_genres.name ASC;
