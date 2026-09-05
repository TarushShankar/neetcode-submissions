-- Write your query below


SELECT t.team_id, t.team_name, SUM(
    CASE WHEN t.team_id = m.host_team AND m.host_goals > m.guest_goals THEN 3
    WHEN t.team_id = m.guest_team AND m.guest_goals > m.host_goals THEN 3
    WHEN t.team_id = m.host_team AND m.host_goals = m.guest_goals THEN 1
    WHEN t.team_id = m.guest_team AND m.host_goals = m.guest_goals THEN 1
    ELSE 0 END
) as num_points 
FROM teams t LEFT JOIN matches m on t.team_id IN (m.host_team,m.guest_team)
GROUP BY t.team_id, t.team_name ORDER BY num_points DESC, team_id
