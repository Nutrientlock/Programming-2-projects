import csv
import data


def load_employees():
    data.employees = []

    try:
        with open("employee.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.employees.append(row)

        print(f"{len(data.employees)} employees loaded.")

    except FileNotFoundError:
        print("employee.csv not found!")
if __name__ == '__main__':
    load_employees()