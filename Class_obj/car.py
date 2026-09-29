class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed

    def accelerate(self):
        print('Acceleration initialized')

    def brake(self):
        print('Apply brake')

obj=Car('BMW',2026,350)

print(obj.speed)
print(obj.model)
print(obj.brand)

obj.accelerate()
obj.brake()
