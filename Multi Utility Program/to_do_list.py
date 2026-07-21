import os
import time

task = []
complete = []

def save(task):
    with open('tasks.txt', 'w') as f:
        for item in task:
                f.write(f'{item}+\n')
def savem(complete):
    with open('tasks.txt', 'w') as f:
        for item in task:
                f.write(f'{item}+\n')

if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as f:
        for line in f:
            task.append(line.strip())
else:
    with open('tasks.txt', 'w') as f:
        f.write('Openning\n')
        
if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as f:
        for line in f:
            task.append(line.strip())
else:
    with open('tasks.txt', 'w') as f:
        f.write('Openning\n')

def to_do():
    while True:
        print('\n===Welcome===\n')
        print('Chosse an Option\n')
        print('1. Add a Task')
        print('2. Veiw all Task')
        print('3. Remove a Task')
        print('4. Complete a Task')
        print('q. Exit\n')
        choice = input('Enter your choice: ').strip().lower()   
        if choice == 'q':
            print('Exiting To Do List. Goodbye!\n')
            break
        elif choice == '1':
            new_task = input('Enter Task: ')
            task.append(new_task)
            save(task)
            print("==Task Entered==")
        elif choice == '2':
            if not task:
                print('No Tasks')
            else:
                for item in task:
                    print(f"Task: {item}")
        elif choice == '3':
            if not task:
                print('No Task to Remove')
            else:
                print('\n===Choose task to remove===\n')
                for item in task:
                    print(f"Task: {item}")
                time.sleep(3)
                task_to_remove = input('\nEnter Task to be Removed: ').strip().lower()
                if task_to_remove in task:
                    task.remove(task_to_remove)
                    print('==Task Removed==')
                else:
                    print('Task Does Not Exist')
        elif choice == '4':
            if not task:
                print('No Task to Complete')
            else:
                print('\n===Choose task to complete===\n')
                for item in task:
                    print(f"Task: {item}")
                time.sleep(3)
                task_to_remove = input('\nEnter Task to be complete: ').strip().lower()
                if task_to_remove in task:
                    task.remove(task_to_remove)
                    task.append(task_to_remove)
                    savem(complete)
                    print('==Task Completed==')
                else:
                    print('Task Does Not Exist')

if __name__ == '__main__':
    to_do()