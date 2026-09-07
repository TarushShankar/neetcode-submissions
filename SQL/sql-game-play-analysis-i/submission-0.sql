-- Write your query below

SELECT a.player_id, min(a.event_date) as first_login
FROM activity a
GROUP BY a.player_id