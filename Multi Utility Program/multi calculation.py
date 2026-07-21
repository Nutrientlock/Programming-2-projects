def add_num():
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 + num2
        print(f"Result: {num1}\n")


def sub_num():
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 - num2
        print(f"Result: {num1}\n")


def mul_num():
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 * num2
        print(f"Result: {num1}\n")


def div_num():
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        if num2 == 0:
            print("Cannot divide by zero\n")
        else:
            num1 = num1 / num2
            print(f"Result: {num1}\n")


def power_num():
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 ** num2
        print(f"Result: {num1}\n")


def multi_calculation():
    while True:
        print("=== Multi Calculation Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("q. Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break
        elif choice == "1":
            add_num()
        elif choice == "2":
            sub_num()
        elif choice == "3":
            mul_num()
        elif choice == "4":
            div_num()
        elif choice == "5":
            power_num()
        else:
            print("Invalid choice\n")