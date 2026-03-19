import load_employees
import viewEmployee

def menu():
    while True:
            print("=== Multi Calculation Calculator ===")
            print("1. Load Employees")
            print("2. View Employee List")
            print("3. Calculate Payroll")
            print("4. View Payroll Summary Report")
            print("q. Exit")

            choice = input("Enter your choice: ").strip().lower()
            if choice == "q":
                print("Goodbye!\n")
                break
            elif choice == "1":
                print("Load Employees selected\n")
                load_employees.load_employees()
            elif choice == "2":
                print("View Employee List selected\n")
                viewEmployee.view_employees()
            elif choice == "3":
                print("Calculate Payroll selected\n")
            elif choice == "4":
                print("View Payroll Summary Report selected\n")
            else:
                print("Invalid choice\n")
menu()