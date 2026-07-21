#Scenario: Movie Ticket Booking System 
#Write a program that simulates a movie ticket booking system. A user can select movie tickets,  choose seat type, add snacks, and proceed to checkout. 
#The program must use a menu that repeats until the user checks out or exits. The system keeps  track of the total ticket cost and snack cost and calculates final charges including tax and service  fee. There is also a chance the user wins a free ticket. 

import random #this allows us to use the random.randint function for the number generating part

def book_ticket():# this allows the user to choose and moive option then seat option and returns the data
    ticket = 0
    ticket_total = 0
    print('==Options==\n')
    print('1. Action Movie $1200')
    print('2. Comedy $1000')
    print('3. Horror Movie $900')
    print('4. Animated Movie $800\n')
    choice= input('Enter Your Choice: ').strip().lower()#.strip() and .lower() - removes any white space and changes the case in to lower case this reduces the chance of error
    if choice == '1':
        ticket = 1200
    elif choice == '2':
        ticket = 1000
    elif choice == '3':
        ticket = 900
    elif choice == '4':
        ticket = 800
    print('==Additional Seating Cost==\n')
    print('1. Regular $0')
    print('2. Premium $500')
    print('3. Horror Movie $1000\n')
    choice1= input('Enter Your Choice: ').strip().lower()
    if choice1 == '1':
        ticket_total = ticket + 0
    elif choice1 == '2':
        ticket_total = ticket + 500
    elif choice1 == '3':
        ticket_total = ticket + 1000
    print(f'Your total is{ticket_total}')
    return ticket_total# allow us to use the data in a different function


def add_snack():#this allow the user to choose multiple snacks then returns the data after stopped 
    snack_total= 0
    while True:# this while loop allows the user to continuously enter snacks
        print('==Options==\n')
        print(f'Balance: ${snack_total}')
        print('1. Popcorn $400')
        print('2. Nachos $350')
        print('3. Soda $250')
        print('4. Combo (Popcorn + Soda) $600')
        print('q. Exit')
        choice2= input('Enter Your Choice: ').strip().lower()
        if choice2 == '1':#made choice; choice2 in this function for readiblity
            snack_total = snack_total + 400
            
        elif choice2 == '2':
            snack_total = snack_total + 350
            
        elif choice2 == '3':
            snack_total = snack_total + 250
            
        elif choice2 == '4':
            snack_total = snack_total + 600
            
        elif choice2 == 'q':
            print('Bye Bye')
            break# allows us to exit this loop and enter back into the main loop
    return snack_total

def checkout(ticket_total, snack_total):#this function calulates subtotal, and print all of the addition details that comes with it
    subtotal = ticket_total + snack_total
    service= 300
    if subtotal < 1000:#check if minimum requirment is meet
        print('Checkout denied: Minimum subtotal allowed is $1000')
    else:
        rannum = random.randint(1,15)#this is allow us to get the ramdom number for the free movie ticket
        if rannum == 2:
            print('You won a free movie ticket!!')
            subtotal = snack_total
            tax = subtotal * 0.12
            final_total = subtotal + tax + service
            ticket_total = 0
            print(f'Your ticket total is: ${ticket_total}')
        else:
            subtotal = ticket_total + snack_total
            tax = subtotal * 0.12
            final_total = subtotal + tax + service
            print(f'Your ticket total is: ${ticket_total}')
        
        print(f'Your snack total is: ${snack_total}')
        print(f'Your tax is: ${tax}')
        print(f'Your service fee is: ${service}')
        print(f'Your final total is: ${final_total}')
        



ticket_total = 0
snack_total= 0
while True:# this is the main menu while loop, it allows us to branch off into the other functions
    print('==Menu==\n')
    print('1. Book Movie Ticket')
    print('2. Add snacks')
    print('3. Checkout')
    print('q. Exit\n')
    choice3= input('Enter Your Choice: ').strip().lower()
    if choice3 == '1':
        ticket_total = ticket_total + book_ticket()
    elif choice3 == '2':
        snack_total = snack_total + add_snack()
    elif choice3 == '3':
        checkout(ticket_total, snack_total)# this uses in information returned from the frist two option to create the checkout page
    elif choice3 == 'q':
        print('Bye Bye')
        break
        
        
    