class a:
    def __init__(self,p,q):
        self.var1=p
        self.var2=q

    def display(self):
        print(self.var1,self.var2)

class b(a):

    def __init__(self,p,q,z):
        self.var3=z
        super().__init__(p,q)          # for accesing variable of parent class

    def f1(self):
        print(self.var3)
        self.display()

b1=b(10,20,30)
b1.f1()
