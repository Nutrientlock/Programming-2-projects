from Employee_Class import Employee
from Employee_Class import PayrollSystem
 
system = PayrollSystem() 
system.loadFile()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_char_input(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Input cannot be empty")
        else:
            return value.capitalize()

def password(passcode, chances = 3):
    
    cheat = '0'
    for remaining in range(chances, 0, -1):
        attempt = input("Enter passcode: ").strip()

        if attempt == passcode :
            print("Access Granted")
            return True

        print("Invalid input")
        print(f"Number of chances left: {remaining - 1}")
    return False

def get_employee():
    frist_name = get_char_input("ENTER FIRST NAME: ")
    last_name = get_char_input("ENTER LAST NAME: ")
    emp_Id = get_char_input("ENTER ID NUMBER: ")
    role = get_char_input("ENTER ROLE: ")
    status = get_char_input("STATUS: ")

    hours_worked = get_int_input("ENTER HOURS WORKED: ")
    hourly_rate = get_int_input("ENTER HOURLY RATE: ")

    print("Employee added successfully!")
    e = Employee(emp_Id, frist_name, last_name, role, status, hours_worked, hourly_rate)
    return e

def get_Id_toDelete():
    Delete_Id = get_char_input('ENTER ID OF EMPLOYEE TO BE DELETED: ') 
    return Delete_Id
        
def menu():
    
    passcode = 'werty' 

    print("MENU STARTED")

    while True:
        print("____________________")
        print("|1. Add Employees   |")
        print("|2. Veiw Employees  |")
        print("|3. Run Payroll     |")
        print('|4. Delete Employee |')
        print("|q. Exit            |")
        print("|__________________ |")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("ADD EMPLOYEE SELECTED...")
            if not password(passcode) :
                print("Blocked")
                continue
            employee = get_employee()
            system.addEmployee(employee)
            system.saveToFile()

        elif choice == '2':
            print('VEIW EMPLOYEES SELECTED')   
            
            system.display_info()

        elif choice == '3':
            print('RUN PAYROLL SELECTED')
            system.DisplayPayroll()

        elif choice == '4':
            if not password(passcode) :
                print("Blocked")
                continue 
            employee_id = get_Id_toDelete()
            system.deleteEmployee(employee_id)
            system.delEmpFileData(employee_id)

        elif choice == 'q':
            print('BYE BYE')
            break
           
if __name__ == "__main__":
    menu()     
