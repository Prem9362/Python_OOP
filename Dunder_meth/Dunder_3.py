class Employee :

    def __init__(self,emp_id,name,dept,basic_sal):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.basic_sal=basic_sal

    def Cal_annual_sal( self) :
        return self.basic_sal*12

    def give_bonus(self,bonus):
        return (self.basic_sal*(bonus/100))

    def __str__(self):
        return f'Name:{self.name} \n'  f'Employee_Id:{self.emp_id}\n'  f'Department :{self.dept}\n' f'Salary :{self.basic_sal}\n'

    def __len__(self):
        return len(self.name)
        
e1 =Employee(101,'Prem Biradar','IT',100000)
print(str(e1)) 

print(len(e1))

print(e1.give_bonus(10))

print(e1.Cal_annual_sal())
        