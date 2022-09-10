-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(sr.rate) AS rating
FROM tv_shows s
LEFT JOIN tv_show_ratings sr ON s.id = sr.show_id
GROUP BY s.title
ORDER BY rating DESC;
