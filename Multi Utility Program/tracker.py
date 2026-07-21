import time
import os


cli={
    "income":0.0,
    "expense": 0.0,
    'transaction':[]
}
def save_cli(cli):
    with open('cli.txt', 'w') as f:
        f.write(f"income:{cli['income']}\n")
        f.write(f"expense:{cli['expense']}\n")
        for transaction in cli['transaction']:
            f.write(f"transaction:{transaction}\n")

# Check if file exists
if os.path.exists('cli.txt'):
# Open the file in read mode
    with open('cli.txt', 'r') as f:
        # Read the file line by line
        for line in f:
            # Remove newline and split into key and value
            key, value = line.strip().split(':', 1)
            # If the line is income, convert to number and store
            if key == 'income':
                cli['income'] = float(value)
            # If the line is expense, convert to number and store
            elif key == 'expense':
                cli['expense'] = float(value)
            # If the line is a transaction, add it to the list
            elif key == 'transaction':
                cli['transaction'].append(value)
else:
    # If file doesn't exist, create it empty
    with open('cli.txt', 'w') as f:
        f.write('income:0\nexpense:0\n') 

def income(cli):
    print('\n==Deposit==\n')
    try:
        new_balance = float(input('Enter Income Amount: J$'))
        if new_balance  <= 0:
            print('\nMust be more than zero.\n')
        else:
            cli['income'] += new_balance
            print('\n Income Added!!\n')
            cli['transaction'].append(f'Income: J${new_balance}') 
            save_cli(cli)   
    except ValueError:
        print('Income must be a number!!\n')

def expense(cli):
    print('\n==Deposit==\n')
    try:
        new_balance = float(input('Enter Expense Amount: J$'))
        if new_balance  <= 0:
            print('\nMust be more than zero.\n')
        else:
            cli['expense'] += new_balance
            print('\n Expense Added!!\n')
            cli['transaction'].append(f'Expense: J${new_balance}') 
            save_cli(cli)   
    except ValueError:
        print('Expense must be a number!!\n')
  
def veiw(cli):
    print('total income', cli['income'])
    print('total expense', cli['expense'])
    print('====================')
    print('transactions')
    print('====================\n')
    if not cli['transaction']:
        print('No transactions yet.\n')
        return
    for items in cli['transaction']:
        print(items)
            

def menu():
    chance = 5
    password = '123'
    while chance > 0:
        user_enter = input('Enter password: ').strip()
        if user_enter == password:
            print('Access granted.\n')
            break
        else:
            chance -= 1
            print('Incorrect.')
            print(f'Chances left: {chance}\n')
            time.sleep(1)
    if chance == 0:
        print('Blocked!\nPlease contact developer.')
        return   
    while True:
        print('== this is menu ==')
        print('1. view')
        print('2. income')
        print('3. expense')
        print('q. exit')

        choice = input('enter choice: ').strip().lower()

        if choice == 'q':
            print('bye')
            break
        elif choice == '1':
            veiw(cli)
        elif choice == '2':
            income(cli)
        elif choice == '3':
            expense(cli)
        else:
            print('invalid')

if __name__ == '__main__':
    menu()
