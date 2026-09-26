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
    




