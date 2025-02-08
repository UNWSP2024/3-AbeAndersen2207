#UNWSP Programming PythonCos2005DEsp25
#Week#3_Program#1_Shipping Charges
#02/06/2025
#Abraham. N. Andersen

# Prompt: Write a program that asks the user to enter a person's age.
# The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.
# Following are the guidelines:
# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 year old, he or she is an adult.


age = int(input("Please enter a person's age and I will classify whether or not they are an infant, child, teenager, or adult: "))
print("")
if age <= 1:
    print("The person of", age, "years is an infant.")
    print("")
elif age < 13:
    print("The person of", age, "years is a child.")
    print("")
elif age < 20:
    print("The person of", age, "years is a teenager.")
    print("")
else:
    print("The person of", age, "years is an adult.")
    print("")
print("Thank you for using this program. :)")
