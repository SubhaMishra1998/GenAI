##Task 1 Basic class and object creation

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Category: {self.category}"
    
    def apply_discount(self,discount):
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        self.price = self.price * (1 - discount / 100)
        return f"After giving you {discount}% the price is {self.price}"
    

p1= Product("Laptop", 1200, "Electronics")
print(p1.get_info())

p2 = Product("Shirt", 50, "Clothing")
print(p2.get_info())


print(p2.apply_discount(10))

