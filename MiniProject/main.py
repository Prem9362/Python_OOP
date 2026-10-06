class Fooditem:
    def __init__(self,food_id,food_name,food_price,availability):
        self.food_id=food_id
        self.food_name=food_name
        self.food_price=food_price
        self.availability=availability

    def __str__(self):
        return f'Food Id :{self.food_id}\n' f'Food_Name : {self.food_name}\n' f'Price :{self.food_price}\n' f'Available:{self.availability}'



class Pizza(Fooditem):
    def __str__(self):
        return f'Pizza\n' f'Food Id :{self.food_id}\n' f'Food_Name : {self.food_name}\n' f'Price :{self.food_price}\n' f'Available:{self.availability}'

class Burger(Fooditem):
    def __str__(self):
        return f'Burger\n' f'Food Id :{self.food_id}\n' f'Food_Name : {self.food_name}\n' f'Price :{self.food_price}\n' f'Available:{self.availability}'
    
class Beverage(Fooditem):
    def __str__(self):
        return f'Beverage\n' f'Food Id :{self.food_id}\n' f'Food_Name : {self.food_name}\n' f'Price :{self.food_price}\n' f'Available:{self.availability}'

class Restaurant:
    def __init__(self,rest_id,rest_name):
        self.rest_id=rest_id
        self.rest_name=rest_name
        self.food_items={}

    def add_food_item(self, food):
        self.food_items[food.food_id] = food

    def display(self):
        for i,j in self.food_items.items():
            print(i,':',j.food_name)

class Customers:
    def __init__(self,cust_id,cust_name):
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.orders=[]

    def __str__(self):
        return f'Customer_ID : {self.cust_id}\n' f'Customer_name : {self.cust_name}\n' f'Orders:{self.orders}\n'

class Order:
    def __init__(self,order_id,customer,restaurant):
        self.order_id=order_id
        self.customer=customer
        self.restaurant=restaurant
        self.items = {}
        self.status = "Placed"

    def add_item(self,id,quantity):
        self.items[id]=quantity


