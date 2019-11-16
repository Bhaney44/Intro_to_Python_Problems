#Write a program that:
    # Asks the user to enter a number 'x'
    # Asks the user to enter a number 'y'
    # Prints out number 'x' to the power 'y'
    # Prints out the log base two of 'x'

import math

x = int(input('Enter a number: '))
y = int(input('Enter a number: '))
power = x**y
log = math.log(x, 2)

print(power)
print(log)
