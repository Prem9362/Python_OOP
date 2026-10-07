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
    restaurants = {}

    def __init__(self,rest_id,rest_name):
        self.rest_id=rest_id
        self.rest_name=rest_name
        self.food_items={}
        Restaurant.restaurants[self.rest_id]=self

    def add_food_item(self, food):
        self.food_items[food.food_id] = food

    def display(self):
        for i,j in self.food_items.items():
            print(i,':',j.food_name)


class FoodIterator:
    def __init__(self, food_items):
        self.food_items = food_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.food_items):
            food = list(self.food_items.values())[self.index]
            self.index += 1
            return food
        else:
            raise StopIteration


        
class Customers:
    customers = {}

    def __init__(self,cust_id,cust_name):
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.orders=[]
        Customers.customers[self.cust_id]=self

    def __str__(self):
        return f'Customer_ID : {self.cust_id}\n' f'Customer_name : {self.cust_name}\n' f'Orders:{self.orders}\n'

class Order:
    def __init__(self,order_id,customer,restaurant):
        self.order_id=order_id
        self.customer=customer
        self.restaurant=restaurant
        self.items = {}
        self.status = "Placed"

        self.customer.orders.append(self)

    def add_item(self, id, quantity):
        try:
            if id not in self.restaurant.food_items:
                raise ValueError("Food item does not exist")

            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")

            self.items[id] = quantity
            print("Item added successfully")

        except ValueError as e:
            print("Error:", e)


    def calculate_total(self):
        total = 0

        for food_id, quantity in self.items.items():
            food = self.restaurant.food_items[food_id]
            total = total + food.food_price * quantity

        return total
    
    def modify_item(self, food_id, quantity):
        try:
            if food_id not in self.items:
                raise ValueError("Food item not found in order")

            if quantity < 0:
                raise ValueError("Quantity cannot be negative")

            if quantity == 0:
                del self.items[food_id]
            else:
                self.items[food_id] = quantity

        except ValueError as e:
            print("Error:", e)

    def update_status(self, status):
        self.status = status
        print("Order status:", self.status)
        

# generator 

def order_generator(orders):
    for order in orders:
        yield order

# decorator

def log(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper



p1 = Pizza(101, "Margherita Pizza", 250, "Yes")
p2 = Pizza(102, "Farmhouse Pizza", 350, "Yes")

b1 = Burger(103, "Cheese Burger", 150, "Yes")

d1 = Beverage(104, "Coke", 50, "Yes")


r1 = Restaurant(1, "Pizza Hub")
r1.add_food_item(p1)
r1.add_food_item(p2)
r1.add_food_item(b1)
r1.add_food_item(d1)


c1 = Customers(1, "Prem")

print(Restaurant.restaurants)
print(Customers.customers)

r1.display()