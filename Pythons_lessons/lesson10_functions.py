# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_hi()
say_bye

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a functions PARAMTER

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT
    return e

expression = express_this(True) # the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

def remainder(a,b):
    return a % b

result = remainder(10, 9)
print(result)

def is_far(distance):

    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance < 20:
        return "Hey that's pretty close by!"
one = is_far(120)
two = is_far(63)
three = is_far(2)
four = is_far(1000000)

print(one, two, three, four)

test_distances = [ 150, 50, 20, 10]
for dist in test_distances:
    result = is_far(dist)
    print(f"Distance {dist}: {result}")
#call is_far() on four different distances, and print the result


# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler() that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 

def doubler(num, times):
    doubled_numbers = []
    number = num

    for n in range(times):
        number = number * 2
        doubled_numbers.append(number)

    print(doubled_numbers)
    return doubled_numbers

doubler(1, 5)


# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers and print and return the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result

def adder(a, b):
    print(a + b)
    return a + b

def subtracter(a, b):
    print(a - b)
    return a - b

def divider(a, b):
    print(a/b)
    return a/b

def multiplier(a, b):
    print(a*b)
    return a*b


# Challenge 2
# Make a function called 'average' that:
# 1) accepts five numbers
# 2) returns the average
# 3) print the returned value outside the function

def pri(a, b, c):
    print((a + b + c)/3)
    return pri((a + b + c)/3)

# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd

def even_odd(a):
    if a % 2 == 0: 
        print("Even")
        return "Even"
    else:
        print("Odd")
        return "Odd"

    
# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a f-string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function

def analyze_word(word):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1 
    return{"vowels": v_count, "constonants": c_count}
