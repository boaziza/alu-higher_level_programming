-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- Using only one SELECT statement
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
