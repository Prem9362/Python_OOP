import time 

def decorator(f):
      def inner():
        x=time.time()
        print('Function Has Started')
        f()
        print('Function Has ended')
        y=time.time()
        print('Execution time is :', y-x)
      return inner

class Employee():

    def __init__(self,emp_name,emp_id,emp_dep,task,role):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_dep=emp_dep
        self.task=task
        self.role=role
        Employee.collection.append({'emp_name':emp_name,'emp_id':emp_id,'emp_dep':emp_dep,"Task":task,'Role':role})

    collection=[]

   
    def get_role_details(self):
        pass

    def calculate_workload(self):
        pass
    
    def display(self):
          print(f'Name : {self.emp_name}\n' f'Employee_ID:{self.emp_id}\n' f'Employee_Department:{self.emp_dep}\n')
          

class Developer (Employee):

    
    def get_role_details(self):
            return self.role
    
    def calculate_workload(self):
            return f'Workload is : {self.task}'
            

class Datascientist (Employee):

   
    def get_role_details(self):
            return self.role
    
    def calculate_workload(self):
                return f'Workload is :{self.task}'
     
class Manager (Employee):

    
    def get_role_details(self):
            return self.role

    
    def calculate_workload(self):
                return f'Workload is :{self.task}'


def gen_fun(Emp):
      i=0
      while i< len(Emp):
            yield Emp[i]
            i+=1

m1=Manager('Prem',101,'IT',["build api","xyz",'JKLM'],'Manager')
m2=Manager('zrem',101,'IT',"buildzxxxapi",'Manager')

m1.display()

for i in gen_fun(Employee.collection):
      x = i
      print('emp_name :',x['emp_name'] )
      print('emm_id :',x['emp_id'] )
      print('emp_dep :',x['emp_dep'] )
      print('Task :',x['Task'] )
      print('Role :',x['Role'] )

      print('SDFGHJKL:SDFGHJKL:XCFGHJKL')
      


it1=iter(Employee.collection)
print(next(it1))





