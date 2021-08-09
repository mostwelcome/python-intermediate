from bank import Bank


bank = Bank()
while True:
    mode = input("Enter 'd' to deposit and 'w' to withdraw from your account and quit to 'quit' the application: ")
    if mode.lower() == 'd' or mode.lower() == 'w':
        try:
            amount = float(input('Enter amount :'))
        except ValueError:
            amount =0

    if mode.lower()  == 'quit':
        bank.remove_transaction_history()
        break

    if mode.lower() =='d':
        bank.deposit(amount)
    elif mode.lower() =='w':
        bank.withdraw(amount)
    else:
        print('Please enter a valid input')

    print('Your remaining balance after transaction : ',bank.check_balance())