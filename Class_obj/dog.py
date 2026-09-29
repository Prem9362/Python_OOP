class Dog :
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age 
        self.breed=breed
    def bark(self):
        print('bhawwww ! bhawwww!') 
    def run(self):
        print('Runs on 4 legs ')

obj1 = Dog('Tommy',2,'Indian')  
print(obj1.name)
print(obj1.age)
print(obj1.breed)
obj1.bark()
obj1.run()