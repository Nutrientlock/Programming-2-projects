import csv
import dataforp2


def load_employees():
    dataforp2.employees = []

    try:
        with open("employee.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dataforp2.employees.append(row)

        print(f"{len(dataforp2.employees)} employees loaded.")

    except FileNotFoundError:
        print("employee.csv not found!")
if __name__ == '__main__':
    load_employees()