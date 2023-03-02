# Program calculates the cost of travel
# Feb 22, 2023
# CTI-110 P1HW2-Travel Expense
# Logan Simmons

## ******************* Pseudocode *******************
# Insert Blank Line
# Display "This program calculates and displays travel expenses"
# Display "------------------------------------------------"
# Ask user "Enter your budget:"
# Input budget
# Ask user "Enter your travel destination: "
# Input travel destination
# Ask user "How much do you think you will spend on gas? "
# Input cost of gas
# Ask user "Approximately, how much will you need for accomodation/hotel? "
# Input cost of hotel
# # Ask user "Last, how much do you need for food? "
# Input cost of food
# Equate how much money is left
# Display "------------Travel Expenses------------"
# Display Destination
# Display Budget
# Display Fuel Price
# Display Hotel Costs
# Display Food Costs
# Display Remainging Balance

print('\nThis program calculates and displays travel expenses')
print('------------------------------------------------')
budget = float(input('\nEnter budget: '))
destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
balance = budget-(gas+hotel+food)
print('\n------------Travel Expenses------------')
print('Location: ',destination)
print('Initial Budget: ',budget)
print('\nFuel: ',gas)
print('Accomodation: ',hotel)
print('Food: ',food)
print('\nRemaining Balance: ',balance)
