# Task 1 basic function 

def apply_discount(price, discount_percentage = 5):
    if discount_percentage>60:
        return "Discount percentage cannot exceed 60%"
    final_price = price - (price * discount_percentage / 100)
    return final_price

print(apply_discount(1000,10))  # Custom discount of 10%    
print(apply_discount(500))      # Default discount of 5%   
print(apply_discount(2000,70))  # Discount percentage exceeds 60%

# Task 2 Recursive function
def factorial(n):
   
    if n==0 or n==1:
        return 1
    elif n<0:
        return "Invalid input. Please enter a non-negative integer."
    else:
        return n * factorial(n-1)
    

print(factorial(5))
print(factorial(0))
print(factorial(-3))


# Task 3 : Lambda function  GST Calculator
gst = lambda x: x+ x*0.18

print("Price after 18%  gst: ", gst(100))


# Task 4 : use map to apply gst to list of prices

prices = [100,250,400,1200,50]
print(list(map(gst,prices)))


# Task 5 : use filter
prices2 = [100,250,400,1200,50,2000,850]
lessthan500 = list(filter(lambda x: x<500,prices2))
morethan500 = list(filter(lambda x: x>=500,prices2))

print(lessthan500)
print(morethan500)


#Task 6 : combined utility function

def process_prices(price):
    discounted_price= list(map(lambda x : x-x*0.10, price))
    print("Discounted Price: ", discounted_price)

    filtered_price = list(filter(lambda x: x>300, discounted_price))
    print("Filtered Price: ", filtered_price)

    return (discounted_price,filtered_price)

process_prices([100,500,900,750,50])


# Task 7: Mini Problem- creating menu using function
price_list = []

def add_prices(prices_list, price):
    prices_list.append(price)

def get_average_price(price_list):
    l = len(price_list)
    s = 0
    for price in price_list:
        s+=price
    return s/l

def get_max_price(price_list):
    m = -1
    for price in price_list:
        if price>m:

            m = price
    return m


while True:
    
    menu = input("Please select one from the list: 1. Add Price 2. Show Average Price 3. Show highest price 4.q: To quit:  ")

    if menu == "1" or menu == "Add Price".lower():
        ask_price = int(input("Please enter the price"))
        try:
            add_prices(price_list, ask_price)
            
            print("Price added to the list")
        except ValueError:
            print("Please ennter valid price")
        
        
    if menu=="2":
        print("Average price is: ", get_average_price(price_list))
        
    
    if menu =="3":
        print("Max is :", get_max_price(price_list))
        

    if menu == 'q':
        print("Existing...")
        break








