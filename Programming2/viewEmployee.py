import dataforp2

def view_employees():
    if not dataforp2.employees:
        print("\t\t\t\t\t\tLoad employees first!")
        return

    status_filter = input("\t\t\t\t\t\tFilter (Active/On Leave/Terminated/All): ")

    for worker in dataforp2.employees:
        # Skip if it doesn't match filter
        if status_filter.lower() != "all" and worker["Status"].lower() != status_filter.lower():
            continue
        print("\n\t\t\t\t\t\t------------------")
        print(f"\t\t\t\t\t\tID    : {worker['EmployeeID']}")
        print(f"\t\t\t\t\t\tName  : {worker['FullName']}")
        print(f"\t\t\t\t\t\tRole  : {worker['Role']}")
        print(f"\t\t\t\t\t\tStatus: {worker['Status']}")
if __name__ == '__main__':
    view_employees()