import math 

# comment
# here 
# is 
# a 
# comment (control dash /)
print("hello world")
# variable declarations and types
a = 4       #integer
b = 5.5     #float
c = "CSAEA" #string
d = False   #boolean

print(a, b, c, d)

# OPERATORS
# + - / * (modulus, divides and gives you a remainder %) (expononent **) (integer division //)
# += -= /= 
e = 3 - 1 
print (e)
e += 7 
print(e)
# f-string

print(f"e is equal to {e}")

e -= 7
e += 12 

print(f"e is NOW eqaul to {e}")

# COMPAIRSONS (booleans, which always return True of False)

# < >   <=  >=  ==  !+

print ( 4 < 5 ) 
print(7 == 4)
print ( 1 != 2 )

isEqual = "Yes" != "YES"
print(isEqual)

# LOGICAL OPERATORS 
# In order of precedence: not and or 

f = False
t = True 
#predict output, Dont run)
print(not f)
print(f and t)
print(f or t)
print(f or t and not f)

#Truth table T F and False
#            F T and F
#            T T and F
#            F F and F 
# if the false is there its always going to be false even if there is a true hence if there is a double T then its true 
# Table truth or version: T F or True
#                         F T or true 
#                         T T or true
#                         F F or False 
#                       THEY CAN BE EITHER OR THE T F AND F T CAN ALSO BE FALSE but its perfered to be True 

# CASTING () 
g = int(5.9) 
print(g) 

s1 = "Goodnight"
s2 = " and " 
s3 = "Goodbye"
end = s1 + s2 + s3 # concatenation with + 
end += ", Cowboy."

print(end + "\n")

# MATH LIBRARY 
# max, min, square root, 
# to use math you need to "call it" sqrt = square root 
# ceil = round up
# floor = round down

print(math.sqrt(14))

#Coniditionals 

#if elif else 

t = True 
f = False 

if t: 
    print("Reached the first condition")
else: 
  print("Reached else")
  

print(math.ceil(3.65))
print(math.floor(8.94))
print(math.pow(2, 4)) 

# CONDITIONALS

# if    elif    else 

t = True
f = False

if f:
    print("Reached the first condition")
elif t:
    print("Reached Second Condition")
else: 
    print("Reached else")

if 100 > 500 and 99 == 1:
    print("Reached the first condition")
elif 6 == 7 or 5 < 2:
    print("Reached second condition")
elif 9 == 10 and 7 > 3:
    print("Reached third condition")
else: 
    print("Reached else")

# LISTS 
# A list can hold any tpye, and can grow or shrink at any time 

#index: 0   1   2  3  4
nums = [34, 52, 3, 64,32]

print(nums)
print (nums[3])
print (nums[0])
print(nums[-1])
print(nums[-3])

print(nums[0] + nums[2]) 

nums[0] = 64
print(nums) 

# LIST METHODS 
# Special built-in methods 

words = []

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")
print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)