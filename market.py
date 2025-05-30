list_of_items_in_cart = []

wallet = 50

credit_card = 30

products = {
    "apple": {'price': 0.5, 'stock': 9}, "orange": {'price': 0.7, 'stock': 7}, "chips": {'price': 1.09, 'stock': 4}, "chesse": {'price': 2.05, 'stock': 0},
      "milk": {'price': 0.85, 'stock': 14}, "sprite": {'price': 0.91, 'stock': 8}, "juice":{'price': 1, 'stock': 15},"biscuits": {'price': 1.44, 'stock': 2}, 
      "shampoo": {'price': 1.78, 'stock': 9}, "chocolate": {'price': 1.9, 'stock': 3}, "fish": {'price': 2.39, 'stock': 15}, "frozen pizza": {'price': 2.45, 'stock': 6},
    "eggs": {'price': 2.32, 'stock': 10}, "fanta":{'price': 0.91, 'stock': 4}, "watermelon": {'price': 1.99, 'stock': 15}, "bread":{'price': 0.89, 'stock': 6}, 
    "cake": {'price': 2.89, 'stock': 3}, "stake":{'price': 2.79, 'stock': 3}, "tomatoes":{'price': 0.9, 'stock': 17}, "watter":{'price': 0.79, 'stock': 20}
}


def displayinvetory(products):
 for item, details, in products.items():
    print(f"{item}: ${details['price']} {details["stock"]}")


displayinvetory(products)
def total_sum_selected(products, list_of_items_in_cart):
    total = 0
    for item in list_of_items_in_cart:  
        if item in products:  
            total += products[item]['price']
    return total

def check_stock(products, user_choice):
    if products[user_choice]['stock'] == 0:
        print(f"We're sorry but {user_choice} is out of stock")
        return False
    return True
          
                
while True:

    user_choice = input('"q" to checkout ) Items you Want to Buy? ').lower()

    if user_choice in products:
       if check_stock(products, user_choice): 
           list_of_items_in_cart.append(user_choice)
           print("Items in your Card:", list_of_items_in_cart)
       else:
           # Don't try to remove if we never added it
           print("Items in your Card:", list_of_items_in_cart)
    elif user_choice == "q":
        print("this will be:", total_sum_selected(products, list_of_items_in_cart), "$")
        user_pay_choice = input("How would you like to pay Cash or Credit Card? ").lower()

        total = total_sum_selected(products, list_of_items_in_cart)

        if user_pay_choice == "cash":
            wallet_after_pay = wallet - total
            print("Current Wallet Balance:", wallet_after_pay, "$")
            print("here's your receipt:")
            for x in list_of_items_in_cart:
                print(x)
            print("Thank you for Shopping")

        elif user_pay_choice == "credit card":
            credit_card_after_pay = credit_card - total
            print("Credit Card Current Balance:", credit_card_after_pay, "$")
            print("here's your receipt:")
            for x in list_of_items_in_cart:
                print(x)
            print("Thank you for Shopping")

        break

    else:
        print("item is not in our Inventory!")
        print(list_of_items_in_cart)

