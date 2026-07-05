SELECT s.name 

FROM sales_person as s


WHERE s.sales_id NOT IN (
    SELECT o.sales_id FROM orders as o, company as c
WHERE o.sales_id = s.sales_id AND o.com_id = c.com_id and c.name LIKE '%CRIMSON%'
) 