# Enhanced multiplication_table.py
# Generates multiplication tables for a range of numbers using nested loops

# Prompt user for starting and ending numbers
start = int(input("Enter the starting number for the multiplication table: "))
end = int(input("Enter the ending number for the multiplication table: "))

# Loop through each number in the range
for number in range(start, end + 1):
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
