class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        pass

    def call(self):
        print('calling !!!!')

    def photo(self):
        print('CLickkk!!!!')

obj=Mobile('IQ','IQZ9Spro',21000)

print(obj.price)
print(obj.model)
print(obj.brand)

obj.call()
obj.photo()