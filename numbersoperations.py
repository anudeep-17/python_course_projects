print("  ")

import math

print("this program calculates area and circufrence")
num1 = float(input("please enter the radius of circle:"))
print("area of the circle is :",round( math.pi * (num1*num1),3))
print("the circumference of the circle is ", round(2 * math.pi * num1 , 3))
