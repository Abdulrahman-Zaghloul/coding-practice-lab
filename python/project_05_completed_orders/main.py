orders = [
    {"order_id": 1, "status": "completed"},
    {"order_id": 2, "status": "pending"},
    {"order_id": 3, "status": "completed"},
    {"order_id": 4, "status": "cancelled"},
]

def get_completed_orders(orders, status):
    completed_orders = []
    for order in orders:
        if order["status"] == status:
            completed_orders.append(order)
    return completed_orders

print(get_completed_orders(orders, "completed"))

