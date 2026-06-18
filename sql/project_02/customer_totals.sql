/*
sales
--------------------------------
order_id | customer | amount | city
1        | Alice    | 100    | Tampa
2        | Bob      | 250    | Miami
3        | Alice    | 50     | Tampa
4        | Charlie  | 300    | Orlando
5        | Bob      | 100    | Miami
*/

SELECT 
       customer,
       SUM(amount) AS total_sales 
FROM sales 
GROUP BY customer 
ORDER BY total_sales DESC;