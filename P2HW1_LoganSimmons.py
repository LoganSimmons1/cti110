# Program calculates the cost of travel-Formatted
# Mar 6, 2023
# CTI-110 P2HW1-Travel Expense
# Logan Simmons

## ******************* Pseudocode *******************
# Insert Blank Line
# Display "This program calculates and displays travel expenses"
# Display "------------------------------------------------"
# Ask user "Enter your budget:"
# Input budget
# Ask user "Enter your travel destination: "
# Input destination
# Ask user "How much do you think you will spend on gas? "
# Input gas
# Ask user "Approximately, how much will you need for accomodation/hotel? "
# Input hotel
# # Ask user "Last, how much do you need for food? "
# Input food
# Equate how much money is left
# Display "------------Travel Expenses------------"
# Display Destination
# Display Initial Budget in $(budget)
# Display Fuel in $(gas)
# Display Accomodation in $(hotel)
# Display Food in $(food)
# Display "---------------------------------------"
# Display Remainging Balance in $(balance)

print('\nThis program calculates and displays travel expenses')
print('------------------------------------------------')
budget = float(input('\nEnter budget: '))
destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
balance = budget-(gas+hotel+food)
print('\n------------Travel Expenses------------')
print(f'{"Location:":<20}{destination}')
print(f'{"Initial Budget:":<20}${budget}')
print(f'{"Fuel:":<20}${gas}')
print(f'{"Accomodation:":<20}${hotel}')
print(f'{"Food:":<20}${food}')
print('---------------------------------------')
print(f'\n{"Remaining Balance:":<20}${balance}')
