##TASK 1

##creating list of product

products= ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch","Smart ring"]

sample_product = ("Laptop", 95000, "Computer")

##printing last and second last product from the list
print("last product", products[-1])
print("second last product", products[-2])

##appending two new products to the list
products.append("Smart Glasses")
products.append("VR Headset")

print("Updated product list:", products)


sample_product = list(sample_product)
sample_product = ("Laptop", 99000, "Computer")

sample_product = tuple(sample_product)

print("Sample product details:", sample_product)

print(type(sample_product))




##TASK 2

category_set = {"Electronics", "Telephones", "Wearables", "Computers"}

category = ["Laptops", "Electronics", "Telephones", "Headphones", "Smartwatches"]

## tried to add a new category to the set
for item in category:
    ##printing whether the item is already present in the set or not in boolean format
    print(item in category_set)
    category_set.add(item)

##printing the updated category set
print("Updated category set:", category_set)

##printng total number of unique categories in the set
print("Total number of unique categories:", len(category_set))



# TASK 3

price_dict = {
    "Laptop": 95000,
    "Mobile": 30000,
    "Tablet": 25000,
    "Headphones": 5000,
    "Smartwatch": 15000,
    "Smart ring": 10000,
}

price_dict["Smart Glasses"] = 20000
price_dict["Smartwatch"] = 40000
price_dict.pop("Tablet")

number_of_products = len(price_dict)
total_price = sum(price_dict.values())
average_price = total_price / number_of_products

print("Updated price dictionary:", price_dict)
print("average price of products:", average_price)

values = list(price_dict.values())
min_price = values[0]
max_price = values[0]

for value in values:
    if value <min_price:
        min_price = value   

    if value > max_price:
        max_price = value

for key,value in price_dict.items():
    if value == min_price:
        print("Min price product", key)
    if value == max_price:
        print("Max priced product", key)


##TASK 4

catalog = [("laptop", 95000, "Computer"), ("mobile", 30000, "Telecommunication"), ("tablet", 25000, "Telecommunication"), ("headphones", 5000, "Audio"), ("smartwatch", 15000, "Wearable"), ("smart ring", 10000, "Wearable")]
# initializing an empty dictionary to store the mapping of categories to products
category_to_products = {}
for items in catalog:
    category = items[2]
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(items[0])     

print("Category to products mapping:", category_to_products)

#creating a list to store the categories with the maximum number of products and a variable to keep track of the maximum value
mxkey = []
mxvalue = 0

for category, products in category_to_products.items():
    if len(products) >mxvalue:
        mxvalue = len(products)
        mxkey.clear()
        mxkey.append(category)
    elif len(products) ==mxvalue:
        mxvalue = len(products)
        mxkey.append(category)

for i in mxkey:
    print(category_to_products[i])






