# CTI-110
# P2HW2 - List
# Logan Simmons
# 3/12/2023

## ******************* Pseudocode *******************
# Insert Blank Line
# Display "------------------------------------------------"
# Display "Enter grade for Module 1: "
# Input mod1
# Display "Enter grade for Module 2: "
# Input mod2
# Display "Enter grade for Module 3: "
# Input mod3
# Display "Enter grade for Module 4: "
# Input mod4
# Display "Enter grade for Module 5: "
# Input mod5
# Display "Enter grade for Module 6: "
# Input mod6
# Create list and input module values
# Insert Blank Line
# Display "------------Results------------"
# Display "Lowest Grade: "
# Display "Highest Grade: "
# Display "Sum of Grades: "
# Calculate the average of the list
# Display "Average: "
# Display "---------------------------------------"

print('------------------------------------------------')
mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))
gradeList = [mod1, mod2, mod3, mod4, mod5, mod6]
print('\n------------Results------------')
print(f'{"Lowest Grade:":<20}', min(gradeList))
print(f'{"Highest Grade:":<20}', max(gradeList))
print(f'{"Sum of Grade:":<20}', sum(gradeList))
Avg = sum(gradeList) / len(gradeList)
print(f'{"Average:":<21}{Avg:.2f}')
print('---------------------------------------')

