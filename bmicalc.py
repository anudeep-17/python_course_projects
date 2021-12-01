print("bmi calculator")

a = float(input("enter your height : "))
b = float(input("enter your weight : "))

bmi = b/(a*a)

if(bmi <= 18.5):
    print("you are under weight")
    
elif(bmi >= 18.5 or bmi <= 24.9):
    print("you are normal")

elif(bmi>=24.9 or bmi<=29.9):
    print("over weight")

else:
    print("obesity")
