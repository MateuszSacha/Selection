# mateusz sacha
#06-10-2014
# revision exercise 3
number = int(input("Im thinking of nine numbers. They all are positive and are between 1 and 100. Try to guess one of the numbers:"))
if number >= 21 and number <= 29:
    print("Congratulations! You have guesses one of the nine numbers!")
elif number < 21:
    print("The number you have entered is too low. Try again.")
elif number > 29:
    print("The number you entered is too large. Try again.")
