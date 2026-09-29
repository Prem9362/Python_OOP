class Bank:
    def __init__(self,acc_holder,acc_number,balance):
        self.acc_holder=acc_holder
        self.acc_number=acc_number
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance + amt
        print(f'{amt} Amount is deposited , total balance is {self.balance}')

    def withdraw(self,amt):
        self.balance=self.balance - amt 
        print(f'{amt} Amount is withdrawn , total balance is {self.balance}')

obj =Bank('Prem',9890696558,50000.6)

print(obj.acc_holder)
print(obj.balance)
print(obj.acc_number)

obj.deposit(9000)

print(obj.balance)

obj.withdraw(6500)


        