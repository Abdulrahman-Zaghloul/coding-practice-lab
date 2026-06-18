# Python Exercise 03 - Calculate Transaction Totals

## Objective

Practice using:

* Functions
* Dictionaries
* Loops
* Conditional logic

## Problem

Given a list of transaction records, calculate the total amount spent by each customer.

### Input

```python
transactions = [
    {"customer": "Alice", "amount": 100},
    {"customer": "Bob", "amount": 250},
    {"customer": "Alice", "amount": 50},
    {"customer": "Charlie", "amount": 300},
    {"customer": "Bob", "amount": 100}
]
```

### Expected Output

```python
{
    "Alice": 150,
    "Bob": 350,
    "Charlie": 300
}
```

## Concepts Practiced

* Creating and calling functions
* Iterating through a list of dictionaries
* Checking if a key exists in a dictionary
* Updating dictionary values
* Building aggregation logic

## Solution

```python
def calculate_totals(transactions):
    totals = {}

    for row in transactions:
        customer = row["customer"]
        amount = row["amount"]

        if customer in totals:
            totals[customer] += amount
        else:
            totals[customer] = amount

    return totals


print(calculate_totals(transactions))
```

## Key Takeaway

Dictionaries are commonly used in data processing to group and aggregate records by a specific key. This pattern is frequently used in ETL pipelines and analytics workflows.
