# Program calculates the Area of a Rectangle
# Feb 08, 2023
# AreaOfRectangle
# Logan Simmons
## ******************* Pseudocode *******************
# Insert Blank Line
# Display "This program calculates the Area of a Rectangle"
# Display "------------------------------------------------"
# Ask user "Enter your name:"
# Input name
# Ask user "Enter Rectangle Length: "
# Input length
# Ask user "Enter Rectangle Width: "
# Input width
# Set area = length * width
# Display "Length entered:" length
# Display "Width entered:" width
# Display "====================================================="
# Display name "the Area of your Rectangle is:" area

print('\nThis program calculates the Area of a Rectangle')
print('------------------------------------------------')
name = input('Enter your name:\n')
length = int(input('Enter Rectangle Length:\n'))
width = int(input('Enter Rectangle Width:\n'))
area = length * width
print('Length entered:', length)
print('Width entered:', width)
print('=====================================================')
print(name, 'the Area of your Rectangle is:', area)
