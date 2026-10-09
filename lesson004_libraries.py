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

seed = 904.2
seed2 = math.pow(seed, 1)
print(seed2)
seed3 = seed2 * seed
print(seed3)
seed4 = seed3 * 312/2
result = math.ceil(seed2)
print("Your random number is:", result)

