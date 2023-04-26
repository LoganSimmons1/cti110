# CTI-110 P5HW - Math Quiz
# Logan Simmons
# 4/25/2023
# A brief description of the project

# Create Main Menu
# Have three options to choose from
# Define functions/ one for adding, one for subtraction
# Generate two random numbers
# Carry out operation
# Ask for input
# If wrong Display "Sorry, guess is too low." or Display "Sorry, guess is too low."
# If correct display "Congratulations!!!! your answer is correct..."
# Reloop main menu
# Carry out operations infinitely using loop.
##
# The given Python code implements a simple math game that allows the user to choose between adding or subtracting random numbers. The game has a menu with three options: Addition, Subtraction, or Exit

import random

def addRandom():
    n1 = random.randint(0, 1000)
    n2 = random.randint(0, 1000)
    print(f"{n1:>6}")
    print(f"+{n2:>5}")
    print("Enter answer")
    ans = int(input())
    while ans != n1 + n2:
        if ans < n1 + n2:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high")
        ans = int(input("Try again: "))
    print("Congratulations!!!! your answer is correct...")

def subRandom():
    n1 = random.randint(0, 1000)
    n2 = random.randint(0, 1000)
    print(f"{n1:>6}")
    print(f"-{n2:>5}")
    print("Enter answer")
    ans = int(input())
    while ans != n1 - n2:
        if ans < n1 - n2:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high")
        ans = int(input("Try again: "))
    print("Congratulations!!!! your answer is correct...")

if __name__ == "__main__":
    while True:
        print("MAIN MENU")
        print("----------------------")
        print("1) Add Random Numbers ")
        print("2) Subtract Random Numbers")
        print("3) Exit")
        num = int(input("\nPlease choose one of the menu options: "))
        if num == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        elif num == 1:
            addRandom()
        elif num == 2:
            subRandom()
        else:
            print("Invalid option. Please choose again")
