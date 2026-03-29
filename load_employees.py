import csv
import dataforp2

def load_employees():
    dataforp2.employees = []  

    try:
        with open("employee_records.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["EmployeeID","FirstName","LastName","Role","Status","HourlyRate"])

            for row in reader:
                worker = {
                    "EmployeeID": row["EmployeeID"],
                    "FullName": row["FirstName"].capitalize() + " " + row["LastName"].capitalize(),
                    "Role": row["Role"],
                    "Status": row["Status"].strip().upper(),
                    "HourlyRate": row["HourlyRate"]
                }
                dataforp2.employees.append(worker)

        print(f"\t\t\t\t\t\t{len(dataforp2.employees)} Employees loaded successfully!")

    except FileNotFoundError:
        print("\t\t\t\t\t\temployees not found!")
    except ValueError as e:
        print(f"\t\t\t\t\t\tError reading HourlyRate: {e}")

if __name__ == '__main__':
    load_employees()