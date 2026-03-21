import dataforp2
import csv
from datetime import datetime

def save_payroll(emp_id, hours, rate, gross, nis, tax, net):

    with open("payroll.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().date(),  # today's date
            emp_id,
            hours,
            rate,
            gross,
            nis,
            tax,
            net
        ])

def calculate_payroll():   
    if not dataforp2.employees:
        print("Load employees first!")
        return

    for worker in dataforp2.employees:

        # Only process ACTIVE employees
        if worker["Status"] != "Active":
            continue

        try:
            hours = float(input(f"Enter hours for {worker['FullName']}: "))
        except ValueError:
            print("Invalid input. Skipping employee.")
            continue

        rate = float(worker["HourlyRate"])

        gross = hours * rate
        nis = gross * 0.025
        edu_tax = (gross - nis) * 0.0225
        net = gross - nis - edu_tax

        save_payroll(worker["EmployeeID"],hours,rate,gross,nis,edu_tax,net)

        print("\n--- Payroll Result ---")
        print(f"Name: {worker['FullName']}")
        print(f"Gross Pay: {gross:.2f}")
        print(f"NIS: {nis:.2f}")
        print(f"Education Tax: {edu_tax:.2f}")
        print(f"Net Pay: {net:.2f}")
if __name__ == '__main__':
    calculate_payroll()