print("----------------------------------------")
import random
print("this is to choose names at random")


for x in range(0,8):
    str1 = input("enter uour name ")
    names = []
    names.append(str1)
    

print("the randomly chosen name is " , random.choice(names))
