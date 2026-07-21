import time

def game():
    time.sleep(2)
    print('==THE DARK ROOM==')
    time.sleep(2)
    print('You enter a dark room')
    time.sleep(2)
    print('Someone suddenly calls you....')
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
    print('You see a hand reaching out to you.\nYou have two options? (Grab the hand/Run)')
    answer = input('Enter Your Choice: ')
    if answer == '1':
        print('===GAME OVER===')
    else:
        print('You reach an intersection\nYou see two doors...')
        time.sleep(2)
        print('Left. An old broken door\nRight. A golden new door')
        
        door_choice = input('Which door do you choose? (left/right): ').strip().lower()
        
        if door_choice == 'left':
            print('You try to open the old door...')
        elif door_choice == 'right':
            print('You enter the golden door...')
        else:
            print('You hesitate and freeze...')


password = "qwerty123"
print('===Welcome===')
user_input = input('Enter Access Code: ')

if user_input == password:
    print('Access Granted')
    game()
else:
    print('Access Denied')
    



