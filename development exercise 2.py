# Mateusz Sacha
# 06-10-2014
# Development exercise 2
temperature = int(input("Enter a temperature:"))
if temperature < 0:
    print("At this temperature water would be frozen.")
elif temperature >=0 and temperature < 100:
    print("At this temperature water would not be frozen or boiling.")
elif temperature >=100:
    print("At this temperature water would be boiling.")
    
