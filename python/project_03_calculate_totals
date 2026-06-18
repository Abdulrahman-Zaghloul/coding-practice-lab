""" 
You are given this list of transactions:
Write a function that returns: 
{
    "Alice": 150,
    "Bob": 350,
    "Charlie": 300
}
"""

transactions = [
    {"customer": "Alice", "amount": 100},
    {"customer": "Bob", "amount": 250},
    {"customer": "Alice", "amount": 50},
    {"customer": "Charlie", "amount": 300},
    {"customer": "Bob", "amount": 100}
]


def calculate_totals(transactions):
    totals = {}

    for row in transactions:
        customer = row["customer"]
        amount = row["amount"]

        if customer in totals:
            totals[customer] += amount

        else:
            totals[customer] = amount

    print(totals)


calculate_totals(transactions)