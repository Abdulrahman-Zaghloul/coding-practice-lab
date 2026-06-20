orders = [
    {"order_id": 1, "status": "completed"},
    {"order_id": 2, "status": "pending"},
    {"order_id": 3, "status": "completed"},
    {"order_id": 4, "status": "cancelled"},
    {"order_id": 5, "status": "pending"},
]

def count_orders_by_status(orders):
    status_counts = {}
    for order in orders:
        status = order["status"]
        if status not in status_counts:
            status_counts[status] = 1
        else:
            status_counts[status] += 1
    return status_counts


print(count_orders_by_status(orders))