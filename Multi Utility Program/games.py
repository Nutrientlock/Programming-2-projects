import time

def game():
    inventory = []
    time.sleep(2)
    print('You enter a dark room')
    time.sleep(2)
    print('Someone suddenly calls you....')
    time.sleep(2)
    name = input("Enter Your Name: ")
    print(f'{name}...')
    time.sleep(2)
    print(f'{name}...')
    time.sleep(2)
    print('Hel')
    time.sleep(2)
    print('HeLp...')
    time.sleep(2)
    print('Mm....\nMe..!!..')
    time.sleep(2)
    print('You see a hand reaching out to you.\nYou have two options? (1.Grab the hand/2.Run)')
    time.sleep(2)
    answer = input('Enter Your Choice: ')
    if answer == '1':
        time.sleep(2)
        print('===GAME OVER===')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('.......')
        time.sleep(1)
    else:
        print('You reach an intersection\nYou see two doors...')
        time.sleep(2)
        print('Left. An old broken door\nRight. A golden new door')
        time.sleep(2)
        
        door_choice = input('Which door do you choose? (left/right/stay): ').strip().lower()
        
        if door_choice == 'left':
            time.sleep(2)
            print('You try to open the old door...')
            time.sleep(2)
            print('You enter the room')
            time.sleep(2)
            print('There is a small table at the center of the room....')
            time.sleep(2)
            print('You step forward')
            time.sleep(2)
            print('You pick up a Bomb')
            inventory.append('Bomb')
            print("....")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("....")
            time.sleep(2)
            print("..")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print('BOOM')
            time.sleep(1)
            print("BLAST")
            time.sleep(2)
            print('===GAME OVER===\n\n')
            time.sleep(3)
            print('Final Inventory', inventory)
        elif door_choice == 'right':
            time.sleep(2)
            print('You enter the golden door...')
            time.sleep(2)
            print('There is a huge bed near a window')
            time.sleep(2)
            print('You start to drift into a deep sleep')
            time.sleep(2)
            print(f'{name}...')
            time.sleep(2)
            print(f'{name}...')
            time.sleep(2)
            print('You open your eyes to see a system message')
            time.sleep(2)
            print('There is a question written in the middle')
            time.sleep(2)
            question = input('What word is spelled incorrectly in every single dictionary? ')
            right_answer = 'incorrectly'

            if question == right_answer:
                time.sleep(2)
                print('....')
                time.sleep(2)
                print('.....')
                time.sleep(2)
                print('You slowly open your eyes....')
                time.sleep(2)
                print('You Have Exit The Mind Trap\n\n')
                time.sleep(2)
            else:
                print('===GAME OVER===\n')
                time.sleep(2)
        else:
            time.sleep(2)
            print('You hesitate and freeze...')
            time.sleep(2)
            print("Your eyes start shutting down")
            time.sleep(2)
            print('Your body starts sinking into the floor')
            time.sleep(2)
            print('You')
            time.sleep(2)
            print('Got')
            time.sleep(2)
            print('Burried')
            time.sleep(2)
            print('Alive')
            time.sleep(2)
            print('===GAME OVER===\n')
            time.sleep(2)


def gamemodes():
    while True:
        if __name__ == '__main__': 
            gamemodes()
        password = 'qwerty'
        print('===WELCOME===')
        user_input = input('Only One Chance\nEnter Access Code: ')

        if user_input == password:
            time.sleep(2)
            print('Access Granted\n\n')
            print('===GAME ROOM===\n')
            print('1, The Dark Room')
            print('2, Coming Soon')
            print('q, Exit')

            choice = input('Enter Your Choice: ').strip().lower()

            if choice == 'q':
                print('Goodbye!')
                break
            elif choice == '1':
                print('\n===THE DARK ROOM===\n')
                time.sleep(2)
                game()
            else:
                print('COMING SOON!')
                print('Will Be Returned To Access Page\n')
                time.sleep(2)

        else:
            print('Access Denied')
            break
