# Project 02: CSV Analyzer

A beginner-friendly Python project that reads employee data from a CSV file and calculates basic salary analytics.

## Goal

Practice reading structured data from a file, parsing rows, and producing summary metrics.

## Features

- Counts total employees
- Calculates total salary
- Calculates average salary
- Aggregates salary totals by department

## Concepts Practiced

- File handling with `open()`
- Reading text files line by line
- Skipping CSV headers
- Splitting strings with `.split(",")`
- Type conversion with `int()`
- Dictionaries for grouping data
- Basic aggregation logic

## Example Output

```text
Total Employees: 5
Total Salary: 392000
Average Salary: 78400.0

Engineering: 185000
Sales: 142000
Marketing: 65000
```

## Data Engineering Connection
This project is a small ETL-style workflow

```
CSV file
  ↓
Read rows
  ↓
Parse fields
  ↓
Aggregate values
  ↓
Print metrics
```
