class Student :

    institute_name='Core Spyder'

    increment=0


    def __init__(self,student_id,name,course,marks):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.marks=marks

        Student.increment = Student.increment + 1


    def update_marks(self,x):
        self.marks=x
        return self.marks

        

    def __str__(self):
        return f'Student Id : {self.student_id} \n'  f'name :{self.name} \n'  f'course : {self.course} \n' f'marks : {self.marks} \n'




s1=Student(101,'Prem','DSML',99)
s2=Student(102,'Xyz','DSML',79)
s3=Student(103,'pqr','DSML',61)

print(s1.institute_name)
print()

print(str(s1))

print(f'total no of students : {Student.increment}')

print(s1.update_marks(95))

