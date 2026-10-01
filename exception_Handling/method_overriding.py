class Animal:
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    def mew(self):
        print('MEWWWWWWWWWWWWWWWWWWWWWWWWW')

a1=Animal()
a1.eat()

d1=Dog()
d1.eat()

c1=Cat()
c1.eat()