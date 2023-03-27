# CTI-110
# P3HW1 - Debugging
# Simmons


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

gradeList = [mod1, mod2, mod3, mod4, mod5, mod6]
# TO DO: determine lowest, highest , sum and average for grades

print('\n------------Results------------')
print(f'{"Lowest Grade:":<20}', min(gradeList))
print(f'{"Highest Grade:":<20}', max(gradeList))
print(f'{"Sum of Grade:":<20}', sum(gradeList))
Avg = sum(gradeList) / len(gradeList)
print(f'{"Average:":<21}{Avg:.2f}')
print('---------------------------------------')

# determine letter grade for average

if Avg >= 90:
    print('Your grade is: A')

elif Avg >= 80:
    print('Your grade is: B')

elif Avg >= 70:
    print('Your grade is: C')

elif Avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')

    
# TO DO: finish this





