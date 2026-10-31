#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_divide = 7 // 2 
print("integer division:", integer_divide)

mod = 7 % 2  
print("Modulus", mod)

exponent = 7 ** 2 
print("Exponent", exponent)

# PEMDAS (paranetheses, exponents, multiplication/division, addition/subtraction)

result = 2 + 3 * 4 
print("Result 1", result)


result2 = 2 ** 3 * 4 
print("Result 2", result2)

result3 = 5 + 2 ** 3 *  (4-1) 

w = 8
l = 5
Area = w * l 
print("The area of the rectangle", Area)

r = 7
pi = 3.14
area2 = pi * r **2
print("The area of the circle is", area2)

book = 12.99
notebook = 3.50
total = 3 * book + 4 * notebook
book_bought = 3
notebook_bought = 4
print(f"\tBook ${book * book_bought}\n\tNotebook ${notebook * notebook_bought} \n\t Total ${total} ")

value = 57 
if value%2 == 0:
    print("Even")
else:
    print("Odd")



