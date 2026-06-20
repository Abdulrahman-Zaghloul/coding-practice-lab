/*
sales
--------------------------------
order_id | customer | amount
1        | Alice    | 100
2        | Bob      | 250
3        | Alice    | 50
4        | Charlie  | 300
5        | Bob      | 100
*/

SELECT customer, 
       SUM(amount) AS total_revenue
FROM sales
GROUP BY customer
ORDER BY total_revenue DESC;