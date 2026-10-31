# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(8.4)
print(f"Round down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANTS are varibales that never cahnge. They are written in all CAPS 

PI = math.pi
print(PI)
cat = "CAT"

import math 
DIAMETER = 14
RADIUS = DIAMETER/2
area = PI * RADIUS ** 2
print(f"The area of the circle is {area}")

#PYTHON RANDOM LIBARY 

# Python's library is a pseudorandom Number Generator 

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.00. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 
import math
seed = 904.2
seed2 = math.pow(seed, 1)
print(seed2)
seed3 = seed2 * seed
print(seed3)
seed4 = seed3 * 312/2
result = math.ceil(seed2)
print("Your random number is:", result)

# The one above does not work 

seed = 76743

for n in range(5):
    calcs = seed + 2234 * 22 / 3
    randint = math.ceil(calcs)
    print(f"Simple random num gen: {randint % 10}")
    seed += 1 


# Change the seed, get a new, pseudorandom number

# for s in range(5):

#     step1 = seed / 6.7
#     # print(step1)
#     step2 = step1 - 800.33
#     # print(step2)
#     step3 = step2 ** 3 
#     # print(step3)
#     round_up = math.ceil(step3)  
#     result = round_up % 10 # remainder between 0 and 6 (never 6)
#     print("Your random num is:", result)

#     seed = seed * 3 

# Pythons random library 

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]
random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

dice = ["1", "2", "3", "4", "5", "6"]
dice_roll1 = random.choice(dice)
print(dice_roll1)

# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with the math library.
num = random.randint(1,75)
square = math.sqrt(num)
rounded_sqr = math.ceil(square)
print(num)
print(square)
print(rounded_sqr)

# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, base to the POWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).
base_dice = random.randint(1,6)
exponent_dice = random.randint(1,6)
final_dice = math.pow(base_dice, exponent_dice)
print(f"base die is {base_dice}")
print(f"exponenet die is {base_dice}")
print(f"final_dice is {final_dice}")
