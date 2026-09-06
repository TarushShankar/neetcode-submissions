-- Write your query below
WITH cte as(

    SELECT CASE WHEN user1_id = 1 THEN user2_id 
    WHEN user2_id = 1 THEN user1_id END AS friends FROM friendship
)

SELECT DISTINCT l.page_id as recommended_page
FROM likes l
WHERE l.user_id in (Select friends from cte)
AND l.page_id NOT in (Select page_id from likes l2 where l2.user_id = 1)