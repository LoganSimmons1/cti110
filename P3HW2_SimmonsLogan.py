# CTI-110
# P3HW2 - Salary
# Logan Simmons
# 3/27/2023

# "Enter employee name: input"
# "Enter number of hours worked: input"
# "Enter employee pay rate: input"
# print line "--------"
# print "Employee name: input"
# print Headers "Hours Worked", "pay rate", etc
# print line "--------"
# define equations and variables
# print header outputs (equations and variables)

var1 = input('Enter employee name: ')
var2 = float(input('Enter number of hours worked: '))
var3 = float(input('Enter employee pay rate: '))
print('---------------------------------------')
print(f'{"Employee name:":<15}', var1)
print(f'\n{"Hours worked":<16}{"Pay Rate":<16}{"OverTime":<16}{"OverTime Pay":<16}{"RegHour Pay":<16}{"Gross Pay":<16}')
print('----------------------------------------------------------------------------------------------')
oth = var2 - 40
otp = oth * (var3*1.5)
regh = var2 - oth
regp = regh * var3
gpay = otp + regp
print(f'{var2:<16.2f}${var3:<16.2f}{oth:<16.2f}${otp:<16.2f}${regp:<16.2f}${gpay:<16.2f}')
