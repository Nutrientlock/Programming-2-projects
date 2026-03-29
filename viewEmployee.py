import dataforp2
import csv
import time

def load_payroll_history():
    payroll_history = {}
    try:
        with open("payroll.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["date", "EmployeeID", "hours", "rate", "gross", "nis", "tax", "net"])
            for row in reader:
                # CSV format: Date, EmployeeID, Hours, Rate, Gross, NIS, Tax, Net
                emp_id = row["EmployeeID"]
                payslip = {
                    "date": row["date"],
                    "hours": row['hours'] ,
                    "rate": row['rate'],
                    "gross": row['gross'],
                    "nis": row['nis'],
                    "tax": row['tax'],
                    "net": row["net"]
                }
                if emp_id not in payroll_history:
                    payroll_history[emp_id] = []
                payroll_history[emp_id].append(payslip)
    except FileNotFoundError:
        pass  # no payroll yet
    return payroll_history

def payroll_summary():
    payroll_history = load_payroll_history()
    if not payroll_history:
        print("\t\t\t\t\t\tNo payroll records found!\n")
        return

    overall_gross = 0
    overall_nis = 0
    overall_tax = 0
    overall_net = 0

    print("\n\t\t\t\t\t\t--- Payroll Summary Report ---\n")
    for worker in dataforp2.employees:
        emp_id = worker["EmployeeID"]
        payslips = payroll_history.get(emp_id, [])
        if not payslips:
            continue

        total_gross = sum(float(p['gross']) for p in payslips)
        total_nis = sum(float(p['nis']) for p in payslips)
        total_tax = sum(float(p['tax']) for p in payslips)
        total_net = sum(float(p['net']) for p in payslips)

        overall_gross += total_gross
        overall_nis += total_nis
        overall_tax += total_tax
        overall_net += total_net

        print(f"\t\t\t\t\t\tEmployee: {worker['FullName']} (ID: {emp_id})")
        print(f"\t\t\t\t\t\tTotal Gross Pay       : {total_gross:0.2f}")
        print(f"\t\t\t\t\t\tTotal NIS Deduction   : {total_nis:0.2f}")
        print(f"\t\t\t\t\t\tTotal Education Tax   : {total_tax:0.2f}")
        print(f"\t\t\t\t\t\tTotal Net Pay         : {total_net:0.2f}\n")
    print("\t\t\t\t\t\t---------------------------------------------")
    print(f"\t\t\t\t\t\tOverall Gross Pay       : {overall_gross:.2f}")
    print(f"\t\t\t\t\t\tOverall NIS Deduction   : {overall_nis:.2f}")
    print(f"\t\t\t\t\t\tOverall Education Tax   : {overall_tax:.2f}")
    print(f"\t\t\t\t\t\tOverall Net Pay         : {overall_net:.2f}\n")


def view_employees():
    if not dataforp2.employees:
        print("\t\t\t\t\t\tLoad employees first!")
        return

    payroll_history = load_payroll_history()  # load full payroll history

    status_filter = input("\t\t\t\t\t\tFilter (Active/Leave/Terminated/All): ")

    for worker in dataforp2.employees:
        if status_filter.lower() != "all" and worker.get("Status", "N/A").lower() != status_filter.lower():
            continue

        print("\n\t\t\t\t\t\t------------------")
        print(f"\t\t\t\t\t\tID    : {worker.get('EmployeeID', 'N/A')}")
        time.sleep(0.3)
        print(f"\t\t\t\t\t\tName  : {worker.get('FullName', 'N/A')}")
        time.sleep(0.3)
        print(f"\t\t\t\t\t\tRole  : {worker.get('Role', 'N/A')}")
        time.sleep(0.3)
        print(f"\t\t\t\t\t\tStatus: {worker.get('Status', 'N/A')}")
        time.sleep(0.3)
        print(f"\t\t\t\t\t\tHourly Rate: {worker.get('HourlyRate', 'N/A')}")

        emp_id = worker.get("EmployeeID")
        emp_payslips = payroll_history.get(emp_id, [])

        if emp_payslips:
            last = emp_payslips[-1]  # get the most recent payslip
            print(f"\n\t\t\t\t\t\t--- Last Payroll Record ---")
            print(f"\t\t\t\t\t\tLast Paid Date : {last["date"]}")
            print(f"\t\t\t\t\t\tHours Worked   : {last['hours']}")
            print(f"\t\t\t\t\t\tHourly Rate    : {last['rate']}")
            print(f"\t\t\t\t\t\tGross Pay      : {last['gross']}")
            print(f"\t\t\t\t\t\tNIS            : {last['nis']}")
            print(f"\t\t\t\t\t\tEducation Tax  : {last['tax']}")
            print(f"\t\t\t\t\t\tNet Pay        : {last['net']}\n")
            time.sleep(0.2)
        else:
            print(f"\n\t\t\t\t\t\t--- Last Payroll Record ---")
            print("\t\t\t\t\t\tLast Paid Date : None")
            print("\t\t\t\t\t\tHours Worked   : None")
            print("\t\t\t\t\t\tHourly Rate    : None")
            print("\t\t\t\t\t\tGross Pay      : None")
            print("\t\t\t\t\t\tNIS            : None")
            print("\t\t\t\t\t\tEducation Tax  : None")
            print("\t\t\t\t\t\tNet Pay        : None")
if __name__ == "__main__":
    view_employees()