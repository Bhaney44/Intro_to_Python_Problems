#Problem 1
#Part A: House Hunting

#Write a program that asks the user to enter the following variables
    #The starting annual salary
    #The portion of the salary to be saved
    #the total cost of the dream home

#Return the number of months to pay for the down payment.

total_cost = int(input('Enter the cost of your dream home: '))
annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion of your salary to save as a decimal: '))
down_payment = total_cost * 0.25
number_of_months = print('Number of months: ', (down_payment/(annual_salary*portion_saved)*12))

