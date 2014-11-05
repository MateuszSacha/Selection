# Mateusz Sacha
# 13-10-2014
# selection spot check task 2a
name = input("Enter your Name:")
last_name = input("Enter your Last Name:")
gender = input("Enter your Gender. If Male enter m. If Female enter f:")
if gender ==("m"):
    print("Mr.{0} {1}".format(name,last_name))
elif gender ==("f"):
    print("Ms.{0} {1}".format(name,last_name))
else:
    print("Enter an appropriate gender.")
    
