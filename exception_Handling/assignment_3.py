class Bank:
    account={}

    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
        Bank.account[self.acc_no]={'name':self.name,'Balance':self.balance}


    def deposit(self,x):
        try:
            if x>0:
                self.balance= self.balance + x
                print(f'{x} Rs  deposited ' )
            else:
                print('Entered Amount is invalid')
        except Exception as e:
            print('Error raised invalid input')

    def withdraw(self,x):
        try:
            if self.balance >= x:
                self.balance = (self.balance-x) 
                print(f'{x} is withdrawn')
            else: 
                print('Insufficient Balance')
        except Exception as e:
            print('Error raised invalid input')

    def display_Acc(self):
        return f'Name :{self.name} \n' f'Account No:{self.acc_no}\n' f'Balance:{self.balance}\n'

    def cal_intrest(self,x):
        return self.balance*(x/100)

class Saving_acc(Bank):
    pass
class Curr_acc(Bank):

    predefine_limit=10000

    def withdraw(self,x):
        try:    
            if (self.balance + Curr_acc.predefine_limit) >= x:
                self.balance = (self.balance-x) 
                print(f'{x} is withdrawn')
            else:
                print('Provided amt out of limit')
        except Exception as e:
            print('Error raised invalid input')
            
A1=Curr_acc('prem',6555,10000)
A2=Saving_acc('XYZ',9090,19900)

x=A1


while True:

    print(" BANKING SYSTEM ")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. View Account Details")
    print("4. calculate Intrest")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        x.deposit(int(input('Enter amount you want to deposit')))

    elif choice == "2":
        x.withdraw(int(input('Enter amount you want to withdraw')))

    elif choice == "3":
        print(x.display_Acc())

    elif choice=='4':
        print(x.cal_intrest(int(input('Enter intrest percentage'))))

    elif choice == "5":
        print("Thank you!")
        break
    

    else:
        print("Invalid choice!")