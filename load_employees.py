import csv
import dataforp2


def load_employees():
    dataforp2.employees = []

    try:
        with open("employee_records.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dataforp2.employees.append(row)

        print(f"\t\t\t\t\t\t{len(dataforp2.employees)} employees loaded.")

    except FileNotFoundError:
        print("\t\t\t\t\t\temployees not found!")
if __name__ == '__main__':
    load_employees()