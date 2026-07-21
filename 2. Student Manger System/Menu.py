from classes import Student

def get_input(prompt):
    i = 0
    fristName = input('Enter frist name: ')
    lastName = input('Enter last name: ')

    while i < 3:
        grade = float(input('ENTER GRADE: '))
        self.grades.append(grade)
        i = i + 1
    


def menu():
    while True:
        print('1. ADD')
        print('2. AVERAGE')
        print('3. EXIT')

        choice = input("Enter a choice: ")

        match choice:
            case "1":
                print("You chose Add.")

                

            case "2":
                print("You chose Two.")
            case "q":
                print("You chose Exit.")
                break
            case _:
                print("Invalid choice.")