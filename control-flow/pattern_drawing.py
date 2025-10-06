# pattern_drawing.py
# This script draws a square pattern of asterisks based on user input using a while loop and a nested for loop.

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
