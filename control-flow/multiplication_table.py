# multiplication_table.py
# This script prints the multiplication table for a given number using a for loop.

# Prompt the user for a number with the exact required input string
number = int(input("Enter a number to see its multiplication table:"))

# Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
