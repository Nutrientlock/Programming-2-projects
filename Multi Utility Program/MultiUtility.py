#importing other 
import calculator
import games
import time
import to_do_list
import tracker

#functions for multi calculator
def add_num():
    result = []
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 + num2
        result.append(num1)
        for item in result:
            print(f"Result: {num1}\n")
    

    print('All Results: ',result)


def sub_num():
    result = []
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 - num2
        result.append(num1)
        for item in result:
            print(f"Result: {num1}\n")
    

    print('All Results: ',result)


def mul_num():
    result = []
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 * num2
        result.append(num1)
        for item in result:
            print(f"Result: {num1}\n")
    

    print('All Results: ',result)


def div_num():
    result = []
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        if num2 == 0:
            print("Cannot divide by zero\n")
        else:
            num1 = num1 / num2
            result.append(num1)
        for item in result:
            print(f"Result: {num1}\n")
    

    print('All Results: ',result)


def power_num():
    result = []
    num1 = float(input("Enter start number: "))
    num_of_cal = int(input("How many calculations do you want to perform: "))

    for i in range(num_of_cal):
        num2 = float(input(f"Calculation {i+1} - Enter the next number: "))
        num1 = num1 ** num2
        result.append(num1)
        for item in result:
            print(f"Result: {num1}\n")
    

    print('All Results: ',result)


#multi calculator
def multi_calculation():
    while True:
        print("=== Multi Calculation Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print('6. View all Saved')
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

#even/odd checker
def even_odd_checker():
    while True:
        print('\n===Even/Odd Checker===\n')
        print('Choose an option\n')
        print('1.Check if even or odd')
        print('q.Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        try:
            if choice == 'q':
                print('Exiting Even/Odd Checker. Goodbye!\n')
                break
            elif choice == '1':
                checker_num = float(input('Enter a number to check if its even or odd:'))
                if checker_num % 2 == 0:
                    print(f'{checker_num} is an Even number.\n')
                else:
                    print(f'{checker_num} is an Odd number.\n')     
        except ValueError:   
            print('Invaild')

#unit converter
def unit_converter():
    while True:
        print('\n===Unit Converter===\n')
        print('Chosse an Option\n')
        print('1. Convert kilometers to miles')
        print('2. Convert miles to kilometers')
        print('q. Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting Unit Converter. Goodbye!\n')
            break

        elif choice == '1':
            km = float(input('Enter distance in kilometers: '))
            miles = km / 1.621371
            print(f'{km} kilometers is equal to {miles:.2f} miles.\n')

        elif choice == '2':
            miles = float(input('Enter distance in miles: '))
            km = miles * 1.621371
            print(f'{miles} miles is equal to {km:.2f} kilometers.\n')

#the utility program
while True:
    print('\n===Welcome to the Multi-Utility Program!===\n')
    print('Please select a utility')
    print('1. Calculator')
    print('2. even/odd Checker')    
    print('3. unit converter')
    print('4. Multi Calculation') 
    print('5. Games')
    print('6. To Do List')
    print('7. Tracker')
    print('q. Exit') 
    print('------------------------------')
    user_choice = input('Your choice: ').strip().lower()
    print("\n------------------------------\n")
    if user_choice == 'q':
        print('Exiting the Multi-Utility Program. Goodbye!\n')
        break
        
    if user_choice == '1':
        calculator.calculator()
    elif user_choice == '2': 
        even_odd_checker()
    elif user_choice == '3':
        unit_converter()
    elif user_choice == '4':
        multi_calculation()
    elif user_choice == '5':
        games.gamemodes()
    elif user_choice == '6':
        to_do_list.to_do()
    elif user_choice == '7':
        tracker.menu()
    else:
        print('Invaild Input')  