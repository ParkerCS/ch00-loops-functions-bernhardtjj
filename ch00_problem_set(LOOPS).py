#21/22
# LOOPS (22pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
# The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
yesterday = 0
today = 1
tomorrow = 1
print(1, end=' ')
while today < 1000:
    tomorrow = yesterday + today
    yesterday = today
    today = tomorrow
    print(today, end=' ')

# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly


print()
number = random.randrange(1, 1001)
guess = 0
while guess != number:
    try:
        guess = int(input("Give me a guess: "))
        if 1000 < guess or guess < 1:
            raise ValueError
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
    except ValueError:
        print("Has to be an integer between 1 and 1000")
print("You are right.")

# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

success = 0
failure = 0
print()
print("Calculating using one million trials:")
for i in range(1000000):
    die_list = []
    for die in range(6):
        die_list.append(random.randrange(1, 7))
    if (die_list[0] <= die_list[1]) and (die_list[1] <= die_list[2]) and (die_list[2] <= die_list[3]) and (
                die_list[3] <= die_list[4]) and (die_list[4] <= die_list[5]):
        success += 1
    else:
        failure += 1
print(round(success / (success + failure) * 100, 2), "%")

# Lee - Should be a five dice roll, not 6.  Otherwise, perfect (-1)

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
print()
for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(1, 10):
                if int(str(D) + str(C) + str(B) + str(A)) == 4 * int(str(A) + str(B) + str(C) + str(D)):
                    print(A, B, C, D);
                    quit()
