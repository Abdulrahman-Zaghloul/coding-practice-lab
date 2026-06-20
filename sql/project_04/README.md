# SQL Exercise 04 - Revenue by Customer

## Objective

Practice calculating total revenue by customer using SQL aggregation.

## Problem

Given a sales table, return each customer and their total revenue, sorted from highest to lowest.

## Concepts Practiced

- `SUM()`
- `GROUP BY`
- Column aliases with `AS`
- Sorting aggregated results with `ORDER BY`

## Solution

```sql
SELECT
    customer,
    SUM(amount) AS total_revenue
FROM sales
GROUP BY customer
ORDER BY total_revenue DESC;
```
## Key Takeaway

When using GROUP BY, selected columns must either be grouped or aggregated.