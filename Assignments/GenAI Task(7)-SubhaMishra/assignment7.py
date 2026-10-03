##Task 1 Basic class and object creation


# class Product:
#     def __init__(self,name,price,category):
#         self.name = name
#         self.price = price
#         self.category = category

#     def get_info(self):
#         return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"
    
#     def apply_discount(self,discount):
#         if discount < 0 or discount > 100:
#             raise ValueError("Discount must be between 0 and 100")
#         self.price = self.price * (1 - discount / 100)
#         return f"After giving you {discount}% the price is {self.price}"
    

# p1= Product("Laptop", 1200, "Electronics")
# print(p1.get_info())

# p2 = Product("Shirt", 50, "Clothing")
# print(p2.get_info())


# print(p2.apply_discount(10))



# Task 2: constructor and encapsulations

from unicodedata import name


class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price
    
    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.get_price()}, Category: {self.category}"

    def set_price(self,price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price    


obj1 = Product('Iphone',55000,'Electronics')
print(obj1.get_price())

obj1.set_price(60000)
print(obj1.get_price())




# Task 3: Inheritance(single level))

class ElectronicProduct(Product):
    def __init__(self,name,price,category,warranty_information):
        ##new this class specific attribute warranty_information initiated here.
        super().__init__(name,price,category)
        ##To intialize the parent class atttibutes used super().
        self.warranty_information = warranty_information

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.get_price()}, Category: {self.category} with warranty information: {self.warranty_information}"
    


obj3 = ElectronicProduct('Iphone',25000,'Electronics','1 year warranty')
print(obj3.get_info())



#Task 4 polymorphism

class Laptop(Product):
    def __init__(self, name, price, category, brand, model, ram):
        super().__init__(name, price, category)
        self.brand = brand
        self.model = model
        self.ram = ram

    def get_info(self):
        return f"Laptop Name: {self.name}, Laptop Price: {self.get_price()}, Laptop Category: {self.category}, Laptop Brand: {self.brand}, Laptop Model: {self.model}, Laptop RAM: {self.ram}"
         

class Mobile(Product):
    def __init__(self, name, price, category, brand, model, ram):
        super().__init__(name, price, category)
        self.brand = brand
        self.model = model
        self.ram = ram

    def get_info(self):
        return f"Mobile Name: {self.name}, Mobile Price: {self.get_price()}, Mobile Category: {self.category}, Mobile Brand: {self.brand}, Mobile Model: {self.model}, Mobile RAM: {self.ram}"





laptop = Laptop("VOSTRO",49000,"Electronics","Dell","XPS 13", "16GB")
mobile = Mobile("Galaxy", 30000, "Electronics", "Samsung", "Galaxy S21", "8GB")

devices = [laptop, mobile]

for device in devices:
    print(device.get_info())



##Task 5 : Abstraction

##importing the abc module to use abstract base classes
from abc import ABC, abstractmethod

##creating abstract class process_payment with abstract method process_payment which is an empty method and will be implemented by the subclasses credit_card_payment and UPIPayment
class process_payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class credit_card_payment(process_payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class UPIPayment(process_payment):
    def process_payment(self, amount):
        print(f"Processing UPI  payment of {amount}")



credit_card1 = credit_card_payment()
credit_card1.process_payment(1000)

upi1 = UPIPayment()
upi1.process_payment(500)   
