-- Write your query below

SELECT w.name as warehouse_name, 
        SUM(w.units*p.width*p.length*p.height) as volume
FROM warehouse w
JOIN products p on w.product_id = p.product_id
GROUP BY w.name