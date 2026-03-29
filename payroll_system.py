import load_employees
import viewEmployee
import payroll
from colorama import Fore, Back, Style, init
init(autoreset=True)

def menu():
    while True:
            
            print(Fore.BLACK + Back.YELLOW +"\n\t\t\t\t\t\t========= PAYROLL SYSTEM =========")
            print(Fore.GREEN +"\t\t\t\t\t\t= 1. Load Employees              =")
            print(Fore.GREEN +"\t\t\t\t\t\t= 2. View Employee List          =")
            print(Fore.GREEN +"\t\t\t\t\t\t= 3. Calculate Payroll           =")
            print(Fore.GREEN +"\t\t\t\t\t\t= 4. View Payroll Summary Report =")
            print(Fore.GREEN +"\t\t\t\t\t\t= q. Exit                        =")
            print(Fore.GREEN +"\t\t\t\t\t\t==================================")

            choice = input(Fore.RED +"\t\t\t\t\t\tEnter your choice: ").strip().lower()
            if choice == "q":
                print("\t\t\t\t\t\tExiting system...\n")
                break
            elif choice == "1":
                print("\t\t\t\t\t\tLoad Employees selected\n")
                load_employees.load_employees()
            elif choice == "2":
                print("\t\t\t\t\t\tView Employee List selected\n")
                viewEmployee.view_employees()
            elif choice == "3":
                print("\t\t\t\t\t\tCalculate Payroll selected\n")
                payroll.calculate_payroll()
               
            elif choice == "4":
                print("\t\t\t\t\t\tView Payroll Summary Report selected\n")
                viewEmployee.payroll_summary()
            else:
                print("\t\t\t\t\t\tInvalid choice! Try again...\n")
menu()