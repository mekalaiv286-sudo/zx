# Program to print 5 lines of sums in Python

# Define pairs of numbers
pairs = [(2, 3), (5, 7), (10, 15), (20, 25), (100, 200)]

# Loop through each pair and print the sum
for a, b in pairs:
    try:
        total = a + b
        print(f"{a} + {b} = {total}")
    except TypeError:
        print(f"Invalid data for sum: {a}, {b}")
