WITH RankedData AS (
    SELECT 
        student_id, 
        exam_id,
        score, 
        ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rank_val
    FROM exam_results
)
SELECT student_id, exam_id, score 
FROM RankedData 
WHERE rank_val = 1;