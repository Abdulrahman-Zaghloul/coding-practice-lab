file_path = "python/project_02_csv_analyzer/data/employees.csv"

employee_count = 0
total_salary = 0
department_totals = {}

with open(file_path, "r") as file:
    header = file.readline()

    for line in file:
        employee_count += 1

        line_items = line.strip().split(",")

        department = line_items[2]
        salary = int(line_items[3])

        total_salary += salary

        if department not in department_totals:
            department_totals[department] = 0

        department_totals[department] += salary

print(f"Total Employees: {employee_count}")
print(f"Total Salary: {total_salary}")
print(f"Average Salary: {total_salary / employee_count}")

print()

for department, salary_total in department_totals.items():
    print(f"{department}: {salary_total}")
