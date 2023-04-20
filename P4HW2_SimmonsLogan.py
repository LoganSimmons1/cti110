# CTI-110
# P4HW2 - Salary Calculator
# Logan Simmons
# 4/20/2023

## Refered to P3HW2 - Salary
# define variables
# create true/if/else statement in order to create loop
# append variables
# print statements with variables implemented

total = 0
RegularPay = []
grossPay = []
overtimeRate = 1.5 
overtimePay = []
while True:
    name = input("\nEnter employee's name or \"Done\" to terminate: ")
    if name == "Done":
        break
    
    hours = int(input("How many hours did {} work? ".format(name)))
    payRate = float(input("What is {}\'s pay rate? ".format(name)))
    
    x = 0
    OP = RP = GP = 0.0
    if hours > 40:
        x = hours - 40 
        OP = x * overtimeRate *payRate
        RP = 40 * payRate 
        GP = OP + RP 
    else:
        OP = 0.0
        RP = hours * payRate
        GP = RP
    overtimePay.append(float(OP))
    RegularPay.append(float(RP))
    grossPay.append(float(GP))
    total = total + 1

    print("Employee Name: ", name)
    print(f'\n{"Hours worked":<16}{"Pay Rate":<17}{"OverTime":<16}{"OverTime Pay":<17}{"RegHour Pay":<17}{"Gross Pay":<17}')
    print("---------------------------------------------------------------------------------------------------")
    print(f'{hours:<16}${payRate:<16.2f}{x:<16}${OP:<16.2f}${RP:<16.2f}${GP:<16.2f}')


print("\nTotal number of employees entered: ",total)
print("Total amount payed for overtime: ", sum(overtimePay))
print("Total amount payed for regular hours: ", sum(RegularPay))
print("Total amount payed in gross: ", sum(grossPay))
