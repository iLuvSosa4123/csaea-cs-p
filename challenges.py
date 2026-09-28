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

# 11. Rocket Launch
# Use a for loop to count down from start to 1, then print "Liftoff!". Use a for loop with range(start, stop, step).
# Given:
start = 10
for count in range(start, 0 ,-1):
    print(count)    
print("liftoff!")

# 12. Times Table Helper
# A younger student needs help with a times table. Use a for loop to print number x 1 through number x 10. Use a for loop with range(start, stop) and an f-string.
# Given:
number = 7
for multiplier in range(1, 11):
    print(f"{number} * {multiplier} = {number * multiplier}")
# 13. Savings Goal
# You save the same amount every week toward headphones. Use a while loop to find how many weeks it takes to reach the goal, then print the weeks and your final savings. Use a while loop.
# Given:
savings = 0
weekly_deposit = 15
goal = 100
weeks = 0
while savings < goal:
    savings += weekly_deposit   
    weeks += 1  
print(f"{weeks} weeks to reach the goal with a total of ${savings} deposited")

# 14. High Score
# Using a loop and an if statement (no max() allowed), find and print the highest score. Use a for loop, comparisons, and conditionals.
scores = [340, 1250, 980, 1510, 720]
highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")

# 15. Class Pass Rate
# Count how many students passed (a grade at or above passing) and print the count out of the class size. Use a for loop, comparisons, and conditionals.
# Given:
grades = [88, 65, 72, 91, 54, 70]
passing = 70
passed_count = 0
failed_count = 0
for grade in grades:
    if grade >= passing:
        passed_count += 1
    elif grade < passing:
        failed_count += 1

print(f"The amount of people passing is {passed_count} while the amount of people failing is {failed_count}")

# 16. Garden Fence
# A square garden has the area below, in square feet. Use the math library to find the length of one side, then print how many feet of fencing go around it. Use the math library.
# # Given:
import math
area = 49
side = math.sqrt(area)
perimeter = side * 4
print(f"The perimeter is {perimeter}ft whilst one side is {side}ft")

# 17. Parking Meter
# Parking is charged in blocks of time, and any started block counts as a full block. Print how much this driver owes. Use the math library and math operators.
# Given:
import math
minutes_parked = 50
block_length = 15
cost_per_block = 1
blocks_used = math.ceil(50/15)
driver_owes = blocks_used * cost_per_block 
print(f"The driver owes ${driver_owes}")

# 18. Playlist Swap
# A DJ wants the first and last songs to trade places. Swap them using indexes and print the new playlist. Your code should still work if songs are added to the middle. Use lists and indexes (including negative indexes).
# Given:
playlist = ["Intro", "Song A", "Song B", "Finale"]
playlist[0], playlist[-1] = playlist[-1], playlist[0]
print(playlist)

# 19. Leap Year Checker
# A year is a leap year if it is divisible by 4, except years divisible by 100 are not, unless they are also divisible by 400. Print whether the year is a leap year. Also test 2024 and 2000. Use the % math operator, logical operators, and conditionals.
# Given:
year = 1900
years_to_test = [2026, 2000, 2024, 1900]
for year in years_to_test:
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year} is not leap year") 
    elif year % 4 == 0:
        print(f"{year} is a leap year") 
    else:
        print(f"{year} is not leap year")

# 20. Speed Trap
# Drivers 1 to 10 mph over the limit get a warning, 11 to 20 over pay $100, and more than 20 over pay $250. Print the result for this driver. Use math operators and conditionals (if, elif, else).
speed_limit = 55
speed = 71
mph_over = speed - speed_limit
if mph_over > 20:
    print("warning!")
elif mph_over > 11:
    print("$100 fine")
elif mph_over > 1:
    print("Warning!")
else:
    print("Safe driving!")
    

