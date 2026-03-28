import csv
import dataforp2


import csv
import dataforp2

def load_employees():
    dataforp2.employees = []  # reset list

    try:
        with open("employee_records.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["EmployeeID","FirstName","LastName","Role","Status"])
            for row in reader:
                worker = {
                    "EmployeeID": row["EmployeeID"],
                    "FullName": row["FirstName"].capitalize() + " " + row["LastName"].capitalize(),
                    "Role": row["Role"],
                    "Status": row["Status"].upper()   # ensure consistent casing for filtering
                }
                dataforp2.employees.append(worker)

        print(f"\t\t\t\t\t\t{len(dataforp2.employees)} employees loaded.")

    except FileNotFoundError:
        print("\t\t\t\t\t\temployees not found!")
if __name__ == '__main__':
    load_employees()