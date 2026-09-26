# Task 1 : Discount rules



try:
    order_amount = int(input("Enter the order amount: "))

    if order_amount >= 2000:
        discount = order_amount*0.15
        final_amount = order_amount - discount
        print("Final amount after discount: ", final_amount)
        print("Discount applied: 15%")
    elif order_amount >= 1500 and order_amount<2000:
        discount = order_amount*0.10
        final_amount = order_amount - discount
        print("Final amount after discount: ", final_amount)
        print("Discount applied: 10%")
    elif order_amount>=1000 and order_amount<1500:
        discount = order_amount*0.07
        final_amount = order_amount - discount
        print("Final amount after discount: ", final_amount)
        print("Discount applied: 7%")
    else:
        print("0% discount applied. Final amount: ", order_amount)
except ValueError:
    print("Invalid input. Please enter a valid order amount.")



# Task 2 : Process mutiple orders
orders = [1200,2500,800,750,3000]
total_revenue = 0

for order in orders:
    if order >= 2000:
        discount = order*0.15
        final_amount = order - discount
        total_revenue += final_amount
        print("Order amount: ", order, "Final amount after discount: ", final_amount, "Discount applied: 15%")
    elif order >= 1500 and order<2000:
        discount = order*0.10
        final_amount = order - discount
        total_revenue += final_amount
        print("Order amount: ", order, "Final amount after discount: ", final_amount, "Discount applied: 10%")
    elif order>=1000 and order<1500:
        discount = order*0.07
        final_amount = order - discount
        total_revenue += final_amount
        print("Order amount: ", order, "Final amount after discount: ", final_amount, "Discount applied: 7%")
    else:
        print("Order amount: ", order, "0% discount applied. Final amount: ", order)

print("Total revenue from all orders: ", total_revenue)




#Task 3 : User Menu

while True:
    user_menu = input("Enter '1' to add new order, '2' to check existing orders, or 'q' to quit: ")

    if user_menu == '1':
        try:
            new_order = int(input("Enter the new order amount: "))
            orders.append(new_order)
            print("New order added successfully.")
            continue
        except ValueError:
            print("Invalid input. Please enter a valid order amount.")
    elif user_menu == '2':
        print("Existing orders: ", orders)
        continue
    elif user_menu == 'q':
        print("Exiting the program.")
        break

# Task 5: loop control statement
daily = [200,150,0,400,50,-1,300]
total_sales = 0
for sale in daily:
    if sale<0:
        print("Data is corrupted. Exiting the loop.")
        break
    elif sale==0:
        print("No sales today. Skipping to next day.")
        continue
    else:
        total_sales += sale
        print("Total sales so far: ", total_sales)
