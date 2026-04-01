import load_employees
import viewEmployee
import payroll
from colorama import Fore, Back, Style, init
init(autoreset=True)
import os
import time

def clear_screen():#rmr to check this
    if os.name == 'nt':
        time.sleep() 
        os.system('cls')

def menu():
    while True:
            print(Fore.CYAN + Style.BRIGHT +"\n\t\t\t\t\t\t========= PAYROLL SYSTEM =========")
            print(Fore.WHITE + "\t\t\t\t\t\t= 1. Load Employees              =")
            print(Fore.WHITE + "\t\t\t\t\t\t= 2. View Employee List          =")
            print(Fore.WHITE + "\t\t\t\t\t\t= 3. Calculate Payroll           =")
            print(Fore.WHITE + "\t\t\t\t\t\t= 4. View Payroll Summary Report =")
            print(Fore.WHITE + "\t\t\t\t\t\t= q. Exit                        =")
            print(Fore.CYAN + Style.BRIGHT +"\t\t\t\t\t\t==================================")

            choice = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\t\t\t\t\t\tEnter your choice: ").strip().lower()
            if choice == "q":
                print(Fore.GREEN +"\t\t\t\t\t\tExiting system...\n")
                break
            elif choice == "1":
                print(Fore.GREEN +"\t\t\t\t\t\tLoad Employees selected\n")
                load_employees.load_employees()
            elif choice == "2":
                print(Fore.GREEN +"\t\t\t\t\t\tView Employee List selected\n")
                viewEmployee.view_employees()
            elif choice == "3":
                print(Fore.GREEN +"\t\t\t\t\t\tCalculate Payroll selected\n")
                payroll.calculate_payroll()
               
            elif choice == "4":
                print(Fore.GREEN +"\t\t\t\t\t\tView Payroll Summary Report selected\n")
                viewEmployee.payroll_summary()
            else:
                print(Fore.RED+"\t\t\t\t\t\tInvalid choice! Try again...\n")
menu()