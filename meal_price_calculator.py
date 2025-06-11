# I added drinks & snacks to my meal price calculator
# ask for inputs
print()
child_meal = float(input("What is the price of child's meal? "))
adult_meal = float(input("What is the price of adults's meal? "))
drinks_meal = float(input("What is the price of the drinks meal? "))
snacks_meal = float(input("what is the price of the snacks meal? "))
# ask for the user for inputs 
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
number_of_drinks = int(input("How many drinks do you want? "))
number_of_snacks = int(input("How many snacks do you want? "))
print()
#calculating the sub total
children_sub_total = children * child_meal
adult_sub_total = adults * adult_meal
drinks_sub_total = drinks_meal * number_of_drinks
snacks_sub_total = snacks_meal * number_of_snacks
#displaying the sub total
sub_total =children_sub_total + adult_sub_total + drinks_sub_total + snacks_sub_total
print(f"Sub total: ${sub_total:.2f}")
print()
#ask for the sales tax
sales_tax_rate = float(input("What is the sales tax rate? "))

# calculate & display the sales tax
sales_tax =(sub_total * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f} ")

#calculate & display the total price
total = sub_total + sales_tax
print(f"Total: ${total:.2f}")
print()
# ask for payment amount
payment_amount = float(input("What is the payment amount? "))
#calculate the change
change = payment_amount - total
print(f"Change: ${change:.2f}")
print()

