#first prediction for question 1: 3.5 1 -3.5
import math 
f = False
t = True 
nums = [34, 52, 3, 64, 32] 
print(7//2, 7% 2, -7 // 2)

#second prediction, -5 , -6 
print(int(-5.9),math.floor(-5.9))
# The two values differ because int causes 5.9 to be rounded to the nearest whole number since int means integer. In contrast, floor means rounding down so the number gets rounded down regardless of the decimal.

#Third prediction 15 , 10
print("5" * 3,  "5" + "5")

#Fourth Prediciton 8, 2 4 8
print(2 ** 4, math.pow(2, 4))

#5 predict the output 
print(True + True + True)

#6 Predict output. Surprised? Explain. 
print(0.1 + 0.2 == 0.3)

#7 Predict the output. Explain 
print("Zebra < apple")

#8. Predict the output. Show the order Python evaluates it.
print(not f or t and f)

#9. Predict the output.
print(nums[-len(nums)])

#10. Predict every line of output.
for i in range(10, 0, -3):
    print(i)

#11. Predict every line of output. Does 11 print? Why?
x = 5
while x < 10:
    x += 2
    print(x)

