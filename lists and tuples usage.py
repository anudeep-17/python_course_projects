print("this program print the mentioned birth date ")
date = input("please enter your birth date in DD-MM-YYYY:")
months = ["jan" , "feb" , "mar" , "apr" , "may" , "jun" ,"jul" , "aug" , "sep" , "oct" , "nov" , "dec"]
month = int(date[3:5])
print("your birth month is ", months[month-1])
