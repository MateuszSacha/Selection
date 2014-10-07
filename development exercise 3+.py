# Mateusz Sacha
# 07-10-2014
# Development Exercise 3
hours = int(input("Enter the number of hours you worked this week:"))
rate_of_pay = int(input("Enter your hourly rate of pay:"))
if hours >= 0 and hours <= 40:
    answer = hours * rate_of_pay 
    print("{0}: This is how much you have earned this week.".format(answer))
elif hours > 40:
    answer = hours * rate_of_pay
    answer1 = hours - 40
    answer2 = hours - 40 * 1.5
    print("{0}: This is how much you've earned this week with {0} hours which are 1.5 times more than your original hourly rate of pay.".format(answer + answer2)(answer1))
