class Student :
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def study(self):
        print('i am studying')

    def result(self):
        if self.marks>=40:
            print('Pass')
        else:
            print('Fail')

obj=Student('prem',22,92)

print(obj.age)
print(obj.name)
print(obj.marks)

obj.result()
obj.study()