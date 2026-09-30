class Complex:

    count=0

    def __init__(self,x,y):
        self.real=x
        self.imag=y
        Complex.count = Complex.count+1

    #def display(self):
        
       # print(f'{self.real}+{self.imag}i')
       # print('Count :',Complex.count)


    def __add__(self,x ):
        m=self.real + x.real
        n=self.imag + x.imag
        return Complex(m,n)

    def __lt__(self,x):
        a= self.real**2 + self.imag**2
        b= x.real**2 + x.imag**2

        return a<b

    def __str__(self):
        return f'{self.real}+{self.imag}i'

c1=Complex(3,4)
c2=Complex(5,6)

c3=c1+c2        # it means c1.__add__(c2)
#c3.display()
print(c3)

p=c1<c2
print(p)

print(str(c1))      # when we use print function str calls automatically 
print(c1)


