records = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": None},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": None},
]


def remove_missing_ages(records):
    cleaned_records = []

    for record in records:
        if record["age"] is not None:
            cleaned_records.append(record)

    return cleaned_records


print(remove_missing_ages(records))
