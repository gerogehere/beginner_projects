list_of_items_in_cart = []

wallet = 50

credit_card = 30

items = {
    "apple": 0.5, "orange": 0.7, "chips": 1.09, "chesse": 2.05, "milk": 0.85, "sprite": 0.91, "juice": 1,
    "biscuits": 1.44, "shampoo": 1.78, "chocolate": 1.9, "fish": 2.39, "frozen pizza": 2.45, "eggs": 2.32,
    "fanta": 0.91, "watermelon": 1.99, "bread": 0.89, "cake": 2.89, "stake": 2.79, "tomatoes": 0.9, "watter": 0.79
}

def total_sum_selected(items, list_of_items_in_cart):
    global total
    total = 0
    for item in list_of_items_in_cart:
        if item in items:
            total += items[item]
    return total

def displayinvetory(inventory):
    print("Hello! Today We Offer:")
    for k, v in inventory.items():
        print(f"{k} for {v}$")

displayinvetory(items)

while True:
    user_choise = input('"q" to checkout ) Items you Want to Buy? ').lower()

    if user_choise in items:
        list_of_items_in_cart.append(user_choise)
        print("This Item was added to your cart")
        print("Items in your Card:", list_of_items_in_cart)

    elif user_choise == "q":
        print("this will be:", total_sum_selected(items, list_of_items_in_cart), "$")
        user_pay_choise = input("How would you like to pay Cash or Credit Card? ").lower()

        total = total_sum_selected(items, list_of_items_in_cart)

        if user_pay_choise == "cash":
            wallet_after_pay = wallet - total
            print("Current Wallet Balance:", wallet_after_pay, "$")
            print("here's your receipt:")
            for x in list_of_items_in_cart:
                print(x)
            print("Thank you for Shopping")

        elif user_pay_choise == "credit card":
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
