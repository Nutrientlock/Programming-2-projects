import random


   
def getnum():
    while True:
        try:
            num = int(input('Enter in num: '))
            return num
        except ValueError:
            print('must be a number')

def easy():
    while True:
        num= getnum()
        rannum = random.randint(1,5)
        
        if num == rannum:
            print('u win')
        else:
            print('u lose')

        print(f'Num was: {rannum}\n')
        choice = input('Do you want to play again (y/n): ')
        if choice =='n':
            break

def med():
    while True:
        num= getnum()
        rannum = random.randint(1,10)
        
        if num == rannum:
            print('u win')
        else:
            print('u lose')

        print(f'Num was: {rannum}\n')
        choice = input('Do you want to play again (y/n): ')
        if choice =='n':
            break

def hard():
    while True:
        num= getnum()
        rannum = random.randint(1,20)
        
        if num == rannum:
            print('u win')
        else:
            print('u lose')

        print(f'Num was: {rannum}\n')
        choice = input('Do you want to play again (y/n): ')
        if choice =='n':
            break

def nightmare():
    while True:
        num= getnum()
        rannum = random.randint(1,1000000)
        
        if num == rannum:
            print('u win')
        else:
            print('u lose')

        print(f'Num was: {rannum}\n')
        choice = input('Do you want to play again (y/n): ')
        if choice =='n':
            break

 



