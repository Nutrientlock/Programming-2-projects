student = {
    "name": 'Karisa',
    "age" : 13,
    "score": 78
}

def display_profile(student):
    print("\n--- Student Profile ---")
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Score:", student["score"])

def update_score(student):
    new_score = int(input('Enter your new score: '))
    student["score"] = new_score
def menu():
    while True:
        print('\n===WELCOME===\n')
        print('Chosse an Option\n')
        print('1. View Profile')
        print('2. Update Score')
        print('q. Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting Unit Converter. Goodbye!\n')
            break
        elif choice == '1':
            display_profile(student)
        elif choice == '2':
            update_score(student)
        else:
            print('Invaild Input')

if __name__ == '__main__':
    menu()
