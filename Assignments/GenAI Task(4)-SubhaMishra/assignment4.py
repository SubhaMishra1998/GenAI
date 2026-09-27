#Task 1: Write Sales record

#sales list

sales = [1200,450,980,1500,3000]

#opening file to write and with keyword closes it automatically

with open ("sales_data.txt",'w') as file:
    for sale in sales:
        file.write(f"{sale}\n")

#Opening file to read the content now

with open("sales_data.txt", 'r') as file:
    content = file.read()
print(content)


#Task 2 : Read files in Different ways

with open ('sales_data.txt', 'r') as file:
    content = file.read()
print(content)

print("Printing First Line")
with open ('sales_data.txt', 'r') as file:
    firstLine = file.readline()
print(firstLine)

print("Printing All Lines")
with open ('sales_data.txt', 'r') as file:
    lines = file.readlines()

list_sales = []
for line in lines:
    list_sales.append(int(line))
print(list_sales)


#Task 3 : Append new Sales(5000,2500,1700)

#adding new values
new_values = [5000,2500,1700]
with open("sales_data.txt", "a") as f:
    for value in new_values:
        f.write(f"{value}\n")

#reading the new values 
with open("sales_data.txt", "r") as file:
    content = file.read()
print(f"After adding new values:\n ", content)


#reading number of lines
with open("sales_data.txt", "r") as f:
    lines= f.readlines()
    print("Number of lines in file: ", len(lines))


##Task 4 : Generate Summary Report

#Calculating total sales
Total_Sales = 0
with open("sales_data.txt","r") as file:
    lines = file.readlines()
for line in lines:
    Total_Sales+= int(line)
print("Total Sales: ", Total_Sales)


#Calculating highest sales

with open("sales_data.txt","r") as file:
    sales = file.readlines()

highest_sale = 0

for sale in sales:
    if int(sale)>highest_sale:
        highest_sale = int(sale)

print("Highest Sale: ", highest_sale)


#Calculating highest sales

with open("sales_data.txt","r") as file:
    sales = file.readlines()

lowest_sale = float('inf')

for sale in sales:
    if int(sale)<lowest_sale:
        lowest_sale = int(sale)

print("Lowest Sale: ", lowest_sale)


#Printing Average Sale:

with open("sales_data.txt","r") as file:
    lines = file.readlines()
l = len(lines)
print("Average Sales: ", Total_Sales/l)


##Task 5: Create Product Info File
import os

i = 0
#initializing empty dictionary
dic = {}

#Taking user inputs
while i<3:
    product = input("Please enter product: ")
    price = int(input(f"Please enter price for {product} : "))
    dic[product]= price
    i+=1

#Putting the values in the file
for key,value in dic.items():

    if not os.path.isfile("products.txt") or not os.path.getsize("products.txt")>0:

        with open('products.txt',"w") as file:
            file.write(f"Product | Price\n")

   
    with open('products.txt',"a") as file:
        file.write(f"{key} | {value}\n")

#Reading the file using readlines

with open("products.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    print(line.split("|"))


# Task 5: Read File Safely
file_name= input("Please enter a filename to enter: ")

if os.path.exists(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    print(content)
else:
    print("File not found , please check with the name")



##Task 7: Mini Project
import os

prices ={
    'Mouse': 500,
    'Keyboard': 800,
    'Monitor': 700,
    'Pendrive': 400,
    'Camera': 5000

}

discount_percentage = int(input("Please enter the discount percentage you want: "))
total_discounted_price = 0

if not os.path.exists("discount_report.txt") or not os.path.getsize("discount_report.txt"):
    with open("discount_report.txt", 'w') as f:
        f.write(f"Product | Original Price | Discounted Price \n")
for product,price in prices.items():
    discounted_price = price-(price*discount_percentage/100)
    total_discounted_price += discounted_price
    with open("discount_report.txt", "a") as f:
        f.write(f"{product} | {price} | {discounted_price}\n")


with open("discount_report.txt", "r") as file:
    lines = file.readlines()
print("Total number of items : ", len(lines)-1)


print("Average discounted price: ", total_discounted_price/len(lines)-1)



    











    




