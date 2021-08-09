import os
class Bank():

    def __init__(self,initial_amount = 0.00) -> None:
        self.amount = initial_amount

    def deposit(self,amount):
        self.amount += amount
        self.track_transaction("Deposited:",amount)

    def withdraw(self,amount):
        if self.amount < amount:
            print('Sorry! Insufficient Balance')
        else:
            self.amount -=amount
            self.track_transaction("Withdrawn",amount)

    def check_balance(self):
        return self.amount

    def track_transaction(self,mode,amount):
        with open('./class/bank-app/data.txt','a') as f:
            record = mode+" Amount: "+str(amount)+"\n"
            f.write(record)

    def remove_transaction_history(self):
        os.remove('./class/bank-app/data.txt')