# 20/20
# SECTION 2 - FUNCTIONS (20PTS TOTAL)
from math import *

# PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
string = input("Give me some string: ")
print(len(string))
# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
try:
    leg_one = float(input("Give me a leg: "))
    leg_two = float(input("Give me a leg: "))
    print("The third side is {:0.2f}".format(sqrt(leg_one ** 2 + leg_two ** 2)), "units")
except ValueError:
    print("Legs have to be numbers or I won't give you the hypotenuse.")


# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

def nicefunction(x, y, z):
    print("The max is {:0.2f}.".format(round(max(x, y, x), 2)))
    print("The min is {:0.2f}.".format(round(min(x, y, x), 2)))
    print("The avg is {:0.2f}.".format(round((x + y + x) / 3, 2)))


try:
    nicefunction(float(input("First number: ")), float(input("Second number: ")), float(input("Third number: ")))
except ValueError:
    print("Numbers are not words.")

#exceptions.  Nice.


# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
for i in range(-1, 4):
    print("e^" + str(i) + " = {:0.2f}.".format(e ** i))
# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
from random import random

print(random() * 9 + 1)


# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def hi(x, y):
    return x + y, x * y


print(hi(1, 2)[0], hi(1, 2)[1])
