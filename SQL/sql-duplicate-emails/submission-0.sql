-- Write your query below
SELECT DISTINCT p1.email 
FROM person p1
WHERE EXISTS (
    SELECT p2.id FROM person p2 WHERE p2.email = p1.email
    AND p1.id != p2.id
)