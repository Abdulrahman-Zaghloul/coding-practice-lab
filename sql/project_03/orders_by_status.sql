/* Input
orders
--------------------------------
order_id | status
1        | completed
2        | pending
3        | completed
4        | cancelled
5        | pending
*/

/* Output
status     | order_count
completed  | 2
pending    | 2
cancelled  | 1
*/


SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY order_count DESC;