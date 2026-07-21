import os
import sys
import time
from colorama import Fore, Style, init
from timers import timer

init(autoreset=True)

tabs = "\t\t\t\t"


# Element colors
course_colors = {
    "Water": Fore.CYAN,
    "Earth": Fore.GREEN,
    "Fire": Fore.RED,
    "Air": Fore.WHITE
}


def boot_loading():

    print(Fore.CYAN + Style.BRIGHT + f"\n{tabs}BOOTING BYTE SYSTEM...\n")

    length = 30

    for i in range(length + 1):

        bar = "#" * i + "-" * (length - i)
        percent = int((i / length) * 100)

        sys.stdout.write(f"\r{tabs}[{bar}] {percent}%")

        sys.stdout.flush()
        time.sleep(0.06)
        

    print(Fore.GREEN + Style.BRIGHT + f"\n{tabs}SYSTEM READY\n")

def bootdown_loading():
    print(Fore.CYAN + Style.BRIGHT + f"\n{tabs}EXITING BYTE SYSTEM...\n")

    length = 30

    for i in range(length + 1):
        bar = "#" * i + "-" * (length - i)
        percent = int((i / length) * 100)

        sys.stdout.write(f"\r{tabs}[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.06)
    clear_screen()
        

def clear_screen():

    time.sleep(1)

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def cafe_header():

    header = [
        f"{tabs}██████╗ ██╗   ██╗████████╗███████╗     ",
        f"{tabs}██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝    ",
        f"{tabs}██████╔╝ ╚████╔╝    ██║   █████╗     ",
        f"{tabs}██╔══██╗  ╚██╔╝     ██║   ██╔══╝      ",
        f"{tabs}██████╔╝   ██║      ██║   ███████╗    ",
        f"{tabs}╚═════╝    ╚═╝      ╚═╝   ╚══════╝     "
    ]

    print(Fore.CYAN + Style.BRIGHT)

    for line in header:
        print(line)
        time.sleep(0.15)


course = [
    {
        "name": "Water",
        "type": "Seafood",
        "duration": 30,
        "goal": "Calm beginning.",
        "dish": "Fish tea"
    },
    {
        "name": "Earth",
        "type": "Plant-Based",
        "duration": 15,
        "goal": "Comfort + Stability.",
        "dish": "Prepare the fish tea."
    },
    {
        "name": "Fire",
        "type": "Meat-Based",
        "duration": 20,
        "goal": "Urgency-High.",
        "dish": "Prepare the fish tea."
    },
    {
        "name": "Air",
        "type": "Dessert",
        "duration": 10,
        "goal": "Light ending.",
        "dish": "Prepare the fish tea."
    }
]


def action(course, config):

    for index, item in enumerate(course):

        color = course_colors.get(
            item['name'],
            Fore.WHITE
        )

        if index < len(course) - 1:
            next_course = course[index + 1]
        else:
            next_course = None

        print(color + "\n" + "=" * 60)

        print(color + f"{tabs}STARTING COURSE - {item['name'].upper()}\n")

        print(color + f"{tabs}Type: {item['type']}")

        print(color + f"{tabs}Dish: {item['dish']}")

        timer(item, next_course, config)

        print(color + "=" * 60 + "\n")


def menu(course):

    boot_loading()
    clear_screen()
    cafe_header()

    print(Fore.WHITE + Style.BRIGHT + f"\n{tabs}FOUR ELEMENTS DINING EXPERIENCE\n")

    for item in course:

        color = course_colors.get(item['name'], Fore.WHITE)

        print(color + f"{tabs}" + "=" * 40)

        print(color +f"{tabs}COURSE: {item['name'].upper()}")

        print(color + f"{tabs}" + "-" * 40)

        print(color + f"{tabs}Type: {item['type']}")

        print(color + f"{tabs}Duration: {item['duration']} sec")

        print(color + f"{tabs}Goal: {item['goal']}")

        print(color + f"{tabs}Dish: {item['dish']}")

        print(color + f"{tabs}" + "=" * 40)
        
        time.sleep(1)