class Human :
    def __init__(self):
        self.weight=2
        self.height=14
        self.balance=0
    def talk(self):
        print('Hi!, How are you')
    def earn(self):
        self.balance =self.balance+1000
    def display(self):
        print('Weight :',self.weight,'Height :',self.height,'Balance :',self.balance)

obj1=Human()
obj2=Human()

obj1.display()
obj2.display()
obj1.earn()
obj2.earn()
obj1.earn()
obj2.earn()
obj1.display()
obj2.display()
