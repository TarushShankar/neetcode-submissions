-- Write your query below

SELECT s.id, s.name 
FROM students s 
WHERE s.department_id IS NULL OR s.department_id NOT IN (
    SELECT id
    FROM departments
)