/* 
EXAMPLE TABLE

   sales
--------------------------------
order_id | customer | amount | city
1        | Alice    | 100    | Tampa
2        | Bob      | 250    | Miami
3        | Alice    | 50     | Tampa
4        | Charlie  | 300    | Orlando
5        | Bob      | 100    | Miami
*/

SELECT customer,
        amount,
        city 
FROM sales 
WHERE amount > 100 
ORDER BY amount DESC;