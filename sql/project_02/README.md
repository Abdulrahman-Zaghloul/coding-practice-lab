# SQL Exercise 02 - Customer Totals

## Objective

Practice using SQL aggregation to calculate total sales by customer.

## Problem

Given a sales table, return each customer and their total sales amount.

## Concepts Practiced

- `SUM()`
- `GROUP BY`
- Column aliases with `AS`
- Sorting aggregated results with `ORDER BY`

## Solution

```sql
SELECT
    customer,
    SUM(amount) AS total_sales
FROM sales
GROUP BY customer
ORDER BY total_sales DESC;
```

## Key Takeaway

GROUP BY is used to combine rows into groups, and aggregate functions like SUM() calculate values for each group.