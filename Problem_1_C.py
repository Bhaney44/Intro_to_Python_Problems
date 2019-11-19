#Part C
#Finding the right amount to save
#Write a program to calculate the savings rate, as a function of starting salary.
#You want to save enough for a down payment in 36 months.
#Answer question: how much should you save each month?

#Use Bi-section search to find the savings rate.
    #The savings rate should be a portion of your annual salary,
    #allowing you to save enough for a down payment in 36 months.

#Starting salary
annual_salary = int(input('Enter the salary: '))

#Given variables
semi_annual_raise = 0.07
investment_rate = 0.04
total_cost = 1000000
down_payment = total_cost * 0.25

#Global variables
months = 0
current_savings = 0

#Bisection search variables
epsilon = 1000
low = 0
high = 10000

savings_rate = ((high + low)/2.0)/10000
monthly_savings = (annual_salary/12)*savings_rate


def calculate_savings(annual_salary, savings_rate):

    #Global variables
    global current_savings
    global monthly_savings

    #Reset monthly savings
    monthly_savings = (annual_salary/12)*savings_rate
    
    #Calculate current savings over 36 months
    for month in range(1,37):

        #Add semi-annual raise to salary
        if (months % 6 == 0):
            annual_salary += annual_salary*semi_annual_raise
            
        #Add monthly savings to current savings every month
        current_savings += (annual_salary/12) * savings_rate
        #Add investment income to current savings every month
        current_savings += (current_savings*investment_rate)/12

    return current_savings

calculate_savings(annual_salary, savings_rate)

# If saving all the income over 3 years doesn't produce more than the down payment,
    #then there is no way to save that much in 3 years.

if (calculate_savings(annual_salary, 1.0)) - down_payment >= 0:
    
    #Initialize bisection counter
    bisection_steps = 0

    #While the difference between the current savings and down payment is >= 100
    while abs((current_savings - down_payment)) >= epsilon:

        #Guess
        guess = (high + low)/2
        #If savings is less than down payment
            #Guess becomes the low boundry
        if current_savings < down_payment:
            low = guess

        #Else guess becomes the high boundry
        else:
            high = guess

        #Calculate new guess
        guess = (high + low)/2
        #Calculate new savings rate
        savings_rate = guess/10000

        #Count bisection search steps
        bisection_steps += 1
        
        #Reset current_savings
        current_savings = 0

        #Call function with original salary and new savings_rate
        calculate_savings(annual_salary, savings_rate)

    print('Best savings rate:', savings_rate)
    print('Steps in bisection search:', bisection_steps)
else:
    print('Not possible to save for down payment in 36 months.')

