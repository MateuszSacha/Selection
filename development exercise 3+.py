# Mateusz Sacha
# 07-10-2014
# Development Exercise 3
hours = int(input("Enter the number of hours you worked this week:"))
rate_of_pay = int(input("Enter your hourly rate of pay:"))
if hours >= 0 and hours <= 40:
    answer = hours * rate_of_pay 
    print("{0}: This is how much you have earned this week.".format(answer))
elif hours > 40:
   answer1 = hours*(rate_of_pay*1.5)
   print("{0}: this is how much you've earned adding the extra hours.".format(answer1))
elif hours > 60:
    print("Enter a number between 0 and 60.")
elif hours < 0 :
    print("Enter a number beween 0 and 60.")
    
   
   
    
