# SQL Exercise 03 - Orders by Status

## Objective

Practice counting records by category using SQL.

## Problem

Given an orders table, count how many orders exist for each status.

## Concepts Practiced

- `COUNT()`
- `GROUP BY`
- Column aliases with `AS`
- Sorting results with `ORDER BY`

## Solution

```sql
SELECT
    status,
    COUNT(*) AS order_count
FROM orders
GROUP BY status
ORDER BY order_count DESC;
```
Key Takeaway

GROUP BY is used to group rows by category, and COUNT(*) counts how many records exist in each group.