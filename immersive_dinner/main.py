from action import menu
from action import action
from action import course
from action import clear_screen
from action import bootdown_loading
config = {
    "real": {
        "warning_time": 10,
        "duration": "original"
    },

    "practice": {
        "warning_time": 3,
        "duration": 5
    }
}


def get_input(prompt):
    while True:
        try:
            choice = int(input(prompt))

            if choice != 1 and choice != 0:
                print('\t\t\t\tinvalid input, must be 1 or 0')
                continue

            return choice

        except ValueError:
            print("\t\t\t\tInvalid input. Please enter a number.")


def main():

    menu(course)

    choice = get_input( "\t\t\t\tEnter 1 for practice and 0 for real: ")

    mode = "practice" if choice == 1 else "real"
    
    clear_screen()

    action(course, config[mode])

    print("\t\t\t\tover")
    bootdown_loading() 


if __name__ == "__main__":
    main()