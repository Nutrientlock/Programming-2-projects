import csv

class Tickets:
    
    
    def __init__(self, service, TicId, name, movie_cost, sitting_cost , snack_cost, sitNum):
        service = 300
        self.TicId = TicId
        self.name = name
        self.movie_cost = movie_cost
        self.sitting_cost = sitting_cost
        self.sitNum = sitNum
        self.snack_cost = snack_cost

        self.subtotal = self.movie_cost + self.sitting_cost + self.snack_cost
        self.tax = self.subtotal * 0.12
        self.final_total = self.subtotal + self.tax + service

    def loadFile(self):
        self.tickets= []
        try:
            with open('Tickets.csv', "r") as f:
                reader = csv.DictReader(f, fieldnames=[ 'TicId', 'name', 'cost', 'sitting_cost' , 'snack', 'sitNum'])
                for row in reader:
                        ticket = Tickets(
                            row["EmployeeID"],
                            row["FirstName"],
                            row["LastName"],
                            row["Role"],
                            row["Status"],
                            float(row["HourlyRate"] or 0),
                            float(row["HoursWorked"] or 0)
                        )
                        self.tickets.append(ticket) 
            if not self.tickets:
                print("No Tickets found!")
                return
            print(f"{len(self.tickets)} Employees loaded successfully!")

        except FileNotFoundError:
            print("Tickets file not found!")

    def delEmpFileData(self, TicId):
        try:
            with open('Tickets.csv', "w") as f:
                for ticket in self.tickets:
                        if ticket.TicId == TicId:
                            continue
                        line = (
                                ticket.TicId + "," +
                                ticket.name + "," +
                                ticket.snack_name + "," +
                                ticket.role + "," +
                                ticket.status + "," +
                                str(ticket.cost) + "," +
                                str(ticket.sitNum) + "," +
                                str(ticket.sitting_num)
                            )
                        f.write(line + "\n")
            
        except FileNotFoundError:
            print("Employees file not found!")  
   

        
        
        
    