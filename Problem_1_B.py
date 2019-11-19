#Part B: Saving, with a raise
#Write a program that asks the user to enter the following variables
    #The starting annual salary
    #The semi-annual raise
    #The portion of the salary to be saved
    #The total cost of the dream home

#Return the number of months to pay for the down payment.

starting_annual_salary = int(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the portion of your salary to save as a decimal: '))
semi_annual_raise = float(input('Enter your semi-annual raise as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
down_payment = total_cost * 0.25

#Initialize variables
months = 0
current_savings = 0
investment_rate = 0.04
annual_salary = starting_annual_salary

def savings_calculator(starting_annual_salary, semi_annual_raise, portion_saved):

    #Global variables
    global current_savings
    global months
    global annual_salary

    #Exit loop when savings equals or exceeds down_payment
    while current_savings < down_payment:
        #In Python += adds a value to variable and assigns the result to the that variable
        
        #Monthly_savings
        monthly_savings = ((annual_salary/12)*portion_saved)
        
        #Add monthly savings to current savings every month
        current_savings += monthly_savings
        #Add investment income to current savings every month
        current_savings += (current_savings*investment_rate)/12

        #Add month
        months += 1
        
        #Add semi-annual raise to salary and adjust monthly savings accordingly
        #In Python == is a test for equality
        #In Python % is a modulus
            #Returns the remainder when the first operancd is divided by the second
        if (months % 6 == 0):
            annual_salary += annual_salary*semi_annual_raise


savings_calculator(starting_annual_salary, semi_annual_raise, portion_saved)


number_of_months = print('Number of months: ', months)
