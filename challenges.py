# 1. Tip Calculator
# A restaurant bill comes to $50. Calculate a 20% tip and the total, and print both using an f-string. Use math operators and an f-string.

b = 50
t = 0.2 * b
a = 60 
print(f"The tip is ${t} whist the total bill is ${a}")

# 2. Pizza Order
# You are ordering pizza for your class. Use the math library to calculate how many whole pizzas to order, then print how many extra slices will be left over. Use the math library and math operators.

import math
 
students = 23
slices_per_student = 2
slices_per_pizza = 8
total_slices_needed = students * slices_per_student
whole_pizzas = math.ceil(total_slices_needed/slices_per_pizza)
slices_in_total = whole_pizzas * slices_per_pizza
leftovers = slices_in_total - total_slices_needed
print(f"The amount of pizzas the class will have to order will be {whole_pizzas} with a remainder {leftovers} of slices")

# 3. A weather app gets temperatures in Fahrenheit. Convert to Celsius using C = (F - 32) * 5 / 9 and print the result in a full sentence. Use math operators and an f-string.
# Given:
f = 212
C = (f - 32) * 5 / 9
print(f"The Fahrenheit is {f} degrees while the Celsius is {C}")

# 4. Report Card
# Print the letter grade: 90+ is A, 80+ is B, 70+ is C, 60+ is D, anything lower is F. Change the score to test every grade. Use conditionals (if, elif, else) and comparisons.
score = 84  
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B") 
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D") 
else:
    print(F) 

# 5. Login Screen
# Print "Access granted" if the attempt matches the password exactly, otherwise print "Access denied". The given attempt was typed with Caps Lock on. Use comparisons and conditionals.
# Given:
password = "csaea2026"
attempt = "CSAEA2026"
if attempt == "csaea2026":
    print("Access granted")
else:
    print("Access denied")

# 6. Even/Odd Parking
# On street-sweeping days, cars with even license numbers park on the east side and odd numbers park on the west. Print which side this car should park on. Use the % math operator, comparisons, and conditionals.
# Given:
plate = 4827
if plate % 2 == 0:
    print("Park on the east side.")
else: 
    print("Park on the west side.")

# 7. Roller Coaster Gate
# Riders must be at least 48 inches tall. Riders under 10 years old also need an adult with them. Print whether this person may ride. Use logical operators and conditionals.
# They can ride if they meet the height requirement AND if they are ten years or older OR they have an adult
# IMPORTANT:::: The first part of the AND conditional ALWAYS has to be true or else the whole thing becomes falses and moves on to the elif or else
# Given:
height = 50
age = 8
has_adult = True
if height >= 48 and age >= 10 or has_adult == True:
    print("You may ride")
else: 
    print("You may not ride")

# 8. Name Tag Generator
# Combine the variables with string concatenation to print a conference name tag like the example. Use strings (concatenate with +).
first = "Ada"
last = "Lovelace"
school = "CSAEA"
student_info = first + " " + last + " who " + "attends " + school
print(f"Hello, I am {student_info}")

# 9. Shopping Cart
# The list holds the prices of the items in a shopping cart. Use a loop to add them up and print the total and the number of items. Use a for loop and len().
# Given:
cart = [12, 5, 30, 8]
total_price = 0 
for price in cart: 
    total_price += price 
item_count = len(cart)
print(f"total price is ${total_price}")
print(f"with {item_count} items in the cart")

#10. Grocery List Manager
# You already have eggs, you need cheese and rice, and apples are the most important item so they go first. Update the list using list methods, then print it and its length. Use list methods.
groceries = ["milk", "eggs", "bread"]
groceries.remove("eggs")
groceries.insert(0,"apples")
groceries.append("cheese")
groceries.append("rice")
print(groceries)
print(len(groceries))

