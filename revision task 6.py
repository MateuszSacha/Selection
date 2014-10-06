# Mateusz Sacha
# 06-10-2014
# revision exercise 6
number1 = int(input("Enter a number:"))
number2 = int(input("Enter a different number:"))
number3 = int(input("Enter a different number:"))
if number1 > number2 and number1 > number3:
    print("{0}:This is the largest number you have entered".format(number1))
elif number2 > number1 and number2 > number3:
    print("{0}:This is the largest number you have entered".format(number2))
elif number3 > number1 and number3 > number2:
    print("{0}:This is the largest number you have entered".format(number3))
    
    
