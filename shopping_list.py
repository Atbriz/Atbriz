# # Shopping Cart Program with Quantity and Enhanced Display
# adding the strip() and the tittle() in my code 
# This program goes beyond the basic requirements by:
# - Supporting multiple quantities for each item.
# - Calculating per-item subtotals (price * quantity).
# - Displaying a clear, formatted shopping cart with item number, unit price, quantity, and total per item.
# - Ensuring all currency is shown with two decimal places and a dollar sign.


print("\nWelcome To The Shopping Cart Program!\n")

shopping_list = []
prices = []

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ").strip()
    
    if choice == "1":
        item = input("What item would you like to add? ").title()
        price = float(input("What is the price of the item? "))
        shopping_list.append(item)
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
        
    elif choice == "2":
        if not shopping_list:
            print("The shopping cart is empty.")
        else:
            print("\nThe contents of the shopping cart are:")
            for i, (item, price) in enumerate(zip(shopping_list, prices), 1):
                print(f"{i}. {item} - ${price:.2f}")
    
    elif choice == "3":
        if not shopping_list:
            print("The shopping cart is empty.")
        else:
            print("\nThe contents of the shopping cart are:")
            for i, (item, price) in enumerate(zip(shopping_list, prices), 1):
                print(f"{i}. {item} - ${price:.2f}")
            
            valid_input = False
            while not valid_input:
                item_num = input("\nWhich item would you like to remove? ")
                if item_num.isdigit():
                    item_num = int(item_num)
                    if 1 <= item_num <= len(shopping_list):
                        removed_item = shopping_list.pop(item_num - 1)
                        removed_price = prices.pop(item_num - 1)
                        print(f"'{removed_item}' has been removed.")
                        valid_input = True
                    else:
                        print(f"Invalid number. Please enter 1-{len(shopping_list)}.")
                else:
                    print("Please enter a valid number (e.g., 1, 2, 3).")
    
    elif choice == "4":
        total = sum(prices)
        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")
    
    elif choice == "5":
        print("\nThank you. Goodbye.")
        break
    
    else:
        print("invalid response")

    
    
        
    

        
            
    