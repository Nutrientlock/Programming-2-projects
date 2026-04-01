import csv
import dataforp2
from colorama import Fore, Back, Style, init
init(autoreset=True)

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

        print(Fore.GREEN+f"\t\t\t\t\t\t{len(dataforp2.employees)} Employees loaded successfully!")

    except FileNotFoundError:
        print(Fore.RED+"\t\t\t\t\t\temployees not found!")

if __name__ == '__main__':
    load_employees()