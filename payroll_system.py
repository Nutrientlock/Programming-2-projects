import load_employees
import viewEmployee
import payroll

def menu():
    while True:
            print("\t\t\t\t\t\t========= Payroll System =========")
            print("\t\t\t\t\t\t= 1. Load Employees              =")
            print("\t\t\t\t\t\t= 2. View Employee List          =")
            print("\t\t\t\t\t\t= 3. Calculate Payroll           =")
            print("\t\t\t\t\t\t= 4. View Payroll Summary Report =")
            print("\t\t\t\t\t\t= q. Exit                        =")
            print("\t\t\t\t\t\t==================================")

            choice = input("\t\t\t\t\t\tEnter your choice: ").strip().lower()
            if choice == "q":
                print("\t\t\t\t\t\tGoodbye!\n")
                break
            elif choice == "1":
                print("\t\t\t\t\t\tLoad Employees selected\n")
                load_employees.load_employees()
            elif choice == "2":
                print("\t\t\t\t\t\tView Employee List selected\n")
                viewEmployee.view_employees()
            elif choice == "3":
                print("\t\t\t\t\t\tCalculate Payroll selected\n")
                
            elif choice == "4":
                print("\t\t\t\t\t\tView Payroll Summary Report selected\n")
              
            else:
                print("\t\t\t\t\t\tInvalid choice\n")
menu()