#UNWSP Programming PythonCos2005DEsp25
#Week#3_Program#3_Shipping Charges
#02/06/2025
#Abraham. N. Andersen

# Prompt:The Fast Freight Shipping Company charges the following rates:
#    Weight    	                           Price Per Pound
# 2 pounds or less   	                        $1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	    $4.00
# Over 10 pounds                                $4.75

print("Would you like to know how much it is to ship that package? ")
print("")
weight = float(input("To find the cost of shipping for your parcel, "
                     "Enter the weight of the package in pounds here: "))
def calculate_shipping_cost(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif weight <= 6:
        price_per_pound = 3.00
    elif weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75

    shipping_cost = weight * price_per_pound
    return shipping_cost

shipping_cost = calculate_shipping_cost(weight)

print("The shipping cost for this item is $", shipping_cost)
print("Thank you for using this program. :)")