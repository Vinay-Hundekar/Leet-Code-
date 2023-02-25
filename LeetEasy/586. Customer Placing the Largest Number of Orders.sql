# Write your MySQL query statement below
Select customer_number 
From Orders 
GROUP BY customer_number 
ORDER BY Count(*) desc
LIMIT 1
;