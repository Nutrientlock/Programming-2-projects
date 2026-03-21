import dataforp2

def view_employees():
    if not dataforp2.employees:
        print("Load employees first!")
        return

    status_filter = input("Filter (Active/On Leave/Terminated/All): ")

    for worker in dataforp2.employees:
        # Skip if it doesn't match filter
        if status_filter.lower() != "all" and worker["Status"].lower() != status_filter.lower():
            continue
        print("\n------------------")
        print(f"ID    : {worker['EmployeeID']}")
        print(f"Name  : {worker['FullName']}")
        print(f"Role  : {worker['Role']}")
        print(f"Status: {worker['Status']}")
if __name__ == '__main__':
    view_employees()