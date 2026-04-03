import dataforp2
import csv
from datetime import datetime
from colorama import Fore, Back, Style, init

init(autoreset=True)

def save_payroll(emp_id, hours, rate, gross, nis, tax, net):
    file_exists = False
    try:
        with open("payroll.csv", "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open("payroll.csv", "a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow(["Date","EmployeeID","Hours","Rate","Gross","NIS","Tax","Net"])

        writer.writerow([
            datetime.now().date(),
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
        print(Fore.RED + "\t\t\t\t\t\tLoad employees first!")
        return

    for worker in dataforp2.employees:

        # Only process ACTIVE employees
        if worker["Status"].upper() != "ACTIVE":
            continue

        try:
            hours = float(input(Fore.LIGHTCYAN_EX + f"\t\t\t\t\t\tEnter hours for {worker['FullName']}: "))
        except ValueError:
            print(Fore.RED + "\t\t\t\t\t\tInvalid input. Skipping employee.")
            continue

        rate = 10
        gross = hours * rate
        nis = gross * 0.025
        edu_tax = (gross - nis) * 0.0225
        net = gross - nis - edu_tax

        save_payroll(worker["EmployeeID"], hours, rate, gross, nis, edu_tax, net)

        print(Fore.CYAN + "\n\t\t\t\t\t\t--- Payroll Result ---")
        print(Fore.MAGENTA + f"\t\t\t\t\t\tName: {worker['FullName']}")
        print(Fore.WHITE + f"\t\t\t\t\t\tGross Pay: ${gross:.2f}")
        print(Fore.YELLOW + f"\t\t\t\t\t\tNIS: ${nis:.2f}")
        print(Fore.YELLOW + f"\t\t\t\t\t\tEducation Tax: ${edu_tax:.2f}")
        print(Fore.GREEN + f"\t\t\t\t\t\tNet Pay: ${net:.2f}\n")
if __name__ == '__main__':
    calculate_payroll()