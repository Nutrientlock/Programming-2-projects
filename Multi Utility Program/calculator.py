#repeated: print result
#repeated: result calculation
#calculator: adds, subtracts, multiplies, divides, power, modular and exits

import os

def clear_screen():
    print("\n" * 50)  # Prints 50 blank lines


def add_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    result = num1 + num2
    print("Result is: ", result)

def sub_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    result = num1 - num2
    print("Result is: ", result)

def multi_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    result = num1 * num2
    print("Result is: ", result)

def div_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    if num2 == 0:
        print("Num 2 cannot be zero")
    else:
        result = num1 / num2
        print("Result is: ", result)

def power_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    result = num1 ** num2
    print("Result is: ", result)

def mod_num():
    num1 = float(input("Enter num 1: "))
    num2 = float(input("Enter num 2: "))
    result = num1 % num2
    print("Result is: ", result)

def calculator():
    while True:
        print("===Simple Integer Calculator===\n")
        print("What is your Choice")
        print("1, Addition")
        print("2, Subtraction")
        print("3, Multiplication")
        print("4, Division")
        print("5, Power")
        print("6, Modular")
        print('q, Exit')

        choice = input('Enter your choice: ').strip().lower()

        if choice == 'q':
            print('Exiting the calculator. Goodbye!')
            break


        if choice == '1':
            add_num()

        elif choice == '2':
            sub_num()
        elif choice == '3':
            multi_num(  )

        elif choice == '4':
            div_num()

        elif choice == '5':
            power_num()

        elif choice == '6':

            mod_num()

        else:
            print('Invalid input')
        
        input("\nPress Enter to continue...")  
        clear_screen()
            
if __name__ == '__main__':
    calculator()

    