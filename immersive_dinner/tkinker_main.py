import tkinter as tk
import winsound

course = [
    {
        "name": "Water",
        "type": "Seafood",
        "duration": 30,
        "goal": "Calm beginning.",
        "dish": "fish tea."
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


window = tk.Tk()
window.title("Four Elements Dining Experience")
window.geometry("800x500")


title = tk.Label(
    window,
    text="FOUR ELEMENTS DINING EXPERIENCE",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

course_name = tk.Label(window, text="", font=("Arial", 16, "bold"))
course_name.pack(pady=5)

course_type = tk.Label(window, text="", font=("Arial", 12))
course_type.pack()

course_goal = tk.Label(window, text="", font=("Arial", 12))
course_goal.pack()

course_dish = tk.Label(window, text="", font=("Arial", 12))
course_dish.pack(pady=10)

timer_label = tk.Label(window, text="00:00", font=("Arial", 30, "bold"))
timer_label.pack(pady=20)



def countdown(time_left, index):

    if time_left > 0:

        timer_label.config(text=f"{time_left:02}")

        window.after(
            1000,
            countdown,
            time_left - 1,
            index
        )

    else:

        if index + 1 < len(course):

            next_item = course[index + 1]

            timer_label.config(
                text=f"Prepare {next_item['name']}"
            )

            window.after(
                2000,
                run_course,
                index + 1
            )

        else:
            winsound.Beep(1000, 1000)
            timer_label.config(text="SERVE NOW")

    if time_left == 3:
        winsound.Beep(900, 200)

    if time_left == 2:
        winsound.Beep(900, 200)

    if time_left == 1:
        winsound.Beep(900, 200)


def run_course(index):

    item = course[index]

    course_name.config(
        text=f"COURSE: {item['name'].upper()}"
    )

    course_type.config(
        text=f"Type: {item['type']}"
    )

    course_goal.config(
        text=f"Goal: {item['goal']}"
    )

    course_dish.config(
        text=f"dish: {item['dish']}"
    )

    countdown(item['duration'], index)


def start_experience():

    start_button.destroy()
    
    run_course(0)



start_button = tk.Button(
    window,
    text="Start Experience",
    font=("Arial", 14),
    command=start_experience
)

start_button.pack(pady=10)



window.mainloop()
