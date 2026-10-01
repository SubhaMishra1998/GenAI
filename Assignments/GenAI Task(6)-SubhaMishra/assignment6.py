# #Task 1 Safe Division Utility

# numerator = input("Please enter the numerator: ")
# denominator = input("Please enter the denominator: ")

# try:
#     result = int(numerator)/int(denominator)
    

# except ZeroDivisionError:
#     print("Denominator can not be zero, please try again")

# except ValueError:
#     print("Please enter only numbers")

# else:
#     print(f"result is {result}")

# finally:
#     print("Operation complete")


# #Task 2: Bill Calculator with error handling

# class NegValueError(Exception):
#     "Raised when negative value comes"

#     def __init__(self,price):
#         self.price = price
#         self.message = f"Cannot add negative price."
#         super().__init__(self.message)



# prices = [120,350,"abc",500, -200,800]
# total = 0



# for price in prices:
#     try:
#         if price < 0:
#             raise NegValueError(price)
#         total+=price
#     except TypeError:
#         print("The price given is not a number,skipping..")
#         continue
#     except NegValueError as e:
#         print("can not add negative price, skipping: ", price)
#         continue
#     finally:
#         print(total)


##Custom exceptions agen validator:


class NValueError(Exception):
        "Raised when number is not between 1-120"

        def __init__(self,price):
                self.price = price
                self.message = f"Age must be between 1 and 120, you entered {self.price}"
                super().__init__(self.message)


def age_check(age):
    if age < 1 or age > 120:
        raise NValueError(age)
    else:
        print("Age is valid")   

age = int(input("Please enter your age: "))

try:
    age_check(age)
except NValueError as e:
    print(e)


##Task 4 : File reading exception handling
fileName = input("Please enter the file name to read: ")
try: 
    with open(fileName, 'r') as f:
        lines = f.readlines()
    lines =lines[0:3]
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print(f"File {fileName} not found, please check the file name and try again.")

except PermissionError:
    print(f"You do not have permission to read the file {fileName}. Please check the file permissions.")    

finally:
    print("File Operation Attempted")



##Task 5; Mini Shopping Cart 
cart = []
totalPrice = 0


class NegValueError(Exception):
    "Raised when negative value comes"

while True:
    item = input("Please enter the price to add to the cart (or type 'q' to exit): ")

    if item.lower() == 'q':
        break

    else:


        try:
            if int(item) < 0:
                raise NegValueError(item)
            totalPrice += float(item)
            cart.append(float(item))
        except NegValueError:
            print("Cannot add negative price, skipping: ", item)
            continue 

        except ValueError:
            print("The price given is not a number, skipping..")
            continue    

        finally:
            print(f"Total price is now: {totalPrice}")
            print(f"Total items in cart: {len(cart)}")     



        

