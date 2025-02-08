#UNWSP Programming PythonCos2005DEsp25
#Week#3_Program#5_Hot Dog
#02/06/2025
#Abraham. N. Andersen

# Prompt: There are two kinds of hot dogs sold:  Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally, a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%. Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

#Establish prices for menu items
Hot_Dog_Price = 3.50
Chili_Dog_Price = 4.50
Cheese_Price = 0.50
Peppers_Price = 0.75
Onions_Price = 1.00
None_Price = 0.00
Tax_Rate = 0.07

# Get hot dog type from user
print("Hello and welcome to the place where people buy hot dogs. ")
print("")
print("I am assuming you are here to buy a hot dog!")
print("")
print("Let us see how much it would cost you to buy one with all the toppings you'd like on it. ")
print("")
hot_dog_type = input("First enter which hot dog type you would like; Enter 'Hot Dog' or 'Chili Dog' : ")

# Define toppings
toppings = []

# Get toppings from user
while True:
    topping = input("Enter toppings you would like (Cheese, Peppers, Onions, None, and enter Done when finished): ")
    if topping == "Done":
        break
    toppings.append(topping)
    if topping == "None":
        break
    toppings.append(topping)

# Calculate the base price
if hot_dog_type == "Hot Dog":
    base_price = Hot_Dog_Price
elif hot_dog_type == "Chili Dog":
    base_price = Chili_Dog_Price
else:
    print("Invalid hot dog type.")
    exit()

# Calculate topping costs
topping_cost = 0
for topping in toppings:
    if topping == "Cheese":
        topping_cost += Cheese_Price
    elif topping == "Peppers":
        topping_cost += Peppers_Price
    elif topping == "Onions":
        topping_cost += Onions_Price
    elif topping == "None":
        topping_cost += None_Price
    else:
        print("Invalid topping.")
        exit()

# Calculate subtotal
subtotal = base_price + topping_cost

# Calculate tax
tax = subtotal * Tax_Rate

# Calculate total cost
total_cost = subtotal + tax

# Print the results
print("  Your Recipt:")
print(f"Hot Dog Cost: ${base_price:.2f}")
print(f"Topping Cost: ${topping_cost:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print("  Sorry we have no physical Hot Dogs, but Thank you for doing business. Have a great day. :)")
