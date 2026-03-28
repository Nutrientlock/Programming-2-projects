import dataforp2
import time

def view_employees():
    if not dataforp2.employees:
        print("\t\t\t\t\t\tLoad employees first!")
        return

    print(dataforp2.employees)
    status_filter = input("\t\t\t\t\t\tFilter (Active/On Leave/Terminated/All): ")

    for worker in dataforp2.employees:
        # Skip if it doesn't match filter
        if status_filter.lower() != "all" and worker.get("Status", "N/A").lower() != status_filter.lower():
            continue
        
        print("\n\t\t\t\t\t\t------------------")
        print(f"\t\t\t\t\t\tID    : {worker.get('EmployeeID', 'N/A')}")
        time.sleep(1)
        print(f"\t\t\t\t\t\tName  : {worker.get('FullName', 'N/A')}")
        time.sleep(1)
        print(f"\t\t\t\t\t\tRole  : {worker.get('Role', 'N/A')}")
        time.sleep(1)
        print(f"\t\t\t\t\t\tStatus: {worker.get('Status', 'N/A')}")
        
        
if __name__ == '__main__':
    view_employees()