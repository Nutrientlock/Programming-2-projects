import csv

class Employee:

    def __init__(self,emp_Id,frist_name,last_name,role,status, hours_worked, hourly_rate):
        self.emp_Id = emp_Id
        self.frist_name = frist_name
        self.last_name = last_name
        self.role = role
        self.status = status
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        self.gross_pay = self.hours_worked * self.hourly_rate
        self.nis = self.gross_pay * 0.025
        self.edu_tax = (self.gross_pay - self.nis) * 0.0225
        self.net_pay = self.gross_pay - self.nis - self.edu_tax
        

    def calculate_GrossPay(self):
        return round(self.gross_pay, 2)
    
    def calculate_NIS(self):
        return self.nis
    
    def calculate_EduTax(self):
        return self.edu_tax
    
    def calculate_NetPay(self):
        return self.net_pay
    
    def complete_payslip(self):
        return self.gross_pay, self.nis, self.edu_tax, self.net_pay

    def DisplayInfo(self):
        print(f"-----------\nid: {self.emp_Id}\nname: {self.frist_name} {self.last_name}\nrole: {self.role}\nstatus: {self.status}") 
    
    def display_payroll(self):
        print(f"-----------\nid: {self.emp_Id}\nname: {self.frist_name} {self.last_name}\ngross pay: ${self.gross_pay}\nnet pay: ${self.net_pay}")
    

class PayrollSystem:
    def __init__(self):
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def deleteEmployee(self, employee_id):
        for employee in self.employees:
            if employee.emp_Id == employee_id:
                self.employees.remove(employee)
                print("Employee deleted successfully!")
                return

        print("Employee not found.") 
            
    def display_info(self):
        for employee in self.employees:
            if self.employees == None:
                print("NO EMPLOYEES FOUND")
                return
            employee.DisplayInfo()
        

    def calculate(self):
        for employee in self.employees:
            print("------------")
            print(employee.complete_payslip())

    def DisplayPayroll(self):
        for employee in self.employees:
            if self.employees == None:
                print("NO EMPLOYEES FOUND")
                return
            print("------------")
            employee.display_payroll()

    def saveToFile(self):
        try:
            with open('Employee_Data.csv', "a") as f:
                for employee in self.employees:
                    line = (
                        employee.emp_Id + "," +  
                        employee.frist_name + "," +
                        employee.last_name + "," +
                        employee.role + "," +
                        employee.status + "," +
                        str(employee.hourly_rate) + "," +
                        str(employee.hours_worked)
                    )
                    f.write(line + "\n")
        except FileNotFoundError:
            print("Employees file not found!")  
            
    def loadFile(self):
        self.employees = []
        try:
            with open('Employee_Data.csv', "r") as f:
                reader = csv.DictReader(f, fieldnames=["EmployeeID","FirstName","LastName","Role","Status","HourlyRate", "HoursWorked"])
                for row in reader:
                        employee = Employee(
                            row["EmployeeID"],
                            row["FirstName"],
                            row["LastName"],
                            row["Role"],
                            row["Status"],
                            float(row["HourlyRate"] or 0),
                            float(row["HoursWorked"] or 0)
                        )
                        self.employees.append(employee) 
            if not self.employees:
                print("No employees found!")
                return
            print(f"{len(self.employees)} Employees loaded successfully!")
            
        except FileNotFoundError:
            print("Employees file not found!")  
    
    def delEmpFileData(self, employee_id):
        try:
            with open('Employee_Data.csv', "w") as f:
                for employee in self.employees:
                        if employee.emp_Id == employee_id:
                            continue
                        line = (
                                employee.emp_Id + "," +
                                employee.frist_name + "," +
                                employee.last_name + "," +
                                employee.role + "," +
                                employee.status + "," +
                                str(employee.hourly_rate) + "," +
                                str(employee.hours_worked)
                            )
                        f.write(line + "\n")
            
        except FileNotFoundError:
            print("Employees file not found!")  
        
