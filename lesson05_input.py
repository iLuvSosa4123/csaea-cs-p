# USER INPUT IN PYTHON
print("<PROMPT>")

name = input("Enter your name:")
print(f"Hello {name}")

print(type(name))


age = input("Enter your age: ")
print(f"Your age is {age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height: "))
print(f"You are {height} meters tall")
print(height + 1)

# Challenge 1: Favorite Color 
# Ask the user for their favorite color and print out a message using it. 
fav_color = input("What is your favourite color?:")
print(f"Wow {fav_color} is super cool")

# Challenge 2: Adding Two Numbers 
# Ask the user for two numbers, add them together, and print the results.
num1 = int(input("Insert a number"))
num2 = int(input("Insert another number"))
sum = num1 + num2
print(f"The sum of the two number is {sum}")
#Challenge 3 
print()      
diameter = int(input("Enter a random number for a diameter of a circle"))
radius = diameter/2
pi = 3.14
print(f"The area of the circle is { pi * radius ** 2 }")

